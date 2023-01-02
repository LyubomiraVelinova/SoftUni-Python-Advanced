#42/100 POINTS
from collections import deque

green_light = int(input())
free_window = int(input())
cars = deque()
cars_passed_safely = deque()
result = ""
while True:
    text = input()
    if text == "END":
        break
    elif text == "green":
        remaining_time = green_light
        free_window_duration = free_window
        while len(cars) > 0:
            passing_car = cars.popleft()
            if remaining_time - len(passing_car) >= 0:
                cars_passed_safely.append(passing_car)
                remaining_time -= len(passing_car)
            elif remaining_time - len(passing_car) < 0:
                index = remaining_time + free_window_duration
                chars = len(passing_car) - remaining_time
                if chars <= free_window_duration:
                    cars_passed_safely.append(passing_car)
                    if result == "":
                        result = f"Everyone is safe.\n{len(cars_passed_safely)} total cars passed the crossroads."
                else:
                    if result == "":
                        result = f"A crash happened!\n{passing_car} was hit at {passing_car[index]}."
                break
    else:
        cars.append(text)

print(result)
