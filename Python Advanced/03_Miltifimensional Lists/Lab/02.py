rows, cols = [int(n) for n in input().split(", ")]

matrix = []

for _ in range(rows):
    matrix.append(list(map(int, input().split())))

for j in range(cols):
    sum_matrix_el = 0
    # for row in matrix:
    #     sum_matrix_el += row[j]
    for i in range(rows):
        sum_matrix_el += matrix[i][j]
    print(sum_matrix_el)