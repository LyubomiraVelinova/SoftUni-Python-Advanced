VOWELS = {"a", "e", "i", "o", "u", "y"}


def vowel_filter(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return [l for l in result if l.lower() in VOWELS]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
