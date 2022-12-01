rows, cols = [int(el) for el in input().split(", ")]
matrix = []
total = 0

for _ in range(rows):
    row = [int(number) for number in input().split(", ")]
    matrix.append(row)
    total += sum(row)

print(total)
print(matrix)
