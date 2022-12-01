input_sw_version = input().split(".")

number = int("".join(input_sw_version)) + 1
next_version = str(number)
# Или изписано на един ред:
# next_version = str(int("".join(input_sw_version))+1)

print(".".join(next_version))