import sys
from pprint import pprint
import re

# Set the pattern for matching OSPF routes
route_pattern = re.compile('^O.{4}([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})')

# Would normally grab realtime from 'show ip routes' but don't have access to a router.

# CHALLENGE - Try dictionary instead of using a list below ----!
with open('route.txt', 'r') as f:
    route_list = f.readlines()

#print(type(route_list))
pprint(route_list)


while True:
    # Grab user input of IP destination prefix
    try:
        ip_address = input('enter IP prefix, [enter "quit" to exit ]: ')
    except KeyboardInterrupt:
        print('')
        break

    if ip_address == 'exit':
        print('Goodby!\n')
        break

    # Loop through our device output of 'show ip route' for OSPF routes.
    for route in route_list:
        route_match = route_pattern.search(route)
        if not route_match:
            continue

        # If our IP address is found, print out information
        if route_match.group(1) == ip_address:
            route_info = route.split(',')
            print(route_info)
            break
    else:
        print('--- Given route prefix not found ---')


print('Program completed')

