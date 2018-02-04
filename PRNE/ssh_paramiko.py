import paramiko
from pprint import pprint

user = 'enter username'
password = 'enter password'

ip_address = '10.91.86.244'
username = user
password = password

print('--- Attempting connection to {}'.format(ip_address))

ssh_client = paramiko.SSHClient()

# Must set missing host key policy since we don't have the SSH key stored in the 'known_hosts' file
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Make the connection to our host.
ssh_client.connect(hostname=ip_address,
                   username=username,
                   password=password)

# If there is an issue, paramiko will throw an exception,
# so the SSH request must have succeeded.

print('--- Success! connected to: {} '.format(ip_address))
print('------------------------------------------------------\n')

# Execute some commands
stdin, stdout, stderr = ssh_client.exec_command('show ip int brief')

output = stdout.readlines()
data = [line.strip('\n') for line in output]
for d in data:
    print(d)

ssh_client.close()
