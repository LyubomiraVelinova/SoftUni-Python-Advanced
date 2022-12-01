symbols = ["-", ",", ".", "!", "?"]

with open("01_text.txt", "r") as file:
    line_counter = 0

    for line in file:
        for symbol in symbols:
            line = line.replace(symbol, "@")

        if line_counter % 2 == 0:
            reversed_line = list(reversed(line.split()))
            print(" ".join(reversed_line))

        line_counter += 1

# symbols = ["-", ",", ".", "!", "?"]
#
#
# def symbol_replacement(symbols, line):
#     for symbol in symbols:
#         line = line.replace(symbol, "@")
#     return line
#
#
# def even_line(line_counter):
#     if line_counter % 2 == 0:
#         return reversed_line(line)
#
#
# def reversed_line(line):
#     reversed_line = list(reversed(line.split()))
#     return print(" ".join(reversed_line))
#
#
# with open("01_text.txt", "r") as file:
#     line_counter = 0
#
#     for line in file:
#         line = symbol_replacement(symbols, line)
#         even_line(line_counter)
#
#         line_counter += 1