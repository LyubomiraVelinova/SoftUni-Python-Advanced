from functools import reduce


def operate(op, *args):
    if op == "+":
        return reduce(lambda a, b: a + b, args)
    if op == "-":
        return reduce(lambda a, b: a - b, args)
    if op == "*":
        return reduce(lambda a, b: a * b, args)
    if op == "/":
        return reduce(lambda a, b: a / b, args)

print(operate("*", 3, 4))