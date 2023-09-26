class BaseGeometry:
  """An empty base class for geometry objects."""

  def area(self):
    raise Exception("area() is not implemented")

  def integer_validator(self, name, value):
    """Validates the value of a given attribute.

    Args:
      name: The name of the attribute.
      value: The value of the attribute.

    Raises:
      TypeError: If the value is not an integer.
      ValueError: If the value is less than or equal to 0.
    """

    if not isinstance(value, int):
      raise TypeError(f"{name} must be an integer")
    if value <= 0:
      raise ValueError(f"{name} must be greater than 0")

class Rectangle:
  """A rectangle.

  Args:
    width: The width of the rectangle.
    height: The height of the rectangle.
  """

  def __init__(self, width, height):
    """Initializes a new rectangle.

    Args:
      width: The width of the rectangle.
      height: The height of the rectangle.
    """

    self._width = width
    self._height = height

    self.integer_validator("width", self._width)
    self.integer_validator("height", self._height)

  def area(self):
    """Calculates the area of the rectangle.

    Returns:
      The area of the rectangle.
    """

    return self._width * self._height

  def __str__(self):
    """Returns a string representation of the rectangle.

    Returns:
      A string representation of the rectangle.
    """

    return f"[Rectangle] {self._width}/{self._height}"

class Square(Rectangle):
  """A square.

  Args:
    size: The size of the square.
  """

  def __init__(self, size):
    """Initializes a new square.

    Args:
      size: The size of the square.
    """

    super().__init__(size, size)

