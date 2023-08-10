class Square:
    """A class that defines a square."""

    def __init__(self, size):
        """Initialize the square with the given size."""
        self.__size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, new_size):
        """Set the size of the square."""
        if new_size <= 0:
            raise ValueError("Size must be positive")
        self.__size = new_size

    def area(self):
        """Calculate the area of the square."""
        return self.__size * self.__size

