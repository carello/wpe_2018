
"""
We want to generate random numbers, but also remember (and be able to access)
the history of numbers we've generated.
For this, we'll create a class ("RandMemory") with a property ("get") that
returns a random number:
    r = RandMemory(1,100)   # produces integers between 1 and 100
    r.get    # returns a number
    r.get    # returns a number
    r.get    # returns a number
    r.history() # returns a list of numbers previously generated

Note that r.get is *not* invoked as a method!  However, it does invoke code.
Hint: This means creating a "property", which looks to the outside as if it's
a data attribute, but from the inside works as a method.  You don't need to
create a "setter" property for this attribute.
"""

import random


class RandMemory(object):
    def __init__(self, start, end):
        self._start = start
        self._end = end
        self.mylist = list()

    @property
    def get(self):
        tmp = random.randint(self._start, self._end)
        self.mylist.append(tmp)
        return tmp

    def history(self):
        return self.mylist


man = RandMemory(1, 100)

print(man.get)
print(man.get)
print(man.get)
print(man.get)
print(man.history())


