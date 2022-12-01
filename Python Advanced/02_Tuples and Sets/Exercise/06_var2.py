num_lines = int(input())

intersections = []

for _ in range(num_lines):
    first, second = input().split("-")
    start_1, end_1 = first.split(",")
    first_set = set(range(int(start_1), int(end_1) + 1))
    start_2, end_2 = second.split(",")
    second_set = set(range(int(start_2),int(end_2)+1))

    set_intersection = first_set & second_set
    intersections.append(set_intersection)

longest_set = set()

for set_intersection in intersections:
    set_size = len(set_intersection)

    if set_size > len(longest_set):
        longest_set = set_intersection

print(f"Longest intersection is {sorted(list(longest_set))} with length {len(longest_set)}")
