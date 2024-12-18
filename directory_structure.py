from exceptions import InvalidPathError, DirectoryNotFoundError, CannotMoveDirectoryError, RootDirectoryError, \
    CannotDeleteDirectoryError, DirectoryAlreadyExistsError


class DirectoryStructure:
    def __init__(self):
        """
        Initializes the directory structure as a nested dictionary.
        """
        self.directory = {}

    def create_directory(self, path: str) -> None:
        """
        Creates a new directory at the specified path.
        If intermediate directories don't exist, they will be created.

        Args:
            path (str): Path where the directory should be created (e.g., 'root/folder1/folder2')

        Raises:
            InvalidPathError: If the path is empty or invalid
            DirectoryAlreadyExistsError: If attempting to create a directory that already exists
        """
        current = self.directory
        path_parts = path.split("/")
        for i, folder in enumerate(path_parts):
            if not folder:
                raise InvalidPathError("Invalid path: empty folder name")
            if i == len(path_parts) - 1 and folder in current:
                raise DirectoryAlreadyExistsError(path)
            if folder not in current:
                current[folder] = {}
            current = current[folder]

    def move_directory(self, source_path: str, dest_path: str) -> None:
        """
        Moves a directory from source path to destination path.

        Args:
            source_path (str): Path of directory to move
            dest_path (str): Destination path for the directory

        Raises:
            CannotMoveDirectoryError: If the source is moved into itself
            DirectoryNotFoundError: If the source path doesn't exist
        """
        if dest_path.startswith(source_path):
            raise CannotMoveDirectoryError(source_path, dest_path)

        source = source_path.split("/")
        dest = dest_path.split("/")

        # Find source and its parent
        current = self.directory
        source_parent = current
        for folder in source[:-1]:
            if folder not in current:
                raise DirectoryNotFoundError(source_path)
            current = current[folder]
            source_parent = current

        if source[-1] not in current:
            raise DirectoryNotFoundError(source[-1])

        source_item = current[source[-1]]

        # Find destination
        current = self.directory
        for folder in dest:
            if folder not in current:
                current[folder] = {}
            current = current[folder]

        # Move the directory
        current[source[-1]] = source_item
        del source_parent[source[-1]]

    def delete_directory(self, path: str) -> None:
        """
        Deletes a directory at the specified path.
        If the directory contains subdirectories, they will also be deleted.

        Args:
            path (str): Path of the directory to delete (e.g., 'root/folder1/folder2')

        Raises:
            RootDirectoryError: If attempting to delete the root directory
            CannotDeleteDirectoryError: If the specified path doesn't exist
        """
        path_parts = path.split("/")
        if not path:
            raise RootDirectoryError()

        current = self.directory
        for folder in path_parts[:-1]:
            if folder not in current:
                raise CannotDeleteDirectoryError(path, folder)
            current = current[folder]

        del current[path_parts[-1]]

    def print_directory(self, directory=None, indent: int = 0) -> None:
        """
        Recursively prints the contents of a directory with proper indentation.

        Args:
            directory (dict): The directory structure to print
            indent (int, optional): The current indentation level. Defaults to 0.
        """
        if directory is None:
            directory = self.directory
        for name, contents in sorted(directory.items()):
            print("  " * indent + name)
            self.print_directory(contents, indent + 1)
