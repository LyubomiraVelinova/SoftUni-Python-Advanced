from collections import deque

clients = deque()
while True:
    name = input()
    if name == "End":
        print(f"{len(clients)} people remaining.")
        break
    elif name == "Paid":
        while len(clients) > 0:
            print(clients.popleft())
        clients.clear()
    else:
        clients.append(name)


