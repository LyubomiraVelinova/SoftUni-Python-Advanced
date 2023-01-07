# r, c = [int(num) for num in input().split()]
# matrix = []
# word = ""
# for row in range(r):
#     matrix_row = []
#     for col in range(c):
#         first_last_l = chr(row + 97)
#         middle_l = chr(col + row + 97)
#         word = first_last_l + middle_l + first_last_l
#         matrix_row.append(word)
#     matrix.append(matrix_row)
# print('\n'.join([' '.join(char for char in row) for row in matrix]))

r, c = [int(num) for num in input().split()]
matrix = [[chr(row + 97)+chr(col + row + 97)+chr(row + 97) for col in range(c)] for row in range(r)]
print('\n'.join([' '.join(char for char in row) for row in matrix]))
