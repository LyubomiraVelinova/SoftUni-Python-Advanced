total_electrons = int(input())

res = []
shield_index = 1

while total_electrons > 0:
    value = 2 * shield_index ** 2

    if total_electrons - value < 0:
        res.append(total_electrons)
    else:
        res.append(value)

    total_electrons -= value
    shield_index += 1


print(res)