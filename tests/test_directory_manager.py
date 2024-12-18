import unittest
from unittest.mock import MagicMock, patch
from directory_manager import DirectoryManager
from exceptions import EmptyStatementError

class TestDirectoryManager(unittest.TestCase):
    def setUp(self):
        """Set up a fresh instance of DirectoryManager for each test."""
        self.manager = DirectoryManager()
        self.manager.command_map["CREATE"] = MagicMock()
        self.manager.command_map["MOVE"] = MagicMock()
        self.manager.command_map["DELETE"] = MagicMock()
        self.manager.command_map["LIST"] = MagicMock()

    def test_print_help(self):
        """Test that help is printed for all commands."""
        with patch("builtins.print") as mock_print:
            self.manager.print_help()
            mock_print.assert_any_call("Available commands:")

    def test_print_help_specific_command(self):
        """Test that specific help is printed for a command."""
        with patch("builtins.print") as mock_print:
            self.manager.print_help("CREATE")
            mock_print.assert_called_once()

    def test_exit_program(self):
        """Test that the exit_program method raises EOFError."""
        with self.assertRaises(EOFError):
            self.manager.exit_program()

    def test_validate_command_args(self):
        """Test the validation of command arguments."""
        self.assertTrue(self.manager._validate_command_args("CREATE", ["path"]))
        self.assertFalse(self.manager._validate_command_args("CREATE", []))
        self.assertTrue(self.manager._validate_command_args("HELP", []))
        self.assertTrue(self.manager._validate_command_args("HELP", ["COMMAND"]))

    def test_normalize_path(self):
        """Test normalization of paths."""
        self.assertEqual(self.manager.normalize_path("/root/folder/"), "root/folder")
        self.assertEqual(self.manager.normalize_path("root//folder"), "root/folder")

    def test_validate_path(self):
        """Test validation of paths."""
        self.assertTrue(self.manager._validate_path("root/folder"))
        self.assertFalse(self.manager._validate_path(""))
        self.assertFalse(self.manager._validate_path("root/folder|invalid"))

    def test_get_command_usage(self):
        """Test retrieval of command usage strings."""
        self.assertEqual(self.manager._get_command_usage("CREATE"), "CREATE <path>")
        self.assertEqual(self.manager._get_command_usage("UNKNOWN"), "")

    def test_parse_statement_valid(self):
        """Test parsing a valid statement."""
        command, args = self.manager.parse_statement("CREATE root/folder")
        self.assertEqual(command, "CREATE")
        self.assertEqual(args, ["root/folder"])

    def test_parse_statement_empty(self):
        """Test parsing an empty statement."""
        with self.assertRaises(EmptyStatementError):
            self.manager.parse_statement("")

    def test_process_valid_command(self):
        """Test processing a valid command."""
        self.manager.process("CREATE", ["root/folder"])
        self.manager.command_map["CREATE"].assert_called_with("root/folder")

    def test_process_invalid_command(self):
        """Test processing an invalid command."""
        with patch("builtins.print") as mock_print:
            self.manager.process("INVALID", [])
            mock_print.assert_any_call("Unknown command: INVALID")

    def test_process_invalid_args(self):
        """Test processing a command with invalid arguments."""
        with patch("builtins.print") as mock_print:
            self.manager.process("CREATE", [])
            mock_print.assert_any_call("Invalid number of arguments for CREATE")

    def test_run_exit(self):
        """Test running the manager and exiting."""
        with patch("builtins.input", side_effect=[KeyboardInterrupt]):
            with patch("builtins.print") as mock_print:
                self.manager.run()
                mock_print.assert_any_call("Exiting...")
