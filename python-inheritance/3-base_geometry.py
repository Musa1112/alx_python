class BaseGeometry:
  """An empty base class for geometry objects."""
  pass

class Rectangle(BaseGeometry):
  """A rectangle."""

  def __init__(self, length, width):
    self.length = length
    self.width = width

  def area(self):
    return self.length * self.width

  def perimeter(self):
    return 2 * (self.length + self.width)

rectangle = Rectangle(10, 5)

print(rectangle.area())
# 50

print(rectangle.perimeter())
# 30
