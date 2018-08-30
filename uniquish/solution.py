#!/usr/bin/env python3

class Foo(object):
    def __init__(self, x):
        self.x = x

    def __hash__(self):
        return self.x

    def __eq__(self, other):
        return self.x == other.x

f1 = Foo(10)
f2 = Foo(10)
f3 = Foo(10)

s = {f1, f2, f3}

print(s)

class Uniquish(object):
    def __hash__(self):
        return hash(vars(self).values())

    def __eq__(self, other):
        return vars(self) == vars(other)

class Bar(Uniquish):
    def __init__(self, x, y):
        self.x = x
        self.y = y

b1 = Bar(10, 'abc')
b2 = Bar(10, 'abc')
b3 = Bar(10, 'abc')

s = {b1, b2, b3}
print(s)
