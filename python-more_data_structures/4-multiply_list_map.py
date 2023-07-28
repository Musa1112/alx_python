def multiply_list_map(my_list=[], number=0):
  """
  Returns a list with all values multiplied by a number.

  Args:
    my_list: The list to be multiplied.
    number: The number to multiply the list by.

  Returns:
    A new list with all values multiplied by number.
  """

  multiplied_list = map(lambda x: x * number, my_list)

  return list(multiplied_list)
