from pprint import pprint

# Using lists and dictionaries

devices = dict()
device_info = {}
devices_lst = list()

with open('sample.txt', 'r') as f:
    for line in f:  # put contents into a list
        #device_info_list = line.strip().split(',')
        # Using list comp
        device_info_list = [device.strip() for device in line.split(',')]

        # Put contents of the list into a dictionary
        device_info['name'] = device_info_list[0]
        device_info['os-type'] = device_info_list[1]
        device_info['ip'] = device_info_list[2]
        device_info['username'] = device_info_list[3]
        device_info['password'] = device_info_list[4]

        # Part 1 - For each device, place dictionary into a list
        devices_lst.append(device_info)

        # Part 2 - Put device list into another dictionary, based on device name
        devices[device_info['name']] = (device_info)

print("\n --- PART1: output by device name\n")
pprint(devices)
print("\n --- PART2: output just a list of devices  \n")
pprint(devices_lst)



# --- PART 3 ---

print("\n---PART3: Output by OS Type\n")
devices2 = dict()
devices2['ios'] = []
devices2['nx-os'] = []
devices2['ios-xr'] = []


# Create a dictionary of list of dictionaries to hold device information about multiple devices,
# based on OS Type for Each device.

with open('sample2.txt', 'r') as data:
    for l in data:
        #device_info_list2 = l.strip().split(',')
        # Using list comp
        device_info_list2 = [node.strip() for node in l.split(',')]

        device_info2 = {}

        device_info2['name'] = device_info_list2[0]
        device_info2['os-type'] = device_info_list2[1]
        device_info2['ip'] = device_info_list2[2]
        device_info2['username'] = device_info_list2[3]
        device_info2['password'] = device_info_list2[4]

        print('device_info2: {}'.format(device_info2))

        devices2[device_info2['os-type']].append(device_info2)

pprint(devices2)
