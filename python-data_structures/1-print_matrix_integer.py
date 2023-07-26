def print_matrix_integer(matrix=[[]]):
  """Prints a matrix of integers."""
  if not matrix:
    print("Empty matrix")
    return

  for row in matrix:
    print(" ".join([str.format("{0:d}", i) for i in row]))

if __name__ == "__main__":
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  print_matrix_integer(matrix)
