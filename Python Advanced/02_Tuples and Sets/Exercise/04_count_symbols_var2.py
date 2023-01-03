command = input()
chars = set()

for ch in command:
    chars.add(ch)

print(sorted(chars))

# for char, time in chars.items():
#     print(f"{char}: {time} time/s")

