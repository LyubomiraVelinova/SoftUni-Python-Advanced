rows, cols = [int(x) for x in input().split()]
snake = input()

matrix = [[0] * cols for i in range(rows)]

for row in range(rows):
    if row % 2 == 0:
        for col in range(cols):
            if len(snake) <cols:
                snake = snake + snake[:(cols- len(snake))]
            matrix[row][col] = snake[col]

        if len(snake) > cols:
            snake = snake[cols:] + snake[:cols+1]
        print(matrix[row])
    else:
        for col in range(cols-1,-1,-1):
            if len(snake) < cols:
                pass
            matrix[row][col] = snake[cols-(col+1)]

        if len(snake) > cols:
            snake = snake[cols:] + snake[:cols+1]

        print(matrix[row])
