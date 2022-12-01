# nums = [1, 2, 3, 4, 5, 6]
#
# evens = [num for num in nums if num % 2 == 0]
# print(evens)

strings_list = ["1", "2", "3", "4"]

res = list(map(lambda n: int(n), strings_list))

print(res)