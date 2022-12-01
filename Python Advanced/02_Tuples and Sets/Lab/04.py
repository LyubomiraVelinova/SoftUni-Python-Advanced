n = int(input())
parking = set()


def get_in_parking(regnum):
    parking.add(regnum)


def get_out_of_parking(regnum):
    if regnum in parking:
        parking.remove(regnum)


for _ in range(n):
    direction, regnum = input().split(", ")
    operations = {
        "IN": get_in_parking,
        "OUT": get_out_of_parking
    }
    operations[direction](regnum)
    # if direction == "IN":
    #     parking.add(regnum)
    #
    # elif direction == "OUT":
    #     parking.remove(regnum)
if parking:
    print("\n".join(parking))
else:
    print("Parking Lot is Empty")
