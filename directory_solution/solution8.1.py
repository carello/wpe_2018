#!/usr/bin/env python3

import os

def filefunc(dirname, func):
    success_dict = {}
    failure_dict = {}

    for filename in os.listdir(dirname):
        try:
            success_dict[filename] = func(dirname + filename)
        except Exception as e:
            failure_dict[filename] = e
    return success_dict, failure_dict


def file_len(filename):
    return len(open(filename).read())


print(filefunc('/etc/', file_len))
