class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """Initialize the square with the given size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square."""
        return self.__size * self.__size

