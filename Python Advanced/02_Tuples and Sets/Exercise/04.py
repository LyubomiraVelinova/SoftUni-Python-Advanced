from _collections import defaultdict

command = input()
chars = defaultdict(int)

for ch in command:
    chars[ch] += 1

for char, time in sorted(chars.items()):
    print(f"{char}: {time} time/s")

