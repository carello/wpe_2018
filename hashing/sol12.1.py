
"""
This week, we created a Python class that makes it easy to calculate the MD5 hash of a file.
True, Python's "hashlib" provides this functionality, but requires that we load the library,
open the file, and do other actions that aren't hard, but are a bit annoying.
With our DirFileHash object, we can tell Python the name of the directory in which we'll want
to calculate MD5s, and then start to do so.

Moreover, we'll be using square brackets in order to do so. This is a bit of an abuse of the
square brackets, in that we normally use them to retrieve items via an index. But in some cases,
you can use square brackets in a slightly different way,
if you think that it'll make the API much clearer.

The key thing to remember here is that when you use square brackets, you're effectively
invoking the __getitem__ method on your object. Thus, there's no difference between:
    d = {'a':1, 'b':2, 'c':3}
    print(d['a'])

and
    d = {'a':1, 'b':2, 'c':3}
    print(d.__getitem__('a'))


If you've ever wondered why strings, lists, tuples, and dicts all use square brackets to
retrieve elements, this is the reason -- they all implement __getitem__.

First of all, we're going to be dealing with a directory name (which we pass to DirFileHash
when we initialize it, sticking it into self.filename) and also a filename. Inside of __init__,
we stick the directory name onto self.dirname, so that we can keep it around in the future.

As described above, we'll use __getitem__ to get the name of the file within the directory,
putting it inside of the variable called "filename".

At a certain point, you'll get fed up with keeping track of trailing (and lack of trailing)
slashes, cross-platform compatibility between Unix and Windows, and other such points.
You'll thus want to use os.path.join, which is similar to str.join in that it returns a string,
but different in that it's smart enough to deal with directory issues in a cross-platform way.

I use os.path.join in two stages; I first use "import os.path" to grab that module from
the "os" package. I then, later on, create the full filename we want to open with
    os.path.join(self.dirname, filename)

Inside of __getitem__, our first order of business is joining the dirname and filename together.
Following this, we open the file -- but notice that we're not using "open" with its default parameters,
but that we're rather opening it in "bytes" mode. Why do this? Because when we open a file in Python 3,
the assumption is that we want to read the Unicode characters it contains.
Because Python uses UTF-8 encoding, each character may contain one, two, or three bytes.
When we're calculating the MD5 of a file, though, we don't care about the characters.
Rather, we care about the bytes.

In order to tell Python 3 that we want to read the file by byte, and not by character,
we need to open it in "bytes" mode. Reading bytes is specified as "rb",
and writing bytes is specified as "wb".  This means that when we read from the file,
we'll get a "bytes" data structure back, rather than a string; "bytes" in Python 3 is the
same as "str" in Python 2.

To be honest, that's not a horribly difficult task, thanks to "hashlib".
We create a new instance of "hashlib.md5" (since we want to calculate the MD5),
and then we read the file, line by line, handing the contents of the file to m.update.
I should note that this is a somewhat dangerous technique, in that it assumes the file
won't be so long that reading its contents all at once will cause memory problems.
You might want to read the file into memory one line at a time, rather than all at once.

Regardless, after we have passed the file's contents -- in one fell swoop or in multiple iterations --
into m.update, we can then retrieve the MD5 hash value with the "hashdigest" method,
producing the 32-bit hex string we want.
"""


import os.path
import hashlib


class DirFileHash(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __getitem__(self, filename):
        fullname = os.path.join(self.dirname, filename)
        if os.path.exists(fullname) and os.path.isfile(fullname):
            m = hashlib.md5()
            m.update(open(fullname, 'rb').read())
            return m.hexdigest()


d = DirFileHash('/etc/')
print(d['passwd'])
