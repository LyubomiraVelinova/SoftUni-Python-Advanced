class Vet:
    animals = []  # Stores all animals in the clinic
    space = 5

    def __init__(self, name: str):
        self.name = name
        self.animals = []  # Stores animals associated to the current Vet

    def register_animal(self, animal_name):
        if len(Vet.animals) < Vet.space:
            self.animals.append(animal_name)
            Vet.animals.append(animal_name)
            return f"{animal_name} registered in the clinic"
        else:
            return "Not enough space"

    def unregister_animal(self, animal_name):
        if animal_name in self.animals:
            # self.animals.pop(self.animals.index(animal_name))
            # Vet.animals.pop(Vet.animals.index(animal_name))
            self.animals.remove(animal_name)
            Vet.animals.remove(animal_name)
            return f"{animal_name} unregistered successfully"
        else:
            return f"{animal_name} not in the clinic"

    def info(self):
        vet_name = self.name
        amount_of_animals = len(self.animals)
        space_left_in_clinic = Vet.space - len(Vet.animals)
        return f"{vet_name} has {amount_of_animals} animals. {space_left_in_clinic} space left in clinic"


peter = Vet('jj')
george = Vet("George")
print(peter.register_animal("Tom"))
