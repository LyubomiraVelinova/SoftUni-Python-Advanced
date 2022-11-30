import random


class RandomList(list):
    def get_random_element(self):
        element = random.choice(self)
        self.pop(self.index(element))
        return element


rl = RandomList(["dcjcn"])
print(rl.get_random_element())
print(list(rl))
