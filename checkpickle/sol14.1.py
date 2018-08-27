'''
This exercise asked you to create an address book, but that every time we added to the address book,
the database would be saved via "pickle".  Moreover, each save should take place in a separate file
containing the timestamp, such that the user could do a selective backup, retrieving data from a specific version.
'''

import pickle
import time
from pprint import pprint

cp_stem = 'people-checkpoint-'
fields = ['first_name', 'last_name', 'email']
people = []

menu = {
    'q': ": Quit the program",
    'l': ": List all the people in the address book",
    'a': ": Add a new person to the address book",
    'r': ": Restore the address book to the stage from a timestamp",
}

while True:
    #pprint(people)
    print()
    options = menu.keys()
    for entry in options:
        print(entry, menu[entry])
    print()
    user_choice = input("Enter your choice: ").strip()

    if user_choice == 'q':
        break

    elif user_choice == 'a':
        new_person = {}
        for one_field in fields:
            new_person[one_field] = input("Enter {}: ".format(one_field)).strip()
        people.append(new_person)
        timestamp = int(time.time())
        print(timestamp)
        pickle.dump(people,
                    open("{}-{}".format(cp_stem, timestamp), 'wb'))

    elif user_choice == 'l':
        for one_person in people:
            print("{last_name}, {first_name}: email {email}".format(**one_person))

    elif user_choice == 'r':
        which_checkpoint = input("Which checkpoint to restore: ").strip()
        people = pickle.load(open("{}-{}".format(cp_stem, which_checkpoint), 'rb'))

    else:
        print("No option {}, try again".format(user_choice))

