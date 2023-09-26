class BaseGeometry:
    def area(self):
        raise NotImplementedError("area() method not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

# Example usage
if __name__ == "__main__":
    rectangle = Rectangle(5, 4)
    print(rectangle.area())  # Output: 20
    print(rectangle)         # Output: [Rectangle] 5/4

    # Testing invalid width and height
    try:
        invalid_rect = Rectangle("invalid", -1)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
