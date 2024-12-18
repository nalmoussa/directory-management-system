# Directory Management System

This project implements a simple directory management system in Python. It allows users to create, delete, move, and list directories in a virtual file system.

## Features

- Create directories
- Delete directories
- Move directories
- List directory structure
- Interactive command-line interface

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository
2. Move into the repository folder after you clone it
3. Ensure Python is added to the System's PATH environment variable

## Running the Code

To start the directory management system, navigate to the project directory and run:

```bash
python directories.py 
```

This will start an interactive session where you can enter commands. Available commands:

- **CREATE path**: Creates a new directory
- **DELETE path**: Removes a directory
- **MOVE source destination**: Moves a directory to a new location
- **LIST**: Shows the current directory structure
- **HELP [command (Optional)]**: Displays command information
- **EXIT**: Quits the program

## Running the Tests

To execute the unit tests, run:

```bash
python -m unittest discover -s tests 
```

This should execute 30 unit tests

## Future Work (Potentially)

- Define some hierarchical depth limit
- Try to find more edge cases and handle them gracefully
- Add official execution logs
- I also considered adding a config file to define business logic (should we allow overrides?, how long can the directory name be?, etc.)
