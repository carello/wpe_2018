from pprint import pprint
import re
OSPF_pattern = re.compile('^O')
intf_pattern = re.compile('(GigabitEthernet)([0-9]\/[0-9])')

# Create regular expressions for mtach prefix and routes
prefix_pattern = re.compile('^O.{4}([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\/[0-9]{1,2})')
route_pattern = re.compile('via ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})')

# This creates a list from 'show ip route'
#with open('route.txt', 'r') as f:
#    route_list = f.readlines()

#print(type(route_list))
#pprint(route_list)


# This creates a dict from 'show ip route'
route_dict = dict()

static = ('C', 'L', 'S')
multipath = '['

def line_to_dict(line):
    OSPF_match = OSPF_pattern.search(line)
    prefix_match = prefix_pattern.search(line)
    next_hop = route_pattern.search(line)
    intf = intf_pattern.search(line)
    if OSPF_match:
        print(OSPF_match.group(0))
        print(prefix_match.group(1))
        print(next_hop.group(0))
        print(intf.group(0))
        print('')
    #if not line.startswith(static):
    #    print(line)
    if line.startswith(' ' * 18):
        print('mulitpath OSPF', line)
        print('')



def logtolist(datafile):
    return [line_to_dict(line)
            for line in open(datafile)]


logtolist('route.txt')