from pprint import pprint
import sys

devices_list = list()

index = 0
with open('devices.txt', 'r') as f:
    for fl in f:
        device_info_list = fl.split(',')
        devices_list.append(device_info_list)

    print('{0:10} {1:10} {2:20} {3}'.format('Name', 'OS_Type', 'Software', 'IP Address'))
    print('-------------------------------------------------------')

    ip_addresses = set()

    for item in devices_list:
        print('{0:10} {1:10} {2:20} {3}'.format(item[0], item[1], item[2], item[3]), end='')
        if item[3] in ip_addresses:
            print("\t*DUP*")
            continue
        ip_addresses.add(item[3])
        print('')


# PART 2
print("\n--- SELECT BY IP\n")
devices_list2 = list()

with open('devices.txt', 'r') as g:
    for gl in g:
        device_info2 = gl.split(',')
        devices_list2.append(device_info2)



while True:
    try:
        ip_address = input('enter IP Address, [enter "quit" to exit ]: ')
    except KeyboardInterrupt:
        print('')
        break

    for item, index in enumerate(devices_list2):
        if index[3][5:] == ip_address:
            print('{0:10} {1:10} {2:20} {3}'.format(index[0], index[1], index[2], index[3]))
            sys.exit(0)
        else:
            continue

    if ip_address == 'exit':
        break
    else:
        print("--- Given IP address not found ---\n")




