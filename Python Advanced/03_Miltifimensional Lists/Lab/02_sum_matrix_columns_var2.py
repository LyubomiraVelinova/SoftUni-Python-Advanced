rows, cols = [int(n) for n in input().split(", ")]
matrix = [[int(n) for n in input().split()] for _ in range(rows)]

for col in zip(*matrix):
    print(sum(col))