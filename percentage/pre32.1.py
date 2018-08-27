from weakref import WeakKeyDictionary

class PercentageTooHighError(Exception):
    pass

class PercentageTooLowError(Exception):
    pass

class Percentage(object):
    def __init__(self, initval=100):
        self._default = initval
        self._percentage = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self._percentage.get(instance, self._default)

    def __set__(self, instance, value):
        if value > 100:
            raise PercentageTooHighError(f'Percentage {value} is above 100')
        if value < 0:
            raise PercentageTooLowError(f'Percentage {value} is below zero')
        self._percentage[instance] = int(value)


class Foo(object):
    participation = Percentage()

f1 = Foo()
f1.participation = 30

f2 = Foo()
f2.participation = 70
print(f1.participation)
print(f2.participation)
