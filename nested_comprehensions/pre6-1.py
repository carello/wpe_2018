
from collections import Counter

people = [{'first': 'Chet', 'last': 'Carello', 'age': 38, 'hobbies': ['Python', 'music', 'yoga', 'hiking']},
       {'first': 'Ray', 'last': 'Cherie', 'age': 58, 'hobbies': ['music', 'space', 'books']},
       {'first': 'Connie', 'last': 'Carello', 'age': 14, 'hobbies': ['books', 'yoga', 'music', 'art']},
       {'first': 'Pasta', 'last': 'Palumbo', 'age': 22, 'hobbies': ['sax', 'music']}]

def spacer():
    print('\n')
    print("*" * 60)


# Find first person in the list
print(people[0]['first'])

# Find all first names
print([one_person['first']
       for one_person in people])

# Unigue last names
print({one_person['last']
       for one_person in people})

# Find all hobbies
print([one_person['hobbies']
       for one_person in people])

# Print out all ages
print([one_person['age']
       for one_person in people])

print('*' * 100)

print('\n--- Starting Assignment ---\n')
print("*" * 60)



def age_under_25():
    print('--- Calculate the average age of people under 25 ---\n')
    counter = 0
    age_tally = 0
    all_ages = ([one_person['age']
                 for one_person in people])
    for age in all_ages:
        if age <= 25:
            counter += 1
            age_tally += age
    print('Average age under 25 years old is: {}'.format(age_tally / counter))


age_under_25()
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


most_popular_hobbies()
spacer()


# Can filter with if statements too!
def filter_hobby():
    print('--- Filter a specific hobby for a specific person ---\n')
    print([one_hobby
           for one_person in people
           if one_person['last'] == 'Cherie'
           for one_hobby in one_person['hobbies']
           if one_hobby == 'space'])        # crazy to do this but nice trick. usually one 'if' level is fine.


filter_hobby()
spacer()


# most common hobbies, where a people have more than two hobbies.
def common_two_hobbies():
    print('--- Most common hobbies among people who have more than two hobbies ---\n')
    for one_person in people:
        if len(one_person['hobbies']) > 2:
            print(one_person['first'], one_person['hobbies'])

    print("\n--- Same question, just a different look ---")
    print([one_person['first']
           for one_person in people
           if len(one_person['hobbies']) > 2])

    more_than_two_hobbies = (Counter([one_hobby
                  for one_person in people
                  for one_hobby in one_person['hobbies']
                                      if len(one_person['hobbies']) > 2]))

    print(more_than_two_hobbies.most_common(3))


common_two_hobbies()
