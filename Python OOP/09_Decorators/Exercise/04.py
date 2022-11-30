def type_check(parameter):
    def inner(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            if parameter == type(*args):
                return result
            return "Bad Type"

        return wrapper

    return inner


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
