string = input().split("|")
matrix = [ch for row in string[::-1] for ch in row if not ch.isspace()]

print(" ".join(matrix))