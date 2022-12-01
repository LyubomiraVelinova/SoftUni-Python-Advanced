n = int(input())
guests = set()
attended = set()

for _ in range(n):
    num = input()
    guests.add(num)

while True:
    command = input()
    if command == "END":
        break
    attended.add(command)

unattended = guests - attended
print(len(unattended))
print("\n".join(sorted(unattended)))