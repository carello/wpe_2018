#!/user/bin/env python 3


class ImmutableMeansImmutableError(Exception):
    pass


class ImmutableParent(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)

    def __setattr__(self, name, value):
        raise ImmutableMeansImmutableError(f'Cannot set {name}; I am immutable!')

    def __repr__(self):
        return f'{vars(self)}'


class ImmutableMe(ImmutableParent):
    pass


im = ImmutableMe(x=111, y=222, z=[10, 20, 30], s='chet')
print(f'Before, vars(im) = {vars(im)}')
# im.x = 999
print(im)
