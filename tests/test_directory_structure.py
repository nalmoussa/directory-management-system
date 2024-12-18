import unittest
from directory_structure import DirectoryStructure
from exceptions import InvalidPathError, DirectoryNotFoundError, CannotMoveDirectoryError, RootDirectoryError, CannotDeleteDirectoryError, DirectoryAlreadyExistsError


class TestDirectoryStructure(unittest.TestCase):
    def setUp(self):
        """Set up a fresh instance of DirectoryStructure for each test."""
        self.ds = DirectoryStructure()

    def test_create_directory_success(self):
        """Test creating a new directory successfully."""
        self.ds.create_directory("root/folder1/folder2")
        self.assertIn("root", self.ds.directory)
        self.assertIn("folder1", self.ds.directory["root"])
        self.assertIn("folder2", self.ds.directory["root"]["folder1"])

    def test_create_directory_invalid_path(self):
        """Test creating a directory with an invalid path."""
        with self.assertRaises(InvalidPathError):
            self.ds.create_directory("root//folder1")

    def test_create_directory_already_exists(self):
        """Test creating a directory that already exists."""
        self.ds.create_directory("root/folder1")
        with self.assertRaises(DirectoryAlreadyExistsError):
            self.ds.create_directory("root/folder1")

    def test_move_directory_success(self):
        """Test moving a directory successfully."""
        self.ds.create_directory("root/source/folder")
        self.ds.create_directory("root/destination")
        self.ds.move_directory("root/source/folder", "root/destination")
        self.assertIn("folder", self.ds.directory["root"]["destination"])
        self.assertNotIn("folder", self.ds.directory["root"]["source"])

    def test_move_directory_not_found(self):
        """Test moving a directory that doesn't exist."""
        with self.assertRaises(DirectoryNotFoundError):
            self.ds.move_directory("root/source/folder", "root/destination")

    def test_move_directory_into_itself(self):
        """Test moving a directory into itself."""
        self.ds.create_directory("root/source/folder")
        with self.assertRaises(CannotMoveDirectoryError):
            self.ds.move_directory("root/source", "root/source/folder")

    def test_delete_directory_success(self):
        """Test deleting a directory successfully."""
        self.ds.create_directory("root/folder1/folder2")
        self.ds.delete_directory("root/folder1/folder2")
        self.assertNotIn("folder2", self.ds.directory["root"]["folder1"])

    def test_delete_directory_not_found(self):
        """Test deleting a directory that doesn't exist."""
        with self.assertRaises(CannotDeleteDirectoryError):
            self.ds.delete_directory("root/folder1/folder2")

    def test_delete_root_directory(self):
        """Test attempting to delete the root directory."""
        with self.assertRaises(RootDirectoryError):
            self.ds.delete_directory("")

    def test_print_directory(self):
        """Test printing the directory structure."""
        self.ds.create_directory("root/folder1/folder2")
        self.ds.create_directory("root/folder3")
        # Use captured output to validate the printed structure
        import io
        from contextlib import redirect_stdout
        output = io.StringIO()
        with redirect_stdout(output):
            self.ds.print_directory()
        printed_output = output.getvalue()
        expected_output = """root
  folder1
    folder2
  folder3
"""
        self.assertEqual(printed_output.strip(), expected_output.strip())
