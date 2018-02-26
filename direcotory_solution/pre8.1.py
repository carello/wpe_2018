import os
import sys


def file_length(filename):
    succ_dct = dict()
    fail_dct = dict()
    sizes = [(path, os.stat(path).st_size) for path in filename]
    try:
        for s in sizes:
            if not s[1]:
                fail_dct[s[0]] = ValueError('Empty File')
            else:
                succ_dct[s[0]] = s[1]
    except Exception as e:
        print(e)
        sys.exit(1)

    return succ_dct, fail_dct


def file_func(folder, funky):
    basedir = folder
    names = os.listdir(basedir)
    paths = [os.path.join(basedir, name) for name in names]
    return funky(paths)


success_dict, failed_dict = file_func('/etc/', file_length)
print(success_dict)
print()
print(failed_dict)


