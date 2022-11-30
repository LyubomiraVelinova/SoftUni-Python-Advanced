from typing import Dict, Any


class dictionary_iter:
    def __init__(self, data: Dict[Any, Any]):
        self.data = data
        self.__data = iter(self.data.items())

    def __iter__(self):
        return self


    def __next__(self):
        val = next(self.__data)
        return val
        # while self.i < len(self.kwargs):
        #     self.i += 1
        #     return self.kwargs.items()[self.i]
        # raise StopIteration



result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
