import re
import operator
import arrow


class LogDicts(object):
    ts_format = 'DD/MMM/YYYY:HH:mm:ss Z'

    def __init__(self, filename):
        self._dicts = [self.line_to_dict(line)
                       for line in open(filename)]

    def dicts(self, key=None):
        return list(self.iterdicts(key=key))


    def iterdicts(self, key=None):
        if key:
            return (item
                for item in sorted(self._dicts, key=key))
        else:
            return (item
                    for item in self._dicts)


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

    def earliest(self):
        return min(self._dicts,
                   key=lambda d: arrow.get(d['timestamp'], self.ts_format))

    def latest(self):
        return max(self._dicts,
                   key=lambda d: arrow.get(d['timestamp'], self.ts_format))

    def for_ip(self, ip_address, key=None):
        if key is None:
            key = lambda d: 1

        return [d
                for d in sorted(self._dicts, key=key)
                if ip_address == d['ip_address']]

    def for_request(self, text, key=None):
        if key is None:
            key = lambda d: 1

        return [d
                for d in sorted(self._dicts, key=key)
                if text in d['request']]


id = LogDicts('mini-access-log2.txt')

#print(id.dicts(key=operator.itemgetter('request'))[0])
#print(list(id.iterdicts(key=operator.itemgetter('REQUEST')))[0])
#print(list(id.iterdicts(key=operator.itemgetter('REQUEST')))[-1])
#print(id.for_ip('66.249.71.65'))
#print(id.for_request('/robots.txt'))
#print(id.earliest())
#print(id.latest())