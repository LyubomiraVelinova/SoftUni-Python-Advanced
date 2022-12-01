import re

with open("words.txt") as words_fh:
    words = words_fh.read().split()

with open("input.txt") as input_fh:
    text = input_fh.read()

words_occurences = {}

for word in words:
    matches = re.findall(r"[\s-]({word})[\s.,?!]",text,re.MULTILINE+re.IGNORECASE)
    print(matches)

with open('output.txt') as output_th:
    for word, occurences in sorted(words_occurences.items(), key = lambda t: -t[1]):
        print(f"{word} - {occurences}", file=output_th)