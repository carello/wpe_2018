
# Print template
template = '{0:10} {1:10} {2:15} {3:10} {4:10}'
#    print(template.format("TENANT", "APP_PROFILE", "EPG"))
#    print(template.format("------", "-----------", "---"))
#    for rec in data:
#        print(template.format(*rec))

# --- PART 1 --- #
print('\n--- PART 1 ---')
class NetworkDevice1():

    def set_info(self, name, os, ip, user='cisco', pw='cisco'):
        self.name = name
        self.os_type = os
        self.ip_address = ip
        self.username = user
        self.password = pw

def print_device_info1(devices_list):
    print('')
    #print('{0:10} {1:10} {2:15} {3:10} {4:10}'.format('Name', 'OS-type', 'IP Address', 'Username', 'Password'))
    print(template.format('Name', 'OS-type', 'IP Address', 'Username', 'Password'))
    print('-' * 55)
    for device in devices_list:
        print(template.format(device.name, device.os_type, device.ip_address, device.username, device.password))

    print('')


dev1 = NetworkDevice1()
dev1.set_info('dev1', 'nx-os', '9.9.9.9')
dev2 = NetworkDevice1()
dev2.set_info('dev2', 'ios', '8.8.8.8', 'chet', 'connie')
print_device_info1([dev1, dev2])



# --- PART 2 --- #
print('\n--- PART 2 ---'.format(end=''))

class NetworkDevice():

    def __init__(self, name, os, ip, user='cisco', pw='cisco'):
        self.name = name
        self.os_type = os
        self.ip_address = ip
        self.username = user
        self.password = pw

def print_device_info(devices_list):
    print('')
    print('{0:10} {1:10} {2:15} {3:10} {4:10}'.format('Name', 'OS-type', 'IP Address', 'Username', 'Password'))
    print('-' * 55)
    for device in devices_list:
        print('{0:10} {1:10} {2:15} {3:10} {4:10}'.format(device.name, device.os_type, device.ip_address, device.username, device.password))
    print('')

def read_device_info(devices_file):
    devices = list()
    with open(devices_file, 'r') as f:
        for fl in f:
            device_info = fl.strip().split(',')
            device = NetworkDevice(device_info[0], device_info[1], device_info[2], device_info[3], device_info[4])
            devices.append(device)
    return devices


devices_list = read_device_info('devices_file.txt')
print_device_info(devices_list)

devices_list = read_device_info('real_devices.txt')
print_device_info(devices_list)


