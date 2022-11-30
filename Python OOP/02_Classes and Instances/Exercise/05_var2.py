from typing import ClassVar

class Time:
    max_hours: ClassVar[int] = 23
    max_minutes: ClassVar[int] = 59
    max_seconds: ClassVar[int] = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hs, ms, ss):
        self.hours = hs
        self.minutes = ms
        self.seconds = ss

    def get_time(self):
        return f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}"

    def next_second(self) -> str:
        self.seconds = (self.seconds + 1) % (self.max_seconds + 1)
        self.minutes = (self.minutes + int(self.seconds == 0)) % (self.max_minutes + 1)
        self.hours = (self.hours + int(self.minutes == 0 and self.seconds == 0)) % (self.max_hours + 1)

        return self.get_time()
