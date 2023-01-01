from _collections import deque

cups = deque(int(num) for num in input().split())
bottles = [int(num) for num in input().split()]

wasted_water = 0

while len(cups) > 0 and len(bottles) > 0:
    cup = cups[0]
    bottle = bottles[-1]
    if bottle >= cup:
        wasted_water += bottle - cup
        bottles.pop()
        cups.popleft()
    elif cup > bottle:
        while bottles[-1] <= cups[0]:
            cups[0] -= bottles[-1]
            bottles.pop()
            if cups[0] == 0:
                cups.popleft()
            if len(bottles) == 0:
                break

if len(cups) == 0:
    print(f"Bottles: {' '.join(str(i) for i in bottles[::-1])}")
else:
    print(f"Cups: {' '.join(str(i) for i in cups)}")
print(f"Wasted litters of water: {wasted_water}")