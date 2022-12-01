def concatenate(*args):
    concatenated_strings = ""
    for string in args:
        concatenated_strings += string

    return concatenated_strings


print(concatenate("Soft", "Uni", "Is", "Great", "!"))
