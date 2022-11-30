from typing import ClassVar


class Trainer:
    name: str
    _id: ClassVar[int] = 1

    def __init__(self, name: str):
        self.name = name

        self.id = self._id
        self.__class__._id += 1  # autoincremented starting from 1

    @classmethod
    def get_next_id(cls):
        return cls._id
        # returns the id that will be given to the next trainer

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
