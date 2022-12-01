rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for i in range(rows)]

counter = 0

squares = []
length = len(matrix)
for i in range(len(matrix) - 1):
    row = matrix[i]
    for j in range(len(row) - 1):
        if rows - 1 > 0 and cols - 1 > 0:
            first = matrix[i][j]
            second = matrix[i][j + 1]
            third = matrix[i + 1][j]
            forth = matrix[i + 1][j + 1]
            if [matrix[i][j], matrix[i][j + 1]] == [matrix[i + 1][j], matrix[i + 1][j + 1]]:
                counter += 1

print(counter)
