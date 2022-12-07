from string import ascii_lowercase

rows, cols = [int(x) for x in input().split()]

def create_cell(i, j):
    first_last_char = ascii_lowercase[i]
    middle_char = ascii_lowercase[i + j]
    cell = first_last_char + middle_char + first_last_char
    if cell == cell[::-1]:
        return cell


matrix = [[create_cell(i,j) for j in range(cols)] for i in range(rows)]

for row in matrix:
    print(" ".join(row))
