nums = tuple(float(t) for t in input().split())
list = []

for number in nums:
    if number not in list:
        list.append(number)
        print(f"{number} - {nums.count(number)} times")