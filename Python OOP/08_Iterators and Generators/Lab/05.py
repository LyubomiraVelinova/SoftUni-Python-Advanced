# def genrange(start, end):
#     for i in range(start, end + 1):
#         yield i


genrange = lambda start, end: (i for i in range(start, end + 1))
print(list(genrange(1, 10)))
