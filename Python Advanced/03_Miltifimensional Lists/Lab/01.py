# rows, columns = list(map(int, input().split(", ")))

import itertools

rows, cols = [int(el) for el in input().split(", ")]
matrix = [[int(number) for number in input().split(", ")] for _ in range(rows)]
total = sum(itertools.chain(*matrix))
# total = sum([sum(row) for row in matrix])

print(total)
print(matrix)

