import paramiko
import csv
from pprint import pprint

class NetworkDevice():
    def __init__(self, name, ip, user='9cisco', pw='9cisco'):
        self.name = name
        self.ip_address = ip
        self.username = user
        self.password = pw

    def connect(self):
        self.session = None

    def get_interfaces(self):
        self.interfaces = '--- Base Device, does not know how to get interfaces ---'

class NetworkDeviceIOS(NetworkDevice):
    def __init__(self, name, ip, user='9cisco', pw='9cisco'):
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
        stdin, stdout, stderr = self.ssh_client.exec_command('show vlan summary')
        self.interfaces = [line.strip('\n') for line in stdout.readlines()]


#======================================================================
def read_devices_info(devices_file):

    devices_list = []

    file = open(devices_file,'r')
    csv_devices = csv.reader(file)
    device_info_list = [dev_info for dev_info in csv_devices]

    for device_info in device_info_list:

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


def write_devices_info(devices_file, devices_list):
    print('--- Printing CSV output---')
    devices_out_list = list()
    for device in devices_list:
        dev_info = [device.name, device.ip_address, device.interfaces]
        devices_out_list.append(dev_info)

    #pprint(devices_out_list)

    with open(devices_file, 'w') as file:
        csv_out = csv.writer(file)
        csv_out.writerows(devices_out_list)




# main section
devices_list = read_devices_info('n9k.txt')
print('working...')
for device in devices_list:
    session = device.connect()
    device.get_interfaces()
    print_device_info(device)

write_devices_info('csv-devices-out.csv', devices_list)
