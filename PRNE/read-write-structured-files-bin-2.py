import paramiko
import csv
import json
from pprint import pprint
import binascii

class NetworkDevice():
    def __init__(self, name, ip, user='9cisco', pw='9cisco'):
        self.name = name
        self.ip_address = ip
        self.username = user
        self.password = pw
        self.os_type = None
        self.sshkey = None

    def connect(self):
        self.session = None

    def get_interfaces(self):
        self.interfaces = '--- Base Device, does not know how to get interfaces ---'

    def set_sshkey(self, sshkey):
        self.sshkey = sshkey


class NetworkDeviceIOS(NetworkDevice):
    def __init__(self, name, ip, user='9cisco', pw='9cisco'):
        NetworkDevice.__init__(self, name, ip, user, pw)
        self.os_type = 'ios'

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

    dev_list = []

    json_file = open(devices_file,'r')
    json_device_data = json_file.read()
    devices_info_list = json.loads(json_device_data)


    for device_info in devices_info_list:

        # Create a device object with this data
        if device_info['os'] == 'ios':

            device = NetworkDeviceIOS(device_info['name'],device_info['ip'],
                                      device_info['user'],device_info['password'])

        elif device_info['os'] == 'ios-xr':
            device = NetworkDeviceXR(device_info['name'],device_info['ip'],
                                     device_info['user'],device_info['password'])

        else:
            device = NetworkDevice(device_info['name'],device_info['ip'],
                                   device_info['user'],device_info['password'])

        # Open SSH key file for this device
        key_file_path = "sshkeys/"+device_info['key']
        print(key_file_path)
        key_file = open(key_file_path, 'rb')

        key_data = key_file.read()  # read ssh key data
        device.set_sshkey(key_data)

        dev_list.append(device)

    return dev_list


def print_device_info(device):

    print('-------------------------------------------------------')
    print('    Device Name:      ',device.name)
    print('    Device IP:        ',device.ip_address)
    print('    Device username:  ',device.username)
    print('    Device password:  ',device.password)
    print('    Device key:       ', end='')
    print(binascii.hexlify(device.sshkey))

    print('-------------------------------------------------------\n\n')



def write_devices_info(devices_file, devices_list):
    print('--- Printing JSON output---')
    devices_out_list = list()
    for dev in devices_list:
        dev_info = {'name': dev.name, 'ip': dev.ip_address, 'os': dev.os_type, 'user': dev.username, 'password': dev.password}
        devices_out_list.append(dev_info)

    json_device_data = json.dumps(devices_out_list)

    with open(devices_file, 'w') as json_file:
        json_file.write(json_device_data)








# main section
devices_list = read_devices_info('devices-bin.json')
print('working...')
for device in devices_list:
    session = device.connect()
    device.get_interfaces()
    print_device_info(device)


