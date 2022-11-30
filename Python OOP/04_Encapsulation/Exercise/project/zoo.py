from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.animal_base import AnimalBase
from project.employee_base import EmployeeBase


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: AnimalBase, price):
        if price <= self.__budget and self.__animal_capacity > 0:
            self.animals.append(animal)
            self.__budget -= price
            self.__animal_capacity -= 1
            type_of_animal = type(animal).__name__
            return f"{animal.name} the {type_of_animal} added to the zoo"
        if self.__animal_capacity > 0:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: EmployeeBase):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            type_of_worker = type(worker).__name__
            return f"{worker.name} the {type_of_worker} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        worker_names = [worker.name for worker in self.workers]
        if worker_name in worker_names:
            self.workers.pop(worker_names.index(worker_name))
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_due = sum([w.salary for w in self.workers])
        if total_due <= self.__budget:
            self.__budget -= total_due
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_due = sum([a.get_needs() for a in self.animals])
        if total_due <= self.__budget:
            self.__budget -= total_due
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [a.__repr__() for a in self.animals if isinstance(a, Lion)]
        tigers = [a.__repr__() for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [a.__repr__() for a in self.animals if isinstance(a, Cheetah)]

        NEW_LINE = '\n'
        return f"""You have {len(self.animals)} animals
----- {len(lions)} Lions:
{NEW_LINE.join(lions)}
----- {len(tigers)} Tigers:
{NEW_LINE.join(tigers)}
----- {len(cheetahs)} Cheetahs:
{NEW_LINE.join(cheetahs)}"""

    def workers_status(self):
        keepers = [w.__repr__() for w in self.workers if isinstance(w, Keeper)]
        caretakers = [w.__repr__() for w in self.workers if isinstance(w, Caretaker)]
        vets = [w.__repr__() for w in self.workers if isinstance(w, Vet)]

        NEW_LINE = '\n'
        return f"""You have {len(self.workers)} workers
----- {len(keepers)} Keepers:
{NEW_LINE.join(keepers)}
----- {len(caretakers)} Caretakers:
{NEW_LINE.join(caretakers)}
----- {len(vets)} Vets:
{NEW_LINE.join(vets)}"""
