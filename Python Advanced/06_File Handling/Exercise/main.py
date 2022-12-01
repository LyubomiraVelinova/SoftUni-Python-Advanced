try:
    file = open("file.txt", "w")
    file.write("Hello,")
    # print(file.read(2))
    # print(file.read(1))
    # print(file.read())

    # file.close()
    # for line in file:
    #     print(file.readline(5))

    # print(file.readlines())

except FileNotFoundError:
    print("File not found!")