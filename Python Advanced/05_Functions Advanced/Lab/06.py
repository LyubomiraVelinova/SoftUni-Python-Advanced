# VAR 1
# from itertools import permutations
#
# single_string = input()
# print("\n".join([''.join(p) for p in permutations(single_string)]))

# VAR 2
def print_comb(text: list, idx: int):
    if idx >= len(text):
        print("".join(text))
        return
    print_comb(text, idx + 1)
    for i in range(idx + 1, len(text)):
        text[idx], text[i] = text[i], text[idx]
        print_comb(text, idx + 1)
        text[idx], text[i] = text[i], text[idx]


text = list(input())
print_comb(text, 0)
