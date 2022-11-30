# def play_instrument(func):
#     return func.play()

from abc import ABC, abstractmethod


class Instruments(ABC):
    @abstractmethod
    def play(self):
        pass


def play_instrument(instrument: Instruments):
    return instrument.play()

class Piano:
    def play(self):
        print("playing the piano")
piano = Piano()
play_instrument(piano)

