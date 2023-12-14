```markdown
# In-Memory File System

This is a simple in-memory file system implementation with basic file system operations. The file system supports commands like `mkdir`, `cd`, `ls`, `touch`, `echo`, `mv`, `cp`, `rm`, and more.

## Getting Started

1. Clone the repository:

   ```bash
      https://github.com/RudraPrasadSwain/project_rudraprasad_120BT0038.git
   ```

2. Navigate to the project directory:

   ```bash
   cd in-memory-file-system
   ```

3. Run the script:

   ```bash
   python filesystem.py
   ```

   Or for Python 3:

   ```bash
   python3 filesystem.py
   ```

## Usage

The file system script runs in an interactive loop. Enter commands at the prompt (">") to interact with the file system.

### Commands:

- **Create a new directory:**
  ```bash
  mkdir my_directory
  ```

- **List contents of the current directory:**
  ```bash
  ls
  ```

- **Change directory:**
  ```bash
  cd my_directory
  ```

- **Create a new empty file:**
  ```bash
  touch my_file.txt
  ```

- **Write text to a file:**
  ```bash
  echo 'Hello, World!' > my_file.txt
  ```

- **Display the contents of a file:**
  ```bash
  cat my_file.txt
  ```

- **Move a file to another location:**
  ```bash
  mv my_file.txt new_location/
  ```

- **Copy a file to another location:**
  ```bash
  cp my_file.txt copy_of_file.txt
  ```

- **Remove a file:**
  ```bash
  rm my_file.txt
  ```

### Exiting the Program:

To exit the program and end the loop, type:

```bash
exit
```

### Save and Load State (Optional):

- **Save the current state to a file:**
  ```bash
  save_state saved_state.json
  ```

- **Load the state from a saved file:**
  ```bash
  load_state saved_state.json
  ```

## Advanced Usage

### Save and Reload State (Bonus Feature)

You can save the current state of the file system and reload it later. Use the `save_state` and `load_state` commands.

- **Save the current state to a file:**
  ```bash
  save_state saved_state.json
  ```

- **Load the state from a saved file:**
  ```bash
  load_state saved_state.json
  ```


