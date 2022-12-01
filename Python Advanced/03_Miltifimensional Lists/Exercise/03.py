from itertools import chain


def read_matrix():
    rows, cols = [int(x) for x in input().split()]
    matrix = [[int(x) for x in input().split()] for i in range(rows)]
    return matrix


counter = 0


def get_squares(matrix):
    squares = []
    for i in range(len(matrix) - 2):
        row = matrix[i]
        for j in range(len(row) - 2):
            a = matrix[i][j]
            b = matrix[i][j + 1]
            c = matrix[i][j + 2]
            d = matrix[i + 1][j]
            e = matrix[i + 1][j + 1]
            f = matrix[i + 1][j + 2]
            g = matrix[i + 2][j]
            h = matrix[i + 2][j + 1]
            k = matrix[i + 2][j + 2]
            square = [
                [a, b, c],
                [d, e, f],
                [g, h, i]
            ]
            squares.append(square)
        return squares


def get_sum_of_matrix(matrix):
    return sum(chain(*matrix))


def get_max_square(squares):
    max_sum = None
    max_square = None
    for square in squares:
        square_sum = get_sum_of_matrix(square)
        if max_sum is None or square_sum > max_sum:
            max_sum = square_sum
            max_square = square
    return max_square


matrix = read_matrix()
squares = get_squares(matrix)
max_sum = get_sum_of_matrix(matrix)
max_square = get_max_square(squares)

print(f"Sum = {max_sum}")
print({get_max_square(squares)})
