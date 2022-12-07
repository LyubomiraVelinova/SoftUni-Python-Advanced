lists = [outer_list.split() for outer_list in input().split("|")]

output_list = [elem for list in reversed(lists) for elem in list]

print(" ".join(output_list))