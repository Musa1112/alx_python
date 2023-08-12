def pow(a, b):
  """Computes a to the power of b and returns the value."""
  if b == 0:
    return 1
  elif b == 1:
    return a
  else:
    return a * pow(a, b - 1)
