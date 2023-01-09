def func_executor(*args):
    result = []
    for func_definition in args:
        func, func_args = func_definition
        return_value = func(*func_args)
        result.append(return_value)

    return result

# def func_executor(*args):
#     result = []
#     for arg in args:
#         fn = arg[0]
#         tuple = arg[1]
#         result.append(fn(*tuple))
#     return result

def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(
    func_executor(
        (sum_numbers, (1, 2)),
        (multiply_numbers, (2, 4))
    )
)
