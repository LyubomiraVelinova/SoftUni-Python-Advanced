import os


def create_file(file_name):
    with open(file_name, "w") as file:
        return file.write("")


def add_line_to_file(file_name, content):
    with open(file_name, "a") as file:
        return file.write(f"{content}\n")


def replace_file(file_name, old_str, new_str):
    try:
        new_lines = []

        with open(file_name, "r") as file:
            lines = file.readlines()

            for line in lines:
                new_lines.append(line.replace(old_str, new_str))

            with open(file_name, "w") as file:
                for line in new_lines:
                    file.write(line)

    except FileNotFoundError:
        return print("An error occurred")


def delete_file(file_name):
    try:
        return os.remove(file_name)
    except FileNotFoundError:
        return print("An error occurred")


while True:
    line = input()

    if line == "End":
        break

    command = line.split("-")[0]
    if command == "Create":
        file_name = line.split("-")[1]
        create_file(file_name)

    elif command == "Add":
        file_name, content = line.split("-")[1:]
        add_line_to_file(file_name, content)

    elif command == "Replace":
        file_name, old_str, new_str = line.split("-")[1:]
        replace_file(file_name, old_str, new_str)

    elif command == "Delete":
        file_name = line.split("-")[1]
        delete_file(file_name)