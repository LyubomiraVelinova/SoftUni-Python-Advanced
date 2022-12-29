children = input().split()
n = int(input())

count = 0
index = -1
while len(children) > 1:
    count += 1
    index += 1
    if index == len(children):
        index = 0
    if count == n:
        print(f"Removed {children[index]}")
        children.pop(index)
        count = 0
        index -= 1

print(f"Last is {''.join(children)}")

