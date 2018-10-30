'''
Ask user to enter, one at a time: city, country where they visited. Make sure they use a comma.
Upon exit of program, provide a report in the following format (note the counter for cities:
You visited:
    China
        Beijing (2)
        Shanghai
    England
        London
    USA
        Boston
        Chicago (2)
        New York
'''


from collections import defaultdict, Counter


def location():
    while True:
        print("Tell me where you went: ")
        user_data = input().strip()

        if not user_data:
            break
        if user_data.count(',') != 1:
            print("Use city, country combo")
            continue

        city, country = user_data.split(',')
        visits[country.strip()][city.strip()] += 1

    print(visits)


    for country, cities in sorted(visits.items()):
        # print("&&&&&&&&&&") # print(visits.items()) # print(cities.items())
        print(country)
        for one_city, total in sorted(cities.items()):
            if total == 1:
                #print('\t{}'.format(one_city))
                print(f"\t{one_city}")
                
            else:
                #print('\t{} ({})'.format(one_city, count))
                print(f'\t{one_city} ({total})')


if __name__ == '__main__':
    # visits['CONGO']['chet'] += 1
    visits = defaultdict(Counter)
    print(visits)
    location()


