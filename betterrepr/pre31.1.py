
def betterrepr(newstr=None, newrepr=None):
    def middle(c):
        def myrepr(self):
            "Better repr"
            return "Instance of {}, vars = {}".format(self.__class__.__name__.vars(self))

        if newstr:
            c.__str__ = newstr
        if newrepr:
            c.__repr__ = newrepr
        else:
            c.__repr__ = myrepr

        def wrapper(*args, **kwargs):
            out = c(*args, **kwargs)
            return out
        return wrapper
    return middle

def fancyrepr(self):
    return f"*** REPR !!! ***: {vars(self)}"

@betterrepr(fancyrepr)
class Foo(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

f = Foo(10,[1,2,3,4,5])
print(f)