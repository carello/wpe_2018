#!/usr/bin/env python3


class ImmutableParent(object):
    """
    Class ImmutableParent

    """

    def __init__(self, **kwargs):
        """
        This is the __init__ of the parent class

        :param kwargs:  create a  __dict__
        """
        self.__dict__.update(kwargs)

    def __setattr__(self, key, value):
        """
        This creates function to check setting attributes of the __dict__

        :param key: dictionary keys
        :param value: dictionary values
        :return: raise error if key is present in  __dict__
        """
        resp = f'Attribute {key} can not be '
        if key in self.__dict__:
            resp += 'changed'
        else:
            resp += 'added'
        raise AttributeError(resp)

    def __delattr__(self, item):
        """
        Function to delete values in __dict__

        :param item: key to delete
        :return: Raise error if key can't be deleted
        """
        raise AttributeError(f'Attribute {key} can not be deleted')

    def __repr__(self):
        """
        printing function

        :return: return vars
        """
        return f'{vars(self)}'

    def dummy(self):
        """Example function with types documented in the docstring.

        `PEP 484`_ type annotations are supported. If attribute, parameter, and
        return types are annotated according to `PEP 484`_, they do not need to be
        included in the docstring:

        Args:
            param1 (int): The first parameter.
            param2 (str): The second parameter.

        Returns:
            bool: The return value. True for success, False otherwise.

        .. _PEP 484:
            https://www.python.org/dev/peps/pep-0484/

        """
        pass


class ImmutableMe(ImmutableParent):
    """
    sub class type of parent
    """

    pass


def main():
    """
    this is main

    :return: some stuff
    """
    im = ImmutableMe(x=10, y=20, z='stuff')
    print(f"before {vars(im)}")
    print(im)
    # im.a = 999
    test_m = {}
    print(type(test_m))


if __name__ == '__main__':
    main()

