print(filter(lambda n: n % 2 == 0), [i for i, n in enumerate(map(int, input().split(", "))))])

is_even = lambda n: n % 2 == 0
numbers = [i for i, n in enumerate(map(int, input().split(", ")))]

# DOESNT WORK
