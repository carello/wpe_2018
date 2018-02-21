import re
import operator
import arrow
from pprint import pprint

# Create a LogDicts class. Load a file upon creating an instance of this class.
# Methods to create:
#   1) return a list of all dicts, e.g: ld.dicts(key=None)
#   2) return an iterator of dicts rather than the list all at once, e.g: ld.iterdicts(key=None)
#   3) return the dict with the earliest timestamp. e.g: ld.earliest()
#   4) return the dict with the latest timestamp. e.g: ld.latest()
# Time stamp for 3/4 above will be tricky, use arrow or time.strptime
#   5) return the dict with X IP_address, e.g: ld.for_ip(ip_address, key=None)
#   6) return the dict with specific text, e.g: ld.for_request(text, key=None)
# The 'key' parameter is for the ability to sort the resulting list of dictionaries.
#


class LogDicts(object):
    ts_format = 'DD/MMM/YYYY:HH:mm:ss Z'

    # Open file upon initialization of the object instance. Notice we call line_to_dict method.
    def __init__(self, filename):
        self._dicts = [self.line_to_dict(line)
                       for line in open(filename)]

    # Break things down to IP Address, timestamp and request. return a dictionary
    def line_to_dict(self, line):
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
            ip_address = 'No IP_ADDR found'
            timestamp = 'No TIMESTAMP found'
            request = 'No REQUEST found'

        output = {'ip_address': ip_address,
                  'timestamp': timestamp,
                  'request': request}
        return output

    # Return a list of all dicts, key is for sorting. This method just calls interdicts method out of convenience.
    def dicts(self, key=None):
        return list(self.iterdicts(key=key))

    # Return a iterator of dicts, use a generator expression. Key is for sorting
    def iterdicts(self, key=None):
        if key:
            return (item
                    for item in sorted(self._dicts, key=key))
        else:
            return (item
                    for item in self._dicts)

    # Return dict with earliest timestamp. We need to turn timestamp into an object that we can compare
    def earliest(self):
        return min(self._dicts,
                   key=lambda d: arrow.get(d['timestamp'], self.ts_format))

    # Return dict with latest timestamp. We need to turn timestamp into an object that we can compare
    def latest(self):
        return max(self._dicts,
                   key=lambda d: arrow.get(d['timestamp'], self.ts_format))

    # Return dict with specific IP Address
    def for_ip(self, ip_address, key=None):
        if key is None:
            key = lambda d: 1
            # this is trick for python3; we can't compare dicts with 'and.
            # If we get a 'None' key, we use a function that returns 1.

        return [d
                for d in sorted(self._dicts, key=key)
                if ip_address == d['ip_address']]

    # Return dict with specific text
    def for_request(self, text, key=None):
        if key is None:
            key = lambda d: 1
            # this is trick for python3; we can't compare dicts with 'and.
            # If we get a 'None' key, we use a function that returns 1.

        return [d
                for d in sorted(self._dicts, key=key)
                if text in d['request']]


ld = LogDicts('mini-access-log2.txt')

print()
print('\n*** LOG FILTERING ***')
print('=' * 120)


print('\n--- Retrieve first entry in data file based on request being true,'
      '(note order is changed due to list(self.iterdicts) ---\n')
print(ld.dicts(key=operator.itemgetter('request'))[0])
print('-' * 120)

print('\n--- Retrieve last entry in data file based on request being true,'
      '(note order is changed due to list(self.iterdicts)---\n')
print(list(ld.iterdicts(key=operator.itemgetter('request')))[-1])
print('-' * 120)

# recall that 'iterdicts' is a generator returning an iterable, so we need 'list' to view this
print('\n--- Retrieve list dicts using interdicts, note that order is now changed from original file ---\n')
pprint(list(ld.iterdicts(key=operator.itemgetter('request'))))
print('-' * 120)

print('\n--- Retrieve IP for example: 66.249.71.65 ---\n')
pprint(ld.for_ip('66.249.71.65'))
print('-' * 120)

print('\n--- Retrieve based on request being "/robots.txt" ---\n')
pprint(ld.for_request('/robots.txt'))
print('-' * 120)

print('\n--- Retrieve based on earliest timestamp ---\n')
print(ld.earliest())
print('-' * 120)

print('\n--- Retrieve based on latest timestamp ---\n')
print(ld.latest())
print('-' * 120)
print()
