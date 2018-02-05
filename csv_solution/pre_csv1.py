
import unicodecsv as csv
import json

# Select input and output files
data_src = 'test.json'
output_csv = 'data.csv'
lst = []


# Convert source raw files into json format
def create_json_py():
    with open(data_src, 'r') as f:
        j_data = f.read()
        json_data = json.loads(j_data)
        return json_data


# Select required keys and create a new list-of-dicts
def create_lst(j_frmt):
    for item, index in enumerate(j_frmt):
        new_dict = dict()
        new_dict['city'] = j_frmt[item]['city']
        new_dict['state'] = j_frmt[item]['state']
        new_dict['population'] = j_frmt[item]['population']
        new_dict['rank'] = j_frmt[item]['rank']
        lst.append(new_dict)
    return lst


# Create csv
def create_csv():
    # my_csv = {'city': None, 'state': None, 'population': None, 'rank': None}
    # keys = my_csv.keys()
    keys = lst[0].keys()

    with open(output_csv, 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(lst)


if __name__ == '__main__':
    json_frmt = create_json_py()
    create_lst(json_frmt)
    create_csv()


