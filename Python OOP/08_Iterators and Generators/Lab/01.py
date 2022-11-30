class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            index = self.start
            self.start += 1
            return index
        raise StopIteration()


one_to_three = custom_range(1, 3)
for num in one_to_three:
    print(num)
