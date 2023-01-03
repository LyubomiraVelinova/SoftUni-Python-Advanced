from collections import defaultdict

collection = defaultdict(int)
number = 0
while True:
    info = input()
    if info.isdigit():
        number = int(info)
        break
    person, phone_num = info.split("-")
    collection[person] = phone_num

for _ in range(number):
    name = input()
    if name in collection.keys():
        phone_number = collection[name]
        print(f"{name} -> {phone_number}")
    else:
        print(f"Contact {name} does not exist.")
