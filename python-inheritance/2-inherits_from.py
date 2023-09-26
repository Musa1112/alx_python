def inherits_from(obj, a_class):
  """Returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False.

  Args:
    obj: The object to check.
    a_class: The class to check against.

  Returns:
    True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False.
  """

  if isinstance(obj, a_class):
    return True

  for parent in obj.__class__.__bases__:
    if inherits_from(parent, a_class):
      return True

  return False
