rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for i in range(rows)]

while True:
    line = input()

    if line == "END":
        break

    elif line.startswith("swap"):
        command = line.split()
        if len(command) == 5:
            row_1 = int(command[1])
            col_1 = int(command[2])
            row_2 = int(command[3])
            col_2 = int(command[4])
            if 0 <= row_1 <= rows-1 and 0 <= row_2 <= rows-1 and 0 <= col_1 <= cols-1 and 0 <= col_2 <= cols-1:
                temp = matrix[row_1][col_1]
                matrix[row_1][col_1] = matrix[row_2][col_2]
                matrix[row_2][col_2] = temp
                matrix_of_str = [[str(i) for i in row] for row in matrix]

                for row in matrix_of_str:
                    print(" ".join(row))
            else:
                print("Invalid input!")
        else:
            print("Invalid input!")

    else:
        print("Invalid input!")
