'''
This method does string manipulation.
Objective: Turn the file into a list of dictionaries.
Do this in a function that takes a single argument.
Since we'll be iterating over lines, we can use list
comprehension.
'''

from pprint import pprint

filename = "mini-access-log2.txt"


def line_to_dict(line):
    ip_address = line.split()[0]
    timestamp_start = line.index('[') + 1
    timestamp_end = line.index(']')
    timestamp = line[timestamp_start:timestamp_end]

    request_start = line.index('"') + 1
    request_end = line[request_start:].index('"')
    request = line[request_start:request_start+request_end]
    return {'IP_ADDRESS': ip_address, 'TIMESTAMP': timestamp, 'REQUEST': request}


def logtolist(datafile):
    return [line_to_dict(line)
            for line in open(datafile)]


for one_item in logtolist(filename):
    pprint(one_item)
    print('\n')
