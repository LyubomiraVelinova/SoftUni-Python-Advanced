from itertools import chain

rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for i in range(rows)]

best_sum = -999999
best_matrix = []
squares = []
for row in range(rows - 2):
    for col in range(cols - 2):
        sub_matrix = []
        current_sum = 0
        row_counter = 0
        for r in range(row, row + 3):
            sub_matrix.append([])
            for c in range(col, col + 3):
                sub_matrix[row_counter].append(matrix[r][c])
                current_sum += matrix[r][c]
            row_counter += 1

        if current_sum > best_sum:
            best_sum = current_sum
            best_matrix = sub_matrix
print(f"Sum = {best_sum}")
for row in best_matrix:
    print(" ".join([str(x) for x in row]))