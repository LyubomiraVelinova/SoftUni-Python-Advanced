# import itertools
#
# matrix = [
#     [1,2],
#     [4,5]
# ]
#
# chained = sum(itertools.chain(*matrix))
# print(chained)


rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for i in range(rows)]

for i in range(rows):
    for j in range(cols):
        matrix_m = matrix[i][j], matrix[i][i + 1]

