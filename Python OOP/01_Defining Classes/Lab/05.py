class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity
        free = size - quantity

    def fill(self, mililiters):
        new_quantity = self.quantity + mililiters
        if new_quantity <= self.size:
            self.quantity = new_quantity

    def status(self):
        free_space = self.size - self.quantity
        return free_space

cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())
