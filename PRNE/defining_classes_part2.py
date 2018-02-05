
template = "{0:10} {1:10} {2:20} {3:20} {4:20}"

class NetworkDevice():
    def __init__(self, name, ip, user='cisco', pw='cisco'):
        self.name = name
        self.ip_address = ip
        self.username = user
        self.password = pw

    def get_type(self):
        return 'base'


class IOSDevice(NetworkDevice):
    def __init__(self, name, ip, user='cisco', pw='cisco'):
        NetworkDevice.__init__(self, name, ip, user, pw)

    def get_type(self):
        return 'IOS'

class XRDevice(NetworkDevice):
    def __init__(self, name, ip, user='cisco', pw='cisco'):
        NetworkDevice.__init__(self, name, ip, user, pw)

    def get_type(self):
        return 'IOS-XR'


def read_device_info(devices_file):
    devices_list = list()
    with open(devices_file, 'r') as f:
        for fl in f:
            device_info = fl.strip().split(',')

            if device_info[1] == 'ios':
                device = IOSDevice(device_info[0], device_info[2], device_info[3], device_info[4])

            elif device_info[1] == 'ios-xr':
                device = XRDevice(device_info[0], device_info[2], device_info[3], device_info[4])
            else:
                device = NetworkDevice(device_info[0], device_info[2], device_info[3], device_info[4])

            devices_list.append(device)
    return devices_list

def print_devices(dev):
    print(template.format('Name', 'OS-type', 'IP Address', 'Username', 'Password'))
    print('-' * 100)
    for d in dev:
        print(template.format(d.name, d.get_type(), d.ip_address, d.username, d.password))


dev_list = read_device_info('devices_file.txt')
print_devices(dev_list)
