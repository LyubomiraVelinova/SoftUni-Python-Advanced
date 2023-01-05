def read_matrix():
    N, M = [int(num) for num in input().split()]
    matrix = [list(map(int, input().split())) for i in range(N)]
    return matrix, N, M


def find_square(matrix, N, M):
    squares = []
    for i in range(N - 2):
        for j in range(M - 2):
            square = [
                matrix[i][j:j + 3],
                matrix[i + 1][j:j + 3],
                matrix[i + 2][j:j + 3],
            ]
            squares.append(square)
    return squares


def take_elements_sum(matrix):
    maximal_sum = 0
    maximal_matrix = None
    for every_matrix in matrix:
        sum_matrix_elements = sum([sum(row) for row in every_matrix])
        if sum_matrix_elements > maximal_sum:
            maximal_sum = sum_matrix_elements
            maximal_matrix = every_matrix
    return maximal_matrix, maximal_sum


matrix, N, M = read_matrix()
squares = find_square(matrix, N, M)
maximal_matrix, maximal_sum = take_elements_sum(squares)
print(f"Sum = {maximal_sum}")
# for row in maximal_matrix:
#     for el in row:
#         print(el, end=" ")
#     print("")
print('\n'.join([' '.join(map(str, row)) for row in maximal_matrix]))
