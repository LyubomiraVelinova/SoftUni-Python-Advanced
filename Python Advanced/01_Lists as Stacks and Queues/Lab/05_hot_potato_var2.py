from collections import deque

children = deque(input().split())
n = int(input())
while len(children) > 1:
    children.rotate(-n)
    loser = children.pop()
    print(f"Removed {loser}")

winner = children.pop()
print(f"Last is {winner}")

