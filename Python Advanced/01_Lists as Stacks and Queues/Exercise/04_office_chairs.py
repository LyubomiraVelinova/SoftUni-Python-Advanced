rooms = int(input())
room_counter = 0
total_free_chairs = 0
is_game_on = True

for room in range(rooms):
    room_counter += 1
    chairs = []
    chairs_and_people = input().split(" ")
    [chairs.append(n) for n in chairs_and_people[0]]
    total_chairs = chairs.count("X")
    needed_chairs = int(chairs_and_people[1])

    if total_chairs < needed_chairs:
        is_game_on = False
        print(f"{needed_chairs - total_chairs} more chairs needed in room {room_counter}")
    else:
        total_free_chairs += (total_chairs - needed_chairs)

if is_game_on:
    print(f"Game On, {total_free_chairs} free chairs left")