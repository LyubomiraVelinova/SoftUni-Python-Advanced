num_lines = int(input())

odd_num_set = set()
even_num_set = set()
for i in range(1, num_lines + 1):
    sum_chars = sum(map(ord, input()))

    divided_sum = sum_chars // i
    if divided_sum % 2 == 0:
        even_num_set.add(divided_sum)
    else:
        odd_num_set.add(divided_sum)

even_sum = sum(even_num_set)
odd_sum = sum(odd_num_set)

if even_sum == odd_sum:
    print(", ".join(map(str,even_num_set | odd_num_set)))

elif even_sum < odd_sum:
    print(", ".join(map(str,odd_num_set - even_num_set)))

else:
    print(", ".join(map(str, even_num_set ^ odd_num_set)))
