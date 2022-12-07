heroes = input().split(", ")

heroes_inventories = {hero: set() for hero in heroes}
items_costs = {}

while True:
    line = input()

    if line == "End":
        break

    hero_name, item, cost = line.split("-")
    cost = int(cost)

    heroes_inventories[hero_name].add(item)
    items_costs[item] = cost


def get_inventory_cost(inventory):


print(f"{hero_name} -> Items: {len(value)}, Cost: {cost}")