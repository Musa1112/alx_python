class BaseGeometry:
  """An empty base class for geometry objects."""

  def area(self):
    raise Exception("area() is not implemented")

class Rectangle(BaseGeometry):
  """A rectangle."""

  def __init__(self, length, width):
    self.length = length
    self.width = width

  def area(self):
    return self.length * self.width

rectangle = Rectangle(10, 5)

print(rectangle.area())
# 50
