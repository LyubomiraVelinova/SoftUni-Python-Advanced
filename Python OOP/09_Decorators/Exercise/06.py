def tags(parameter):
    def inner(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"<{parameter}>{result}</{parameter}>"

        return wrapper

    return inner


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))
