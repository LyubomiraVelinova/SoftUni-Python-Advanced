class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.index = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.index > 0:
            self.index -= 1
            return self.index
        raise StopIteration

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
