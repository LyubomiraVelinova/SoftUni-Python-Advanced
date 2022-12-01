version_input = input().split(".")
reversed_input = list(reversed(version_input))

reversed_strings = list(map(lambda n: int(n), reversed_input))

new_version = []
counter = 0

for i in reversed_strings:
    if counter != 0:
        new_version.append(i)
    elif i < 9:
        i += 1
        counter += 1
        new_version.append(i)
    elif i == 9:
        new_version.append(0)

new_version = list(reversed(new_version))
newest_version = list(map(lambda n: str(n), new_version))
print(".".join(newest_version))