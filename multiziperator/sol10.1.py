#!/usr/bin/env python3
letters = 'abcde'
numbers = [1, 2,]
symbols = '!@#$%'


def multiziperator(*args):
    for one_index in zip(*args):
        for one_element in one_index:
            yield one_element


for one_item in multiziperator(letters, numbers, symbols):
    print(one_item)
