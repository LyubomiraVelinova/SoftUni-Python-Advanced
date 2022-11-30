def get_primes(nums):
    not_prime_nums = []
    for i in nums:
        if i > 3:
            for j in range(2, i):
                if i % j == 0:
                    not_prime_nums.append(i)
                    break
        elif i == 0:
            not_prime_nums.append(i)
    # prime_nums = (x for x in nums if x not in not_prime_nums
    for x in nums:
        if x not in not_prime_nums:
            yield x


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
