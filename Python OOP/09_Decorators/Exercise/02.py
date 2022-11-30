def even_parameters(function):
    def wrapper(*args, **kwargs):
        for num in args:
            if not isinstance(num, int) or num % 2 != 0:
                return "Please use only even numbers!"

        result = function(*args, **kwargs)
        return result

    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
