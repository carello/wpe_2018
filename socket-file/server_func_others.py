# server_func_others.py

def reverse_word(word):
    """Returns the supplied word in reverse.

    The function accept only one argument.
    """
    return word[::-1]

def unicode_map(word):
    """Returns all unique letters in the supplied word and their unicode points."""
    return {letter : ord(letter) for letter in word}

def average(one, two):
    """Returns the average of two numbers.

    If, for whatever reason, the calculation of the average is not possible
    this function returns None
    """

    try:
        return (float(one) + float(two))/2.0
    except ValueError:
        return None

