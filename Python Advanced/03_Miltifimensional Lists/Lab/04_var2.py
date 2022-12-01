def find_in_matrix(matrix, symbol):
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == symbol:
                return i, j


n = int(input())
matrix = [list(input()) for _ in range(n)]
symbol = input()

pos = find_in_matrix(matrix, symbol)

if pos:
    print(pos)
else:
    print(f"{symbol} does not occur in the matrix")