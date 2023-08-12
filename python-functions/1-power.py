def pow(a, b):
  """Computes a to the power of b and returns the value."""
  if b < 0:
    return 1 / pow(a, -b)
  elif b == 0:
    return 1
  elif b == 1:
    return a
  else:
    return a * pow(a, b - 1)

if __name__ == "__main__":
  print(pow(10, -2))
