from typing import ClassVar

class Equipment:
    name: str
    _id: ClassVar[int] = 1

    def __init__(self, name: str):
        self.name = name
        self.id = self._id  # (autoincremented starting from 1)
        self.__class__._id += 1

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @classmethod
    def get_next_id(cls):
        return cls._id
