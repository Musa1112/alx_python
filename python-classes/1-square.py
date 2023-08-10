class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """Initialize the square with the given size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, new_size):
        """Set the size of the square."""
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        if new_size < 0:
            raise ValueError("size must be >= 0")
        self.__size = new_size

    def area(self):
        """Calculate the area of the square."""
        return self.__size * self.__size
# Documentation for the Square class

    """This class defines a square with a private size attribute. The size attribute cannot be changed directly, but it can be accessed through the size property. The area method calculates and returns the area of the square."""


