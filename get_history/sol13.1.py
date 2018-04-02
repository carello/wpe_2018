
import random


class RandMemory(object):
    def __init__(self, lowest, highest):
        self.lowest = lowest
        self.highest = highest
        self._history = []

    @property
    def get(self):
        number = random.randint(self.lowest, self.highest)
        self._history.append(number)
        return number

    def history(self):
        return self._history


r = RandMemory(1,100) # produces integers between 1 and 100
print(r.get)          # returns a number
print(r.get)          # returns a number
print(r.get)          # returns a number
print(r.history())    # returns a list of numbers previously generated
