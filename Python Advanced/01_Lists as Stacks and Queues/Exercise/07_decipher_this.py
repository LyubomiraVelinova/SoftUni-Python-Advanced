# Поправи го!

secret_message = input().split()


def split(word):
    return [char for char in word]


decipher_message = []

res = split(secret_message[0])
first_two = []
for i in range(0, 2):
    first_two.append(res[i])
first_two_int = int(''.join(first_two))
first_letter = chr(first_two_int)
decipher_message.append(first_letter)

second_letter = res[-1]
decipher_message.append(second_letter)
for i in range(3, len(res) - 1):
    decipher_message.append(res[i])

last_letter = res[2]
decipher_message.append(last_letter)

for i in range(1,len(secret_message)-1):
    res = split(secret_message[i])
    first_two = []
    for i in range(0, 3):
        first_two.append(res[i])
    first_two_int = int(''.join(first_two))
    first_letter = chr(first_two_int)
    decipher_message.append(first_letter)

    second_letter = res[-1]
    decipher_message.append(second_letter)
    for i in range(4, len(res) - 1):
        decipher_message.append(res[i])

    last_letter = res[2]
    decipher_message.append(last_letter)

# •	the second and the last letter are switched (e.g. Hello becomes Holle)
# •	the first letter is replaced by its character code (e.g. H becomes 72)


print(decipher_message)