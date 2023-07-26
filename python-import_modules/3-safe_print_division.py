def safe_print_division(x, y):
  """Safely prints the division of x and y."""
  try:
    result = x / y
    print(f"{x} / {y} = {result}")
  except ZeroDivisionError:
    print(f"Cannot divide {x} by 0")

if __name__ == "__main__":
  safe_print_division(10, 2)
  safe_print_division(10, 0)
