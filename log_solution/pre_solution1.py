from pprint import pprint

# Enter file name for parsing
data_file = "mini-access-log2.txt"

data_list = []
cleaned_data = []
keys = ['IP_ADDRESS', 'TIMESTAMP', 'REQUEST']


# Open file and set new delimiters
def get_data():
    with open(data_file, 'r') as f:
        for line in f.readlines():
            ls = line.strip()
            ls = ls.replace(' - - [', ',')
            ls = ls.replace('] "GET', ',GET')
            # cut_request_tail_index = ls.rfind('HTTP/1.') + 8
            cut_request_tail_index = ls.find('"')
            ls = ls[:cut_request_tail_index]
            cleaned_data.append((ls.split(',')))

        for stuff in cleaned_data:
            data_list.append(dict(zip(keys, stuff)))


def visualize():
    for row in data_list:
        pprint(row)
        print('\n')


if __name__ == '__main__':
    get_data()
    visualize()
