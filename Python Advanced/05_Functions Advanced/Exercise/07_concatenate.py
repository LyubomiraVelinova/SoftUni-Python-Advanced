def concatenate(*args):
    return ''.join(["".join(arg) for arg in args])


print(concatenate("Soft", "Uni", "Is", "Great", "!"))
