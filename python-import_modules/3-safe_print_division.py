def safe_print_division(a, b):
  """Safely prints the division of a and b."""
  try:
    result = a / b
    print("Inside result: {}".format(result))
    return result
  except ZeroDivisionError:
    return None

if __name__ == "__main__":
  result = safe_print_division(10, 2)
  print(result)
