import re
from pprint import pprint

filename = 'mini-access-log2.txt'

def re_line_to_dict(line):
    regexp = '''
            ((?:\d{1,3}\.){3}\d{1,3})       # IP addresses contain four numbers (each with 1-3 digits)
            .*                              # Junk between IP address and timestamp
            \[([^\]]+)\]                    # Timestamp, defined to be anything between [ and ]
            .*                              # Junk between timestamp and request
            "(GET[^"]+)"                    # Request, starting with GET
            '''
    m = re.search(regexp, line, re.X)

    if m:
        ip_address = m.group(1)
        timestamp = m.group(2)
        request = m.group(3)

    else:
        ip_address = 'No IP address found'
        timestamp = 'No timestamp found'
        request = 'No request found'

    output = {'ip_address': ip_address,
              'timestamp': timestamp,
              'request': request}
    return output


def logtolist(datafile):
    return [re_line_to_dict(line)
            for line in open(datafile)]


for one_item in logtolist(filename):
    pprint(one_item)
    print('\n')
