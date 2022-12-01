is_finished = False

num_names = 0
address_book = {}

while not is_finished:
    next_input = input()

    try:
        num_names = int(next_input)
        is_finished = True
    except ValueError:
        name, phone = tuple(next_input.split("-"))
        address_book[name] = phone

for _ in range(num_names):
    name = input()
    if name not in address_book:
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {address_book[name]}")
