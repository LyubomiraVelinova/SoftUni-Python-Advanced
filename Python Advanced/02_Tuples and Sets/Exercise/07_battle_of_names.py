num_lines = int(input())

odd_num_set = set()
even_num_set = set()
for i in range(1, num_lines + 1):
    name = input()
    sum_letters = 0
    for ch in name:
        sum_letters += ord(ch)

    divided_sum = int(sum_letters / i)
    if divided_sum % 2 == 0:
        even_num_set.add(divided_sum)
    else:
        odd_num_set.add(divided_sum)

even_sum = sum(even_num_set)
odd_sum = sum(odd_num_set)

if even_sum == odd_sum:
    union_values = list(map(str, even_num_set | odd_num_set))
    print(", ".join(union_values))

elif even_sum < odd_sum:
    different_values = list(map(str, odd_num_set - even_num_set))
    print(", ".join(different_values))

else:
    sym_different_values = list(map(str, even_num_set ^ odd_num_set))
    print(", ".join(sym_different_values))
