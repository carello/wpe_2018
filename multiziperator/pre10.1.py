
# This week, we'll be writing another generator function.
# Normally, an iterator returns the elements of its inputs
# one at a time. This week, I want to take several inputs
# (similar to itertools.chain) but return their elements
# interleaved (like "zip").
# Psuedo-code:
#
# letters = 'abcde'
# numbers = [1,2,3,4,5]
# symbols = '!@#$%'
#
# for one_item in multiziperator(letters, numbers, symbols):
#   print(one_item)
#
# The result would be:
#
#    a
#    1
#    !
#    b
#    2
#    @
#    c
#    3
#    #
#    d
#    4
#    $
#    e
#    5
#    %
#
# In other words: We get the first element of "letters",
# then the first element of "numbers", then the first element
# of "symbols".  Then the second element of each.
# Then the third element of each.  And so forth.
#
# You should be able to pass any number of iterables to
# multiziperator.  And if they aren't the same length,
# then the shortest one determines when things stop
#
# Possible solutions:
# --- A ---
"""
from itertools import chain, izip
list(chain.from_iterable(izip(list_a, list_b)))
"""
#
# --- B ---
"""
def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    # Recipe credited to George Sakkis
    pending = len(iterables)
    nexts = cycle(iter(it).next for it in iterables)
    while pending:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            pending -= 1
            nexts = cycle(islice(nexts, pending))
"""


from itertools import chain, cycle, islice
import itertools


letters = 'abcde'
numbers = [1,2]
symbols = '!@#$%'

# Classic itertool using chain
output = list(chain.from_iterable(zip(letters, numbers, symbols)))
print(output)

'''
def cycle(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
            yield element


def islice(iterable, *args):
    # islice('ABCDEFG', 2) --> A B
    # islice('ABCDEFG', 2, 4) --> C D
    # islice('ABCDEFG', 2, None) --> C D E F G
    # islice('ABCDEFG', 0, None, 2) --> A C E G
    s = slice(*args)
    it = iter(range(s.start or 0, s.stop or sys.maxsize, s.step or 1))
    try:
        nexti = next(it)
    except StopIteration:
        return
    for i, element in enumerate(iterable):
        if i == nexti:
            yield element
            nexti = next(it)

'''

# Using a method, this one prints out everything and doesn't stop with shorted len variable
def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    num_active = len(iterables)
    nexts = cycle(iter(it).__next__ for it in iterables)

    while num_active:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            # Remove the iterator we just exhausted from the cycle.
            num_active -= 1
            nexts = cycle(islice(nexts, num_active, None))


print()
solve = roundrobin(letters, numbers, symbols)
#for s in solve:
#    print(s)


def multiziperator1(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)


print()
solved = multiziperator1(letters, numbers, symbols)
print(solved)
for ss in solved:
    for s in ss:
        print(s)


# --- Another option ---
def multiziperator3(*args):
    """ Returns interleaved elements from all input iterators in such a way that
        the number of returned elements coming from different iterators is the
        same and equal to the length of the shortest iterator.
    """
    shortest = min([len(iterator) for iterator in args])
    print('SHORT: {}'.format(shortest))
    generators = [(item for item in iterator) for iterator in args]
    for _ in range(shortest):
        for gen in generators:
            yield next(gen)


print()
solved3 = multiziperator3(letters, numbers, symbols)
for ss3 in solved3:
    print(ss3)


# --- super concise, function inside
def multiziperator4(*args):
    return [(yield y) for x in zip(*args) for y in x]


print()
solved4 = multiziperator4(letters, numbers, symbols)
for ss4 in solved4:
    print(ss4)


# --- Same as 4 above, but simpler to understand
def multiziperator5(*args):
    return (y for x in zip(*args) for y in x)


print()
solved5 = multiziperator5(letters, numbers, symbols)
print(solved5)
for ss5 in solved5:
    print(ss5)


##############################################################
print("\n\n**************************************************")
# --- Try and play ---

# Super concise example
print('\n--- GEN 1 ---')
def multiz1(*args):
    return [(yield y) for x in zip(*args) for y in x]

gen1 = multiz1(letters, numbers, symbols)
print(type(gen1))
print(gen1)
for g1 in gen1:
    print(g1)



# Simpler version of concise example above
print()
def multiz2(*args):
    for x in zip(*args):
        for y in x:
            yield y

print('\n--- GEN 2 ---')
gen2 = multiz2(letters, numbers, symbols)
print(type(gen2))
print(gen2)
for g2 in gen2:
    print(g2)



# hybrid version of above two
print()
def multiz3(*args):
    return (y for x in zip(*args) for y in x)

print('\n--- GEN 3 ---')
gen3 = multiz3(letters, numbers, symbols)
print(type(gen3))
print(gen3)
for g3 in gen3:
    print(g3)


# Using chain
print('\n--- USING CHAIN ---')
# This returns a list, not a generator
out = list(chain.from_iterable(zip(letters, numbers, symbols)))
print(type(out))
print(out)
for o in out:
    print(o)

