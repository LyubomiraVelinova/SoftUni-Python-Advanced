class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.num = -self.step
        self.times = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.times <= self.count:
            self.num += self.step
            self.times += 1
            return self.num

        raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
