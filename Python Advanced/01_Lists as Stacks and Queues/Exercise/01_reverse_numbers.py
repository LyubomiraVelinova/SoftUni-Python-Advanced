line_input = input().split()
stack = []
for i in range(len(line_input)):
    stack.append(line_input.pop())

print(" ".join(stack))
