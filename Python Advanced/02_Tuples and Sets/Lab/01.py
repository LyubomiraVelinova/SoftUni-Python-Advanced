from collections import defaultdict

number_occurences = defaultdict(int)
numbers = list(map(float, input().split()))

for number in numbers:
    number_occurences[number] += 1

for number, occurence_count in number_occurences.items():
    print(f"{number} - {occurence_count} times")