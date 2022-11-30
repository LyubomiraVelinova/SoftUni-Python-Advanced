# def reverse_text(s):
#     reversed_string = reversed(s)
#     for letter in reversed_string:
#         yield letter

def reverse_text(s):
    i = len(s)
    while i > 0:
        i -= 1
        yield s[i]


for char in reverse_text("step"):
    print(char, end='')
