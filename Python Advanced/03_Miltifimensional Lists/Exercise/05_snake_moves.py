N, M = [int(num) for num in input().split()]
matrix = [[""] * M] * N
text = input()
index = 0
counter = 0
for row in matrix:
    for j in range(M):
        if counter % 2 == 0:
            row[j] = text[index]
        else:
            row[M - j - 1] = text[index]
        index += 1
        if index == len(text):
            index = 0
    counter += 1
    print(''.join([char for char in row]))

#
# for i in range(N):
#     for j in range(M):
#         if i % 2 == 0:
#             matrix[i][j] = text[index]
#         else:
#             matrix[i][M - j - 1] = text[index]
#         index += 1
#         if index == len(text):
#             print([''.join(map(str, row)) for row in matrix])
#             index = 0

