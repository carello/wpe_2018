
import requests
import csv

output_csv = 'cities.csv'

url = 'https://gist.githubusercontent.com/reuven/77edbb0292901f35019f17edb9794358/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json'


def create_csv():
    with open(output_csv, 'w') as outfile:
        output = csv.writer(outfile, delimiter=',')
        cities = [(d['city'], d['state'], d['rank'], d['population'])
                  for d in requests.get(url).json()]
        output.writerows(cities)


import unicodecsv as csv2
def create_csv2():
    my_csv = {'city': None, 'state': None, 'population': None, 'rank': None}
    keys = my_csv.keys()

    with open('output2.csv', 'wb') as output_file:
        dict_writer = csv2.DictWriter(output_file, keys, extrasaction='ignore')
        dict_writer.writeheader()
        dict_writer.writerows(requests.get(url).json())


create_csv()
create_csv2()
