from pprint import pprint

# --- PART 1: Create a tuple to hold device information
print('\n --- PART 1: Create a tuple to hold device information\n')
with open('sample.txt', 'r') as f:
    file_line = f.readline().strip()
    device_info = tuple(file_line.split(','))


pprint(device_info)



# --- PART 2: Create a list of tuples to hold device information about multiple devices.
print('\n --- PART 2: Create a list of tuples to hold device information about multiple devices.\n')
devices2 = list()
with open('sample2.txt', 'r') as g:
    for gl in g:
        device_info2 = tuple(gl.strip().split(','))
        #print(device_info2)
        devices2.append(device_info2)

pprint(devices2)


# --- PART 3: Create a dictionary of named tuples which hold device information, key on name
print('\n --- PART 3: Create a dictionary of named tuples which hold device information\n')
from collections import namedtuple
dev_info3 = namedtuple('Dev_Info3', ['name', 'os', 'ip', 'user', 'password'])
devices3 = dict()

with open('sample2.txt', 'r') as h:
    for hl in h:
        device_info3 = dev_info3(*(hl.strip().split(',')))
        devices3[device_info3.name] = device_info3

pprint(devices3)


# -- PART 4: Create a set of all the OS types present for the list of devices read from the file.
print('\n --- PART 4: Create a set of all the OS types present for the list of devices read from the file.\n')
dev_info4 = namedtuple('Dev_Info4', ['name', 'os_type', 'ip', 'user', 'password'])
os_types = set()

with open('sample2.txt', 'r') as j:
    for jl in j:
        device_info4 = dev_info4(*(jl.strip().split(',')))
        if device_info4.os_type not in os_types:
            os_types.add(device_info4.os_type)
        print(device_info4)
pprint(os_types)

