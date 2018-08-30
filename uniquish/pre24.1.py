
seen = {}


class Foo(object):
    def __init__(self, x):
        self.x = x

    @classmethod
    def new(cls, x):
        if x not in seen:
            seen[x] = cls(x)
        return seen[x]


f1 = Foo.new(10)
f2 = Foo.new(10)
f3 = Foo.new(20)
f4 = Foo.new(10)
f5 = Foo.new(20)


s = {f1, f2, f3, f4, f5}
print(type(s))
for i in s:
    print(i)


print('\n')

class Foo2:
    _instances = {}

    def __new__(cls, *args):
        if args not in cls._instances:
            cls._instances[args] = super().__new__(cls)
        return cls._instances[args]

    def __init__(self, x):
        self.x = x


class Bar(Foo2):
    _instances = {}

    def __init__(self, x, y):
        super().__init__(x)
        self.y = y


print('\n')
f6 = Bar(10, 'abc')
f7 = Bar(10, 'abc')
f8 = Bar(20, 'xyz')
f9 = Bar(10, 'abc')
f10 = Bar(20, 'xyz')
f11 = Bar(10, 'def')
f12 = Bar(20, 'ghi')
f13 = Bar(20, 'ghi')
f14 = Bar(10, 'xyz')

ss = {f6, f7, f8, f9, f10, f11, f12, f13, f14}
for i in ss:
    print(i)

