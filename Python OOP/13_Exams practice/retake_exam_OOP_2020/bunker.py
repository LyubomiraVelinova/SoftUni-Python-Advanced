from project.medicine.medicine import Medicine
from project.supply.supply import Supply
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food_obj = [o for o in self.supplies if o.__class__.__name__ == "FoodSupply"]
        if len(food_obj) == 0:
            raise IndexError("There are no food supplies left!")
        return food_obj

    @property
    def water(self):
        water_obj = [o for o in self.supplies if o.__class__.__name__ == "WaterSupply"]
        if len(water_obj) == 0:
            raise IndexError("There are no water supplies left!")
        return water_obj

    @property
    def painkillers(self):
        painkillers_obj = [o for o in self.medicine if o.__class__.__name__ == "Painkiller"]
        if len(painkillers_obj) == 0:
            raise IndexError("There are no painkillers left!")
        return painkillers_obj

    @property
    def salves(self):
        salves_obj = [o for o in self.medicine if o.__class__.__name__ == "Salve"]
        if len(salves_obj) == 0:
            raise IndexError("There are no salves left!")
        return salves_obj

    def add_survivor(self, survivor: Survivor):
        # survivor_names = [s.name for s in self.survivors]
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        pill = ""
        if not survivor.needs_healing:
            return

        if medicine_type == "Painkiller":
            pill = self.painkillers.pop()
        elif medicine_type == "Salve":
            pill = self.salves.pop()
        pill.apply(survivor)
        return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        sus = ""
        if not survivor.needs_sustenance:
            return

        if sustenance_type == "FoodSupply":
            sus = self.food.pop()
        elif sustenance_type == "WaterSupply":
            sus = self.water.pop()
        sus.apply(survivor)
        return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for s in self.survivors:
            s.needs -= s.age * 2

        for s in self.survivors:
            self.sustain(s, "FoodSupply")
            self.sustain(s, "WaterSupply")

# b = Bunker()
# s = Survivor("Test1", 100)
# f = FoodSupply()
# b.add_supply(f)
# b.sustain(s, "FoodSupply")
# print(len(b.food))
