
import sys
import os

"""
The Unix "tee" command lets you write data not only to standard output, but also to a file.
This is useful if you want to see the result of a command on the screen,
but also write that output to a file.

This week, we'll make it possible to create our own tee-like system in Python.
The basic idea is that you'll create an instance of the Tee class, passing it
all of the file-like objects that you want.
For example:
    import sys

    f1 = open('/tmp/tee1.txt', 'w')
    f2 = open('/tmp/tee2.txt', 'w')
    t = Tee(sys.stdout, f1, f2)

Now, when I invoke t.write or t.writelines, the method call will be applied to each of
these file-like objects.
If an error occurs, then the exception will be raised as usual:
    t.write('abc\n')
    t.write('def\n')
    t.write('ghi\n')

Invoking the above, assuming that there are no exceptions, will print the three strings
on the screen, as well as to the two other files.

For additional credit, make our "Tee" class a context manager, meaning that we can use
it within a "with" statement to guarantee that all of the file-like objects are
flushed and closed.
"""


class Tee(object):

    def __init__(self, *args):
        if not args:
            raise TypeError("At least 1 file object is required")
        else:
            self.args = args

    def __enter__(self):
        return self

    def __exit__(self, t_type, value, traceback):
        for doc in self.args:
            doc.close()

    def write(self, s_string):
        for doc in self.args:
            doc.write(s_string)
            doc.flush()      # Write to file
            try:
                if doc != sys.stdout:
                    os.fsync(doc)   # Commit changes to file
            except TypeError:
                pass


if __name__ == '__main__':
    f1 = open('tee1.txt', 'w')
    f2 = open('tee2.txt', 'w')

    with Tee(sys.stdout, f1, f2) as g:
        g.write('chet\n')
        g.write('connie\n')
        g.write('789\n')
