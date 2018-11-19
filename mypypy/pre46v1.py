#!/usr/bin/env python3


# decorator function
def mymypy(types):
    print("LEVEL 1A")
    print(types)

    def wrap(func):
        print("LEVEL 2A")
        print(func)

        def inner(*args):
            print("LEVEL 3A")
            print(*args)
            for t, a in zip(types, args):
                print("LEVEL 4A")
                if not isinstance(a, t):
                    raise TypeError(f'Argument: {a} is not type {t}')
                print(t, a)
                print("LEVEL 4B\n")

            print("LEVEL 3B")
            return func(*args)

        print("LEVEL 2B\n")
        return inner

    print("LEVEL 1B\n")
    return wrap


# --- testing ---
@mymypy([float, int])
def mul(a, b):
    return a * b


print(mul(3.3, 10))
print("%%%%%%%%%%%%%%%%%%")

