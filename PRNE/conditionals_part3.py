from pprint import pprint
import re

# PART 3: Tabulate OSPF Interfaces
print('\n--- PART 3: Tabulate OSPF Interfaces\n')

import pexpect
print("Interfaces, routes list, routes details")
print('---------------------------------------')

# Create regular expressions to match interfaces and OSPF
OSPF_pattern = re.compile('^O')
intf_pattern = re.compile('(GigabitEthernet)([0-9]\/[0-9])')


# Create regular expressions for mtach prefix and routes
prefix_pattern = re.compile('^O.{4}([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\/[0-9]{1,2})')
route_pattern = re.compile('via ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})')

# Disable until we can test with actual router
'''
print('connecting to router...')
session = pexpect.spawn('telnet 10.30.30.1', timeout=20)
result = session.expect(['Username:', pexpect.TIMEOUT])

# Check for failure
if result != 0:
    print('Timeout or unexpected reply from device')
    exit()

# enter usenname
session.sendline('cisco')
result = session.expect('Password:')

# Enter password
session.sendline('cisco')
result = session.expect('>')


# Must set terminal length to zero for long replies
print('--- setting terminal length to 0')
session.sendline('terminal length 0')
result = session.expect('>')

# Run the 'show ip route' commanmd on device
print('--- successfully logged into device, performing show ip route command')
session.sendline('show ip route')
result = session.expect('>')

# Print out the output of the command, for comparison
print('--- show ip route output:')
show_ip_route_output = session.before
print(show_ip_route_output)

# Get the output from the command into a list of lines from the output
routes_list = show_ip_route_output.splitlines()
'''


intf_routes = {}    # Create dictionary to hold number of routes per interface

# Go through the list of routes to get routes per interface
routes_list =  open('route.txt')
    #routes_list = rtr.readlines()
    #print(routes_list)
for route in routes_list:
    OSPF_match = OSPF_pattern.search(route)
    if OSPF_match:
        intf_match = intf_pattern.search(route) # Match for Gigabit Ethernet

        # Check to see if we matched the Gig Ethernet string
        if intf_match:
            intf = intf_match.group(2) # get the interface from the match
            if intf not in intf_routes:  # If route list not yet created, do so now
                intf_routes[intf] = []

            # Extract the prefix (destination IP address/subnet)
            prefix_match = prefix_pattern.search(route)
            #print(prefix_match)
            prefix = prefix_match.group(1)
            #prefix = '10.1.1.0/24'

            # Extract the route
            route_match = route_pattern.search(route)
            next_hop = route_match.group(1)

            # Create dictionary for this route, and add it to the list
            route = {'prefix': prefix, 'next-hop': next_hop}
            intf_routes[intf].append(route)

routes_list.close()

pprint(intf_routes)

