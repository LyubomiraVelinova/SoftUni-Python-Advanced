rows, cols = [int(num) for num in input().split()]
matrix = [list(map(str, input().split())) for _ in range(rows)]
while True:
    line_input = input()
    if line_input == "END":
        break
    tokens = line_input.split()
    if tokens[0] == "swap" and len(tokens) == 5:
        if rows > (int(tokens[1]) and int(tokens[3])) and cols > (int(tokens[2]) and int(tokens[4])):
            first_row = int(tokens[1])
            second_row = int(tokens[3])
            first_col = int(tokens[2])
            second_col = int(tokens[4])
            first_element = matrix[first_row][first_col]
            second_element = matrix[second_row][second_col]
            matrix[first_row][first_col], matrix[second_row][second_col] = second_element, first_element
            print('\n'.join([' '.join(map(str, row)) for row in matrix]))
        else:
            print("Invalid input!")

    else:
        print("Invalid input!")
