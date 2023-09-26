def is_kind_of_class(obj, a_class):
  """Returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise False.

  Args:
    obj: The object to check.
    a_class: The class to check against.

  Returns:
    True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise False.
  """

  return isinstance(obj, a_class) or issubclass(obj.__class__, a_class)

class MyClass:
  pass

class SubclassOfMyClass(MyClass):
  pass

obj = MyClass()

if is_kind_of_class(obj, MyClass):
  print("The object is an instance of MyClass.")
else:
  print("The object is not an instance of MyClass.")
