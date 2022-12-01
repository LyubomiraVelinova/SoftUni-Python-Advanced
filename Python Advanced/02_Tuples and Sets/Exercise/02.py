# count = input().split()
# count_n = int(count[0])
# count_m = int(count[1])

count_n, count_m = tuple(int(x) for x in input().split())

set_n = set()
set_m = set()

for _ in range(count_n):
    set_n.add(input())

for _ in range(count_m):
    set_m.add(input())

unique = set_m & set_n
for i in unique:
    print(i)
