def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print("{:d}".format(col), end=" ")
        print()
if __name__ == "__main__":
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  print_matrix_integer(matrix)