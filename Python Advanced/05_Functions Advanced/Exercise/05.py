command = input()
nums = list(map(int, input().split()))

if command == "Odd":
    odd_nums = list(filter(lambda x: x % 2 != 0, nums))
    multiplied_odds = [x*len(nums) for x in odd_nums]
    print(sum(multiplied_odds))
elif command == "Even":
    even_nums = list(filter(lambda x: x % 2 == 0, nums))
    multiplied_evens = [x*len(nums) for x in even_nums]
    print(sum(multiplied_evens))
