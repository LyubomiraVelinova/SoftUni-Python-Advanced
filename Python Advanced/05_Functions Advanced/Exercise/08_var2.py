def even_odd(*args):
    nums = []
    for i in args:
        if i == "even":
            return list(filter((lambda x: x % 2 == 0), nums))
        elif i == "odd":
            return list(filter((lambda x: x % 2 != 0), nums))
        else:
            nums.append(int(i))

print(even_odd(1, 2, 3, 4, 5, 6, "even"))