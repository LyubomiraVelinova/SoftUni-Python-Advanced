def read_matrix():
    rows, cols = [int(num) for num in input().split()]
    matrix = [input().split() for _ in range(rows)]
    return matrix, rows, cols


def get_squares(matrix, rows, cols):
    all_square_matrix = []
    for row in range(rows - 1):
        for col in range(cols - 1):
            square_matrix = [
                [matrix[row][col], matrix[row][col + 1]],
                [matrix[row + 1][col], matrix[row + 1][col + 1]]
                 ]
            all_square_matrix.append(square_matrix)
    return all_square_matrix


def get_squares_of_equal_char(matrix):
    equals = []
    for square_matrix in matrix:
        if square_matrix[0] == square_matrix[1]:
            equals.append(square_matrix)
    return len(equals)


matrix, rows, cols = read_matrix()
square_matrix = get_squares(matrix, rows, cols)
print(get_squares_of_equal_char(square_matrix))