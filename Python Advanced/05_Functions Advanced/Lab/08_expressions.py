from itertools import permutations
from itertools import chain

nums = input().split(", ")
n = len(nums)
permutations = set(permutations(["+"] * n + ["-"] * n, n))
for permutation in permutations:
    expr = ''.join(list(chain(*zip(permutation, nums))))
    res = eval(expr)
    print(f"{expr}={res}")
# print('\n'.join([', '.join(combination) for combination in combinations(nums, len(nums))]))

