rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for i in range(rows)]

counter = 0
for i in range(rows):
    for j in range(cols):
        if rows - 1 >= 0 and cols - 1 >= 0:

            if matrix[i][j] == matrix[i][j - 1] and \
                    matrix[i][j] == matrix[i - 1][j] and \
                    matrix[i][j] == matrix[i - 1][j - 1]:
                counter += 1

print(counter)
