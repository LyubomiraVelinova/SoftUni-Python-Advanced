def read_matrix():
    N = int(input())
    matrix = [[int(num) for num in input().split(" ")] for _ in range(N)]
    return matrix


def find_primary_diagonal_sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    return sum


def find_secondary_diagonal_sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][len(matrix) - i - 1]
    return sum


def find_absolute_difference(a, b):
    return abs(a - b)


matrix = read_matrix()
primary_diagonal_sum = find_primary_diagonal_sum(matrix)
secondary_diagonal_sum = find_secondary_diagonal_sum(matrix)
print(find_absolute_difference(primary_diagonal_sum, secondary_diagonal_sum))
