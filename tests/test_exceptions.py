import unittest
from exceptions import (
    InvalidPathError,
    DirectoryNotFoundError,
    CannotDeleteDirectoryError,
    CannotMoveDirectoryError,
    DirectoryAlreadyExistsError,
    RootDirectoryError,
    EmptyStatementError,
)


class TestExceptions(unittest.TestCase):
    def test_invalid_path_error(self):
        """Test InvalidPathError with default and custom message."""
        default_error = InvalidPathError()
        self.assertEqual(str(default_error), "Invalid path provided")

        custom_error = InvalidPathError("Custom message")
        self.assertEqual(str(custom_error), "Custom message")

    def test_directory_not_found_error(self):
        """Test DirectoryNotFoundError with a path."""
        error = DirectoryNotFoundError("/invalid/path")
        self.assertEqual(str(error), "Directory not found: /invalid/path")
        self.assertEqual(error.path, "/invalid/path")

    def test_cannot_delete_directory_error(self):
        """Test CannotDeleteDirectoryError with path and folder."""
        error = CannotDeleteDirectoryError("/path/to/dir", "missing_folder")
        self.assertEqual(
            str(error), "Cannot delete /path/to/dir - missing_folder does not exist"
        )
        self.assertEqual(error.path, "/path/to/dir")
        self.assertEqual(error.folder, "missing_folder")

    def test_cannot_move_directory_error(self):
        """Test CannotMoveDirectoryError with source and destination paths."""
        error = CannotMoveDirectoryError("/source/path", "/destination/path")
        self.assertEqual(
            str(error), "Cannot move directory: /source/path to /destination/path"
        )
        self.assertEqual(error.source_path, "/source/path")
        self.assertEqual(error.dest_path, "/destination/path")

    def test_directory_already_exists_error(self):
        """Test DirectoryAlreadyExistsError with a path."""
        error = DirectoryAlreadyExistsError("/existing/path")
        self.assertEqual(str(error), "Directory already exists: /existing/path")
        self.assertEqual(error.path, "/existing/path")

    def test_root_directory_error(self):
        """Test RootDirectoryError with default and custom message."""
        default_error = RootDirectoryError()
        self.assertEqual(
            str(default_error), "Operation not allowed on the root directory"
        )

        custom_error = RootDirectoryError("Custom root directory error")
        self.assertEqual(str(custom_error), "Custom root directory error")

    def test_empty_statement_error(self):
        """Test EmptyStatementError with default and custom message."""
        default_error = EmptyStatementError()
        self.assertEqual(str(default_error), "Empty statement")

        custom_error = EmptyStatementError("Custom empty statement error")
        self.assertEqual(str(custom_error), "Custom empty statement error")
