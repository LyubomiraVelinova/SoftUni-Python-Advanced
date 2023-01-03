from math import floor

N = int(input())
names = [input() for _ in range(N)]
odd_numbers = set()
even_numbers = set()
for line in range(1, len(names) + 1):
    ascii_value = 0
    for letter in names[line - 1]:
        ascii_value += ord(letter)
    ascii_value = floor(ascii_value / line)
    if ascii_value % 2 == 0:
        even_numbers.add(ascii_value)
    else:
        odd_numbers.add(ascii_value)

if sum(odd_numbers) == sum(even_numbers):
    union_values = odd_numbers | even_numbers
    print(", ".join(map(str, union_values)))
elif sum(odd_numbers) > sum(even_numbers):
    different_values = odd_numbers - even_numbers
    print(", ".join(map(str, different_values)))
else:
    symmetric_different_values = even_numbers ^ odd_numbers
    print(", ".join(map(str, symmetric_different_values)))
