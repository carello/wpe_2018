
"""
This week, we'll look at another way in which we can use Python's
magic methods to create an object that takes use of built-in operators.

We're going to create a class that I call DirFIleHash.
The idea is that you create an instance of DirFileHash by passing a directory name:
    d = DirFileHash('/etc/')

You can then get the MD5 hash of any file in this directory by
putting it in square brackets:
    print(d['passwd'])

This will return the 32-character hexadecimal MD5 hash value
for the contents of /etc/passwd.

You'll almost certainly want to use Python's "hashlib" in order to solve this exercise,
which is documented here:
    https://docs.python.org/3/library/hashlib.html
"""

import hashlib
import os


class DirFileHash():

    def __init__(self, directory):
        if os.path.isdir(directory):
            self.directory = directory
        else:
            raise TypeError(f"Argument: '{directory}' is not a directory.")

    def __getitem__(self, key):
        path = os.path.join(self.directory, key)
        if os.path.isfile(path):
            h = hashlib.md5()
            with open(path, "br") as fo:
                h.update(fo.read())
                return h.hexdigest()
        return None


dothis = DirFileHash('/etc/')
print(dothis['passwd'])
