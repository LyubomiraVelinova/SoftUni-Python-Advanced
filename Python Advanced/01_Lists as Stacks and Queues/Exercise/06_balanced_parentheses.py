from collections import deque

BALANCED_PAIRS = ["{}", "[]", "()"]

line_input = input()
sequence = deque(ch for ch in line_input)
is_balanced = False
while len(sequence) > 0:
    pair = sequence.popleft() + sequence.pop()
    if pair in BALANCED_PAIRS:
        is_balanced = True
    else:
        is_balanced = False

if is_balanced:
    print("YES")
else:
    print("NO")
