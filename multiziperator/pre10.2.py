
letters = 'abcde'
numbers = [1,2,4]
symbols = '!@#$%'



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

    #return [(yield next(gen)) for gen in generators for _ in range(shortest)]


resp = multiziperator3(letters, numbers, symbols)

for x in resp:
    print(x)