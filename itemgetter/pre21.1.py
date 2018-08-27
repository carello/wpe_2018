
d = {'a':5, 'b':3, 'c':7, 'd':4, 'e':6}


def mygetter(*args):
    def inner(s):
        if len(args) == 1:
            return s[args[0]]
        else:
            return tuple(s[i] for i in args)
    return inner


g1 = mygetter('b', 'c')
print(g1(d))
