#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod
import sys
from operator import itemgetter


class ImmutableParent(object):
    __slots__ = []

    def __init__(self, **kwargs):
        super().__setattr__("value", kwargs)

    def __setattr__(self, key, value):
        msg = (self.__class__, key)
        raise AttributeError(msg)


class ImmutableMe(ImmutableParent):
    pass


im = ImmutableMe(x=10, y=6, z="stuff")
print(f"before {vars(im)}")


#im.s = 999

print(f"After {vars(im)}")
