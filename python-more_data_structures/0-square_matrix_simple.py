def square_matrix_simple(matrix=[]):
    return [[num ** 2 for num in row] for row in matrix]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = square_matrix_simple(matrix)
print(result)
