n = int(input())
matrix = [input() for _ in range(n)]
symbol = input()

is_occur = False
rows_counter = 0
for row in matrix:
    cols_counter = 0
    for ch in row:
        if ch == symbol:
            is_occur = True
            print(f"({rows_counter}, {cols_counter})")
            break
        cols_counter += 1
    rows_counter += 1

if not is_occur:
    print(f"{symbol} does not occur in the matrix")