from itertools import combinations

names = input().split(", ")
n = int(input())
print('\n'.join([', '.join(combination) for combination in combinations(names, n)]))