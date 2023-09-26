def is_same_class(obj, a_class):
  """Returns True if the object is exactly an instance of the specified class; otherwise False.

  Args:
    obj: The object to check.
    a_class: The class to check against.

  Returns:
    True if the object is exactly an instance of the specified class; otherwise False.
  """

  return obj.__class__ == a_class

class MyClass:
  pass

obj = MyClass()

if is_same_class(obj, MyClass):
  print("True.")
else:
  print("False.")
