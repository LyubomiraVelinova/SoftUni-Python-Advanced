class Hero:
    username: str
    level: int

    def __init__(self, username: str, level: int):
        self.username = username
        self.level = level

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{self.username} of type {class_name} has level {self.level}"
