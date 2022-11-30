class sequence_repeat:
    def __init__(self, seq, number):
        self.sequence = seq
        self.number = number
        self.index = 0
        # self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        idx, self.index = self.index, self.index + 1
        if idx == self.number:
            raise StopIteration

        return self.sequence[idx % len(self.sequence)]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
