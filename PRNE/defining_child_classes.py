import paramiko

class NetworkDevice():
    def __init__(self, name, ip, user='cisco', pw='cisco'):
        self.name = name
        self.ip_address = ip
        self.username = user
        self.password = pw

    def connect(self):
        self.session = None

    def get_interfaces(self):
        self.interfaces = '--- Base Device, does not know how to get interfaces ---'

class NetworkDeviceIOS(NetworkDevice):
    def __init__(self, name, ip, user='admin', pw='A!min567'):
        NetworkDevice.__init__(self, name, ip, user, pw)

    def connect(self):
        print('--- Attempting connection to {}'.format(self.ip_address))

        self.ssh_client = paramiko.SSHClient()

        # Must set missing host key policy since we don't have the SSH key stored in the 'known_hosts' file
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Make the connection to our host.
        self.ssh_client.connect(hostname=self.ip_address,
                                username=self.username,
                                password=self.password)

    def get_interfaces(self):
        stdin, stdout, stderr = self.ssh_client.exec_command('show ip interface brief')
        self.interfaces = [line.strip('\n') for line in stdout.readlines()]


#======================================================================
def read_devices_info(devices_file):

    devices_list = []

    file = open(devices_file,'r')
    for line in file:

        device_info = line.strip().split(',')

        # Create a device object with this data
        if device_info[1] == 'ios':

            device = NetworkDeviceIOS(device_info[0],device_info[2],
                                      device_info[3],device_info[4])

        elif device_info[1] == 'ios-xr':

            device = NetworkDeviceXR(device_info[0],device_info[2],
                                     device_info[3],device_info[4])

        else:
            device = NetworkDevice(device_info[0],device_info[2],
                                   device_info[3],device_info[4])

        devices_list.append(device)

    return devices_list


def print_device_info(device):

    print('-------------------------------------------------------')
    print('    Device Name:      ',device.name)
    print('    Device IP:        ',device.ip_address)
    print('    Device username:  ',device.username)
    print('    Device password:  ',device.password)

    print('')
    print('    Interfaces')
    print('')

    print('-------------------------------------------------------\n\n')
    for item in device.interfaces:
        print(item)


# main section
devices_list = read_devices_info('n9k.txt')

for device in devices_list:
    session = device.connect()
    device.get_interfaces()
    print_device_info(device)

