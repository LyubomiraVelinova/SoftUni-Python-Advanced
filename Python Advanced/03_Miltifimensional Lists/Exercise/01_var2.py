num = int(input())
matrix = [[int(n) for n in input().split()] for i in range(num)]

primary_diagonal = 0
secondary_diagonal = 0

for i in range(num):
    for j in range(num):
        if i == j:
            primary_diagonal += matrix[i][j]
        if num - 1 - i == j:
            secondary_diagonal += matrix[i][j]

print(abs(primary_diagonal - secondary_diagonal))
