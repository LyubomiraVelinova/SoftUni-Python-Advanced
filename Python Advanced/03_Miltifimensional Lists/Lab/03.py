num = int(input())
matrix = [list(map(int, input().split())) for _ in range(num)]
primary_diagonal_sum = sum([matrix[i][i] for i in range(num)])

# primary_diagonal_sum = 0
# for i in range(num):
#     primary_diagonal_sum += matrix[i][i]

print(primary_diagonal_sum)