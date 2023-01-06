def bomb_explodes(matrix, row, column):
    damage = matrix[row][column]
    # matrix[row][column - 1] -= damage
    # matrix[row][column] -= damage
    # matrix[row][column + 1] -= damage
    # matrix[row - 1][column] -= damage
    # matrix[row + 1][column] -= damage
    # matrix[row - 1][column - 1] -= damage
    # matrix[row - 1][column + 1] -= damage
    # matrix[row + 1][column + 1] -= damage
    # matrix[row + 1][column - 1] -= damage
    for i in range(row - 1, row + 2):
        if i < 0:
            i = 0
        elif i > len(matrix):
            i = len(matrix)
        for j in range(column - 1, column + 2):
            if j < 0:
                j = 0
            elif j > len(matrix):
                j = len(matrix)
            if matrix[i][j] > 0:
                matrix[i][j] -= damage
    return matrix


def find_alive_cells(matrix):
    counter = 0
    sum_of_cells = 0
    for row in matrix:
        for num in row:
            if num > 0:
                counter += 1
                sum_of_cells += num
    return counter, sum_of_cells


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
bomb_matrix = [list(map(int, sell.split(","))) for sell in input().split()]
for row, column in bomb_matrix:
    matrix = bomb_explodes(matrix, row, column)

alive_cells, alive_cells_sum = find_alive_cells(matrix)
print(f"Alive cells: {alive_cells}")
print(f"Sum: {alive_cells_sum}")
print('\n'.join([' '.join(map(str, row)) for row in matrix]))
