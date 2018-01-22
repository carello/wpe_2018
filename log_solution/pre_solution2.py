import re
from pprint import pprint

regex = re.compile(r'(?P<IP_ADDRESS>(?:\d{1,3}\.){3}\d{1,3}).+?\[(?P<TIMESTAMP>.+?)\].?"(?P<METHOD>.+?)"')


with open('mini-access-log2.txt', 'r') as file:
    output = [re.match(regex, line).groupdict() for line in file]

pprint(output)

