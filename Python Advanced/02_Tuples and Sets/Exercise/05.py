address_book = {}
while True:
    command = input()
    if command.isdigit():
        number = int(command)
        break
    else:
        name, phone = tuple(command.split("-"))
        address_book[name] = phone

for _ in range(number):
    name = input()
    if name not in address_book:
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {address_book[name]}")
