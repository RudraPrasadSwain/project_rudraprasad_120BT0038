import os
import json
import argparse

class FileSystem:
    def __init__(self):
        self.root = Directory('/')
        self.current_directory = self.root

    def change_directory(self, path):
        if path == '..':
            self.current_directory = self.current_directory.parent
        elif path == '/':
            self.current_directory = self.root
        else:
            self.current_directory = self.current_directory.find_directory(path)

    def create_directory(self, name):
        if name in self.current_directory.children:
            raise Exception('Directory already exists')
        new_directory = Directory(name, self.current_directory)
        self.current_directory.children[name] = new_directory

    def create_file(self, name):
        if name in self.current_directory.children:
            raise Exception('File already exists')
        new_file = File(name, self.current_directory)
        self.current_directory.children[name] = new_file

    def delete_directory(self, name):
        directory = self.current_directory.find_directory(name)
        del self.current_directory.children[directory.name]

    def delete_file(self, name):
        file = self.current_directory.find_file(name)
        del self.current_directory.children[file.name]

    def write_file(self, name, content):
        file = self.current_directory.find_file(name)
        file.content = content

    def read_file(self, name):
        file = self.current_directory.find_file(name)
        return file.content

    def save_state(self, filename):
        file_system_data = {
            'root': self.root.serialize(),
            'current_directory': self.current_directory.serialize()
        }
        with open(filename, 'w') as f:
            json.dump(file_system_data, f)

    def load_state(self, filename):
        with open(filename, 'r') as f:
            file_system_data = json.load(f)
        self.root = Directory.deserialize(file_system_data['root'])
        self.current_directory = Directory.deserialize(file_system_data['current_directory'])

class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = {}

    def find_directory(self, path):
        if path == '.':
            return self
        if path == '/':
            return self.root
        components = path.split('/')
        current_directory = self
        for component in components:
            if component == '..':
                current_directory = current_directory.parent
            else:
                current_directory = current_directory.children[component]
        return current_directory

    def find_file(self, name):
        return self.children[name]

    def serialize(self):
        serialized_children = {}
        for child in self.children.values():
            serialized_children[child.name] = child.serialize()
        return {
            'name': self.name,
            'parent': self.parent.name if self.parent else None,
            'children': serialized_children
        }

    @staticmethod
    def deserialize(serialized_directory):
        name = serialized_directory['name']
        parent = None
        children = {}
        for child in serialized_directory['children'].values():
            if child['type'] == 'directory':
                children[child['name']] = Directory.deserialize(child)
            else:
                children[child['name']] = File.deserialize(child)
        return Directory(name, parent, children)

class File:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.content = ""

    def serialize(self):
        return {
            'name': self.name,
            'parent': self.parent.name if self.parent else None,
            'content': self.content
        }

    @staticmethod
    def deserialize(serialized_file):
        name = serialized_file['name']
        parent = None
        content = serialized_file['content']
        return File(name, parent, content)

fs = FileSystem()
if __name__ == "__main__":
    
    
    while True:
        command = input("> ")
        if command.lower() == "exit":
            break

        try:
            parts = command.split(' ')
            operation = parts[0]
            args = parts[1:]

            if hasattr(fs, operation):
                getattr(fs, operation)(*args)
            else:
                print(f"Invalid command: {operation}")

        except Exception as e:
            print(f"Error: {str(e)}")
