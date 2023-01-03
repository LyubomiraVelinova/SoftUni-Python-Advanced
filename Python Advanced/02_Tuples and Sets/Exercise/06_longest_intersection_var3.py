def finding_intersection(a: set, b: set):
    return a & b


def sets_from_range(start: int, stop: int):
    return set(range(start, stop + 1))


def longest_from_list(numbers: list):
    max_length = max(len(nums) for nums in numbers)
    intersection = 0
    for nums in numbers:
        if len(nums) == max_length:
            intersection = nums
    return max_length, intersection


N = int(input())
intersections = []
for _ in range(N):
    tokens = input().split("-")
    first_start, first_stop = tokens[0].split(",")
    first_set = sets_from_range(int(first_start), int(first_stop))
    second_start, second_stop = tokens[1].split(",")
    second_set = sets_from_range(int(second_start), int(second_stop))
    intersections.append(finding_intersection(first_set, second_set))
list_intersections = [list(s) for s in intersections]
length, longest_intersection = longest_from_list(list_intersections)

print(f"Longest intersection is {longest_intersection} with length {length}")
