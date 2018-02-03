from pprint import pprint
import re

print('--- PART 1: Count Routers per Interface \n')
# This pattern looks for gig 0/0/0/0 not gig 0/0
gig_pattern = re.compile('(GigabitEthernet)([0-9]\/[0-9]\/[0-9]\/[0-9])')

routes = dict()

with open('route.txt', 'r') as f:
    for fl in f:
        match = gig_pattern.search(fl)
        if match:
            intf = match.group(2)
            #routes[intf] = routes[intf]+1 if intf in routes else 1
            if intf in routes:
                routes[intf] = routes[intf]+1
            else:
                routes[intf] = 1
        else:
            continue

print("Number of routes per interface")
print('------------------------------')
pprint(routes)



# PART 2: Tabulate OS types
print('\n--- PART 2: Tabulate OS Types\n')

os_types = {'Cisco IOS':    {'count': 0, 'devs': []},
            'Cisco Nexus':  {'count': 0, 'devs': []},
            'Cisco IOS-XR': {'count': 0, 'devs': []},
            'Cisco IOS-XE': {'count': 0, 'devs': []}}

device_info = dict()
with open('devices.txt', 'r') as g:
    for gl in g:
        device_info_list = gl.strip().split(',')
        device_info['name'] = device_info_list[0]
        device_info['os-type'] = device_info_list[1]

        name = device_info['name']
        os = device_info['os-type']

        if os == 'ios':
            os_types['Cisco IOS']['count'] += 1
            os_types['Cisco IOS']['devs'].append(name)
        elif os == 'nx-os':
            os_types['Cisco Nexus']['count'] += 1
            os_types['Cisco Nexus']['devs'].append(name)
        elif os == 'ios-xr':
            os_types['Cisco IOS-XR']['count'] += 1
            os_types['Cisco IOS-XR']['devs'].append(name)
        elif os == 'nx-xe':
            os_types['Cisco IOS-XE']['count'] += 1
            os_types['Cisco IOS-XE']['devs'].append(name)
        else:
            print("--- Warning: unknown device type: {}".format(os))

pprint(os_types)

