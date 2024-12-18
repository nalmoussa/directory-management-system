from directory_manager import DirectoryManager

def main():
    """
    Entry point for the program. Creates a DirectoryManager instance
    and starts the command processing loop.
    """
    manager = DirectoryManager()
    manager.run()


if __name__ == "__main__":
    main()
