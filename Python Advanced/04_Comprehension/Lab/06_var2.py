rows, cols = [int(x) for x in input().split()]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
nested_matrix = []
matrix = []

for i in range(rows):
    for j in range(cols):
        first_last_letter = letters[i]
        middle_letter = letters[i + j]

        string = first_last_letter + middle_letter + first_last_letter

        if string == string[::-1]:
            nested_matrix.append(string)
    matrix.append(nested_matrix)
    nested_matrix = []

for row in matrix:
    print(" ".join(row))