num = int(input())
matrix = [[int(n) for n in input().split()] for i in range(num)]

primary_diagonal = 0
secondary_diagonal = 0
counter = 0
for i in range(num):
    counter += 1
    primary_diagonal += matrix[i][i]
    secondary_diagonal += matrix[i][num-counter]

print(abs(primary_diagonal - secondary_diagonal))
