def multiply(*args):
    multiplication = 1
    for a in args:
        multiplication *= a
    return multiplication

print(multiply(2, 0, 1000, 5000))