from collections import deque

people = deque()
water_qty = int(input())
while True:
    name = input()
    if name == "Start":
        break
    people.append(name)

while True:
    command = input()
    if command == "End":
        break
    elif "refill" in command:
        liters = int(command.split()[1])
        water_qty += liters
    else:
        liters = int(command)
        if liters <= water_qty:
            water_qty -= liters
            print(f"{people.popleft()} got water")
        else:
            print(f"{people.popleft()} must wait")

print(f"{water_qty} liters left")