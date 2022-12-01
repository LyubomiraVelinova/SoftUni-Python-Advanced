from _collections import defaultdict

n = int(input())

students = defaultdict(list)

for _ in range(n):
    tokens = input().split()
    name = tokens[0]
    mark = float(tokens[1])
    students[name].append(mark)

for name, marks in students.items():
    mark_str = " ".join(map(lambda f: format(f, ".2f"), marks))

    print(f'{name} -> {mark_str} (avg: {format(sum(marks) / len(marks), ".2f")})')
