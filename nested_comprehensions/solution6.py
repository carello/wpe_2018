
from collections import Counter

# Objective - create various reports wiht Python built-in data structures
# Use this list of dicts. Keys are: name, age hobbies. Hobbies, will be a list.
people = [{'first': 'Chet', 'last': 'Carello', 'age': 38, 'hobbies': ['Python', 'music', 'yoga', 'hiking']},
       {'first': 'Ray', 'last': 'Cherie', 'age': 58, 'hobbies': ['music', 'space', 'books']},
       {'first': 'Connie', 'last': 'Carello', 'age': 14, 'hobbies': ['books', 'yoga', 'music', 'art']},
       {'first': 'Pasta', 'last': 'Palumbo', 'age': 22, 'hobbies': ['sax', 'music']}]

# Given this data (above), produce the following reports:
# - 1) Calculate the average age of people under 25.
# - 2A) Print all of the different hobbies that people in our database have.
# - 2B) Print a list of unique hobbies
# - 3) Show how many people have each hobby: e.g. how many people are interested in Python, how many enjoy cooking, etc.
# - 4) What are the three most common hobbies?
# - 5) What are the three most common hobbies, among people who have more than two hobbies?
# Hint: Nested list comprehension and the Counter class will make this easier.


def spacer():
    print('\n')
    print("*" * 60)
    print()

print('\n--- HOBBIES ---\n')
# Step 1: Calculate the average age of people under 25.
young_ages = [one_person['age']
                  for one_person in people
                  if one_person['age'] < 25]

print("Average age for those under 25: {}".format(sum(young_ages)/len(young_ages)))
spacer()


# Step 2A: Get a list of all hobbies we have in our dB.
def all_hobbies_all_people():
    print('--- List of all hobbies in our dB, (there will be repeats) ---\n')
    print([one_hobby                                    # Result is flat list for each value of hobby
           for one_person in people                     # Step 1: iterate across list of dicts
           for one_hobby in one_person['hobbies']])     # Step 2: iterate over Step1 list, looking for hobbies


all_hobbies_all_people()
spacer()

# Step 2B: Get a list of unique hobbies
def unique_hobbies():
    print('--- List of unique hobbies ---\n')
    print({one_hobby                                    # Result is flat list for each value of hobby
           for one_person in people                     # Step 1: iterate across list of dicts
           for one_hobby in one_person['hobbies']})     # Step 2: iterate over Step1 list, looking for hobbies


unique_hobbies()
spacer()


# Step 3/4: Show how many people have each hobby. Do a Counter of most popular hobbies
def most_popular_hobbies():
    print('--- List of all unique hobbies with respective totals per hobby and most common.---\n')
    count_unique_hobbies = (Counter([one_hobby
                               for one_person in people
                               for one_hobby in one_person['hobbies']]))
    print('Unique hobbies:\t{}'.format(count_unique_hobbies))
    print()
    for k, v in count_unique_hobbies.items():
        print('{0:.<10}: {1:.>}'.format(k, str(v)))
    print()

    # Step 4: Get most common 3 hobbies
    print('Most common hobbies:\t{}'.format(count_unique_hobbies.most_common(3)))


most_popular_hobbies()
spacer()

# Step 5: What are the three most common hobbies, among people who have more than two hobbies?
# In a normal list comprehension, the third section is an "if", allowing us to selectively
# determine if we will get output.  In a nested list comprehension, we can have one "if" for every "for".
# That is, we can filter things out after the first "for", or after the second "for".
print('--- Most common hobbies among people who have more than two hobbies ---\n')
more_than_two_hobbies = (Counter([one_hobby
                                  for one_person in people
                                  for one_hobby in one_person['hobbies']
                                  if len(one_person['hobbies']) > 2]))

print(more_than_two_hobbies.most_common(3))
print()
