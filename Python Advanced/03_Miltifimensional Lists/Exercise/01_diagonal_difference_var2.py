N = int(input())
matrix = [[int(num) for num in input().split(" ")] for _ in range(N)]
primary_diagonal_sum = sum([matrix[i][i] for i in range(N)])
secondary_diagonal_sum = sum([matrix[j][N - j - 1] for j in range(N)])
print(abs(primary_diagonal_sum - secondary_diagonal_sum))
