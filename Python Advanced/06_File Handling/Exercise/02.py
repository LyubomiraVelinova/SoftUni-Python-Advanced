import string

with open("02_text.txt", "r") as file:
    counter = 0
    list_of_lines = []

    for line in file:
        line = line.replace("\n", "")
        counter += 1
        letters_counter = 0
        punct_mark_counter = 0
        for ch in line:
            if ch.isalpha():
                letters_counter += 1
            elif ch in string.punctuation:
                punct_mark_counter += 1

        modified_line = f"Line {counter}: {line} ({letters_counter})({punct_mark_counter})"
        list_of_lines.append(modified_line)

with open("02_output.txt", "w") as output:
        output.write("\n".join(list_of_lines))