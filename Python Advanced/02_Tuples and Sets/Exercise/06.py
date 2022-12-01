num_lines = int(input())

longest_set = set()

for _ in range(num_lines):
    first, second = input().split("-")
    start_1, end_1 = first.split(",")
    first_set = set(range(int(start_1), int(end_1) + 1))
    start_2, end_2 = second.split(",")
    second_set = set(range(int(start_2), int(end_2) + 1))

    intersection = first_set & second_set
    if len(intersection) > len(longest_set):
        longest_set = tuple(intersection)

print(f"Longest intersection is {list(longest_set)} with length {len(longest_set)}")
