import re
from pprint import pprint
current_version = "Version 5.3.1"

print("--- PART 1: ID devices running invalid code\n")
device_info = dict()
'''
with open('sample_versions1.txt', 'r') as f:
    for fl in f:
        device_info_file1 = fl.strip().split(',')
        device_info['name'] = device_info_file1[0]
        device_info['os'] = device_info_file1[1]
        device_info['version'] = device_info_file1[2]
        device_info['ip'] = device_info_file1[3]
        device_info['username'] = device_info_file1[4]
        device_info['password'] = device_info_file1[5]

        if device_info['version'] != current_version:
            print('\tDevice: {} \tVersion: {}'.format(device_info['name'], device_info['version']))
'''
# --- PART 2: Using Regex
print("\n--- PART 2: Using Regex\n")

ip_addr_pattern = re.compile('Mgmt:([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})')

dev_info2 = dict()
with open('sample_versions1.txt', 'r') as g:
    for gl in g:
        device_info_list = gl.strip().split(',')
        dev_info2['name'] = device_info_list[0]

        mgmt_addr = ip_addr_pattern.search(gl)
        dev_info2['ip'] = mgmt_addr.group(1)
        print('\tDevice: {} \tMgMT IP: {}'.format(dev_info2['name'], dev_info2['ip']))

