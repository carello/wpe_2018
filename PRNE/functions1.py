from pprint import pprint
import json

json.l
def getdata(datafile):
    data_list = [line.strip().split(',') for line in open(datafile)]
    return data_list

def dev_table(dev):
    print('\n{0:15} {1:15} {2:20} {3:20} {4:15} {5:15}'.format('Device','Platform','Version','IP','User','Pass'))
    print('-' * 100)
    for item in dev:
        print('{0:15} {1:15} {2:20} {3:20} {4:15} {5:15}'.format(item[0],item[1],item[2],item[3],item[4],item[5]))
    return


data = getdata('devices.txt')
dev_table(data)

# --- PART 2 --- #

def get_creds(dev_ip, username, password):
    """
    Connects to device
    :param dev_ip: The IP address of the device
    :param username: The username to login
    :param password: The users password to login
    :return: 1 if successful, 0 otherwise
    """
    print('Attempting to login...')
    session = 1
    result = session
    if result == 0:
        print('too bad')
        return 0
    return session

def show_int_summary(session):
    """

    :param session: credentials
    :return: show ip interface output is returned
    """
    if session == 1:
        show_int_brief = "blah, blah IP ints and stuff"
        return show_int_brief


session = get_creds('10.1.1.10', 'chet', 'hello')
result = show_int_summary(session)
print(result)



def get_credentials():
    return {'username': 'cisco', 'password': 'secret'}

print(get_credentials()['username'])


def fun(x):
    x = x - 1
    y = y + 1

x = 1
y = 2
x = fun(x)
y = fun(y)
print(x)