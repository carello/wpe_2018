import os
import sys


def file_length(filename):
    return [(path, os.stat(path).st_size) for path in filename]


def file_func(folder, funky):
    succ_dct = dict()
    fail_dct = dict()
    basedir = folder
    names = os.listdir(basedir)
    paths = [os.path.join(basedir, name) for name in names]
    sizes = funky(paths)

    try:
        for s in sizes:
            if not s[1]:
                fail_dct[s[0]] = ValueError(s)
            else:
                succ_dct[s[0]] = s[1]
    except Exception as e:
        print(e)
        sys.exit(1)

    return succ_dct, fail_dct


success_dict, failed_dict = file_func('/etc/', file_length)
print(success_dict)
print()
print(failed_dict)





success_dict, failed_dict = file_func('/etc/', file_length)
print(success_dict)
print()
print(failed_dict)