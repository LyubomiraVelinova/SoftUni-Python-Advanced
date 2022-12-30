from collections import deque

food_qty = int(input())
orders_queue = deque(map(lambda n: int(n), input().split()))
print(max(orders_queue))

while True:
    order = orders_queue.popleft()
    if order <= food_qty:
        food_qty -= order
    else:
        orders_queue.appendleft(order)
        break

if orders_queue:
    print(f"Orders left: {' '.join(map(str, orders_queue))}")
else:
    print("Orders complete")
