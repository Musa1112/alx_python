def safe_print_division(x, y):
  """Safely prints the division of x and y."""
  try:
    result = x / y
    print("{} / {} = {}".format(x, y, result))
  except ZeroDivisionError:
    print("Cannot divide {} by 0".format(x))
  finally:
    print("This code is always executed.")

if __name__ == "__main__":
  safe_print_division(10, 2)
  safe_print_division(10, 0)
