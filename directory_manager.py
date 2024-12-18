from directory_structure import DirectoryStructure
from exceptions import EmptyStatementError


class DirectoryManager:
    def __init__(self):
        """
        Initializes the DirectoryManager with a DirectoryStructure instance
        and a command map for user commands.
        """
        self.structure = DirectoryStructure()
        self.command_map = {
            "CREATE": self.structure.create_directory,
            "MOVE": self.structure.move_directory,
            "DELETE": self.structure.delete_directory,
            "LIST": self.structure.print_directory,
            "HELP": self.print_help,
            "EXIT": self.exit_program,
        }

    def print_help(self, command: str = None) -> None:
        """
        Displays all available commands and their descriptions.
        If a specific command is provided, displays detailed help for that command only.

        Args:
            command (str, optional): The command to get help for. If provided, shows help
            for that specific command only. Must be one of: CREATE, DELETE, MOVE,
            LIST, HELP, or EXIT. Defaults to None.
        """
        if command:
            command = command.upper()
            if command in self.command_map:
                print(f"{command}: {self.command_map[command].__doc__}")
            else:
                print(f"Unknown command: {command}")
                print("Use HELP to see available commands")

        else:
            # print all commands and their descriptions
            print("Available commands:")
            for command, function in self.command_map.items():
                print(f"{command}: {self.command_map[command].__doc__}")

    def exit_program(self) -> None:
        """
        Terminates the program execution by raising an EOFError.
        This method is typically called when the user wants to exit the application.

        Raises:
            EOFError: Signal to terminate the program execution
        """
        raise EOFError

    @staticmethod
    def _validate_command_args(command: str, args: list) -> bool:
        """
        Validates the number and type of arguments for a command.

        Args:
            command (str): The command to validate
            args (list): The arguments to validate

        Returns:
            bool: True if arguments are valid, False otherwise
        """
        command_args = {
            'CREATE': [1],
            'DELETE': [1],
            'MOVE': [2],
            'LIST': [0],
            'HELP': [0, 1],
            'EXIT': [0]
        }

        return len(args) in command_args.get(command.upper(), [0])

    @staticmethod
    def normalize_path(path: str) -> str:
        """
        Normalizes a directory path by removing leading and trailing slashes.

        Args:
            path (str): The path to normalize

        Returns:
            str: The normalized path
        """
        import re
        path = path.strip()
        if path.startswith('/'):
            path = path[1:]
        if path.endswith('/'):
            path = path[:-1]
        return re.sub(r'/{2,}', '/', path)

    @staticmethod
    def _validate_path(path: str) -> bool:
        """
        Validates a directory path.

        Args:
            path (str): The path to validate

        Returns:
            bool: True if path is valid, False otherwise
        """
        if not path:
            return False

        # Check for invalid characters
        invalid_chars = set('<>:"|?*')
        if any(char in path for char in invalid_chars):
            return False

        # Check path components
        path = DirectoryManager.normalize_path(path)
        parts = path.split('/')
        return all(part and not part.isspace() for part in parts)

    @staticmethod
    def _get_command_usage(command: str) -> str:
        """
        Returns the usage string for a command.

        Args:
            command (str): The command to get usage for

        Returns:
            str: Usage string for the command
        """
        usage = {
            'CREATE': 'CREATE <path>',
            'DELETE': 'DELETE <path>',
            'MOVE': 'MOVE <source_path> <destination_path>',
            'LIST': 'LIST',
            'HELP': 'HELP [command]',
            'EXIT': 'EXIT'
        }
        return usage.get(command.upper(), '')

    @staticmethod
    def parse_statement(statement: str) -> tuple:
        """
        Parses a statement into a command and its arguments.

        Args:
            statement (str): The statement to parse

        Returns:
            tuple: A tuple containing the command and its arguments

        Raises:
            ValueError: If the statement is empty
        """
        if not statement:
            raise EmptyStatementError

        statement_parts = statement.split()
        command = statement_parts[0] if statement_parts else ''
        args = statement_parts[1:] if len(statement_parts) > 1 else []

        return command, args

    def process(self, command: str, args: list) -> None:
        """
        Processes user commands with input validation and error handling.

        Args:
            command (str): The command to process
            args (list): Arguments for the command
        """
        try:
            command = command.upper()
            if command not in self.command_map:
                print(f"Unknown command: {command}")
                print("Use HELP to see available commands")
                return

            # Validate argument count
            if not self._validate_command_args(command, args):
                print(f"Invalid number of arguments for {command}")
                print(f"Usage: {self._get_command_usage(command)}")
                return

            # Validate paths for commands that require them
            if command in ['CREATE', 'DELETE', 'MOVE']:
                for path in args:
                    if not self._validate_path(path):
                        print(f"Invalid path: {path}")
                        return

            # Execute command
            command_function = self.command_map[command]
            command_function(*args)
        except EOFError:
            raise
        except Exception as e:
            print(str(e))

    def run(self) -> None:
        """
        Runs the main loop for the DirectoryManager, handling user input
        and processing commands until the user exits.
        """
        while True:
            try:
                statement = input().strip()
                command, args = self.parse_statement(statement)
                self.process(command, args)
            except (EOFError, KeyboardInterrupt):
                print("Exiting...")
                break
