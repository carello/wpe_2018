
from collections import Counter

people = [{'first': 'Chet', 'last': 'Carello', 'age': 38, 'hobbies': ['Python', 'music', 'yoga', 'hiking']},
       {'first': 'Ray', 'last': 'Cherie', 'age': 58, 'hobbies': ['music', 'space', 'books']},
       {'first': 'Connie', 'last': 'Carello', 'age': 14, 'hobbies': ['books', 'yoga', 'music', 'art']},
       {'first': 'Pasta', 'last': 'Palumbo', 'age': 22, 'hobbies': ['sax', 'music']}]

def spacer():
    print('\n')
    print("*" * 60)


# calculate the average age of people under 25
# using nested list comp
young_ages = [one_person['age']
                  for one_person in people
                  if one_person['age'] < 25]

print("average age for those under 25: {}".format(sum(young_ages)/len(young_ages)))
spacer()

# get number of unique hobbies, need a Counter. need to get data in a flat list
# need nested list comprehension to do this.
def all_hobbies_all_people():
    print('--- List of all hobbies for all people, there is overlap as you can see. ---\n')
    print([one_hobby                                    # Result is flat list for each value of hobby
           for one_person in people                     # Step 1: iterate across list of dicts
           for one_hobby in one_person['hobbies']])     # Step 2: iterate over Step1 list, looking for hobbies


all_hobbies_all_people()
spacer()


def unique_hobbies():
    print('--- List of unique hobbies ---\n')
    print({one_hobby                                    # Result is flat list for each value of hobby
           for one_person in people                     # Step 1: iterate across list of dicts
           for one_hobby in one_person['hobbies']})     # Step 2: iterate over Step1 list, looking for hobbies


unique_hobbies()
spacer()

# Can now do a Counter of most popular hobbies
def most_popular_hobbies():
    print('--- List of all unique hobbies with respective totals per hobby and most common.---\n')
    count_unique_hobbies = (Counter([one_hobby
                               for one_person in people
                               for one_hobby in one_person['hobbies']]))
    print('Unique hobbies:\t\t\t{}'.format(count_unique_hobbies))
    print('Most common hobbies:\t{}'.format(count_unique_hobbies.most_common(3)))

    for k, v in count_unique_hobbies.items():
        print('{0:.<10}: {1:.>}'.format(k, str(v)))



most_popular_hobbies()
spacer()


# In a normal list comprehension, the third section is an "if", allowing us to selectively
# determine if we will get output.  In a nested list comprehension, we can have one "if" for every "for".
# That is, we can filter things out after the first "for", or after the second "for".
print('--- Most common hobbies among people who have more than two hobbies ---\n')
more_than_two_hobbies = (Counter([one_hobby
                                  for one_person in people
                                  for one_hobby in one_person['hobbies']
                                  if len(one_person['hobbies']) > 2]))

print(more_than_two_hobbies.most_common(3))

for k, v in more_than_two_hobbies.items():
    print('{0:.<10}: {1:.>}'.format(k, str(v)))