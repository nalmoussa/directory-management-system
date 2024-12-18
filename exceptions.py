class InvalidPathError(Exception):
  """
  Raised when a given path is invalid.

  Attributes:
      message (str): Explanation of the error.
  """
  def __init__(self, message="Invalid path provided"):
    self.message = message
    super().__init__(self.message)


class DirectoryNotFoundError(Exception):
  """
  Raised when the specified directory is not found.

  Attributes:
      path (str): The path that was not found.
      message (str): Explanation of the error.
  """

  def __init__(self, path, message="Directory not found"):
    self.path = path
    self.message = f"{message}: {path}"
    super().__init__(self.message)


class CannotDeleteDirectoryError(Exception):
  """
  Raised when the specified directory can not be deleted.

  Attributes:
      path (str): The path of the directory.
      folder (str): the non-existing folder.
  """
  def __init__(self, path: str, folder: str):
    self.path = path
    self.folder = folder
    self.message = f"Cannot delete {path} - {folder} does not exist"
    super().__init__(self.message)


class CannotMoveDirectoryError(Exception):
  """
  Raised when attempting to move a directory in an invalid way (e.g., into itself).

  Attributes:
      source_path (str): The source path of the directory.
      dest_path (str): The destination path for the directory.
      message (str): Explanation of the error.
  """
  def __init__(self, source_path, dest_path, message="Cannot move directory"):
    self.source_path = source_path
    self.dest_path = dest_path
    self.message = f"{message}: {source_path} to {dest_path}"
    super().__init__(self.message)


class DirectoryAlreadyExistsError(Exception):
  """
  Raised when attempting to create a directory that already exists.

  Attributes:
      path (str): The path that already exists.
      message (str): Explanation of the error.
  """
  def __init__(self, path, message="Directory already exists"):
    self.path = path
    self.message = f"{message}: {path}"
    super().__init__(self.message)


class RootDirectoryError(Exception):
  """
  Raised when an operation is attempted on the root directory that is not allowed.

  Attributes:
      message (str): Explanation of the error.
  """
  def __init__(self, message="Operation not allowed on the root directory"):
    self.message = message
    super().__init__(self.message)


class EmptyStatementError(Exception):
  """
  Raised when attempting to parse an empty statement

  Attributes:
      message (str): Explanation of the error.
  """
  def __init__(self, message="Empty statement"):
    self.message = message
    super().__init__(self.message)
