
# Overall Objective
# Write a class to organize wedding guests.
# The guests themselves are represented by named tuples,
# and the tables at which they were seated are represented by integers.
# The idea is for the class to help us to arrange the guests at the wedding by table.
# We're going to do that with a GuestList class. We'll create an instance of this class,
# and add our guests (as named tuples) into the guest list, along with a table number.
# We'll then be able to ask our class for a complete guest list by table, as well as a
# report of which tables aren't yet full.
#

from collections import namedtuple
from collections import defaultdict

# Create a named tuple. Note namedtuple actually returns a new 'class'.
# Creating a class called Person (right hand side) and assigning to Person (left side)
Person = namedtuple('Person', ['first', 'last'])

# Define class GuestList. This class allows us to define a guest list,
# assigning people to tables and producing reports that describe how many
# guests are at each table. Each instance of "GuestList" is going to need
# to keep track of any number of guests at a table and most of our interactions
# are going to involve the table numbers. Suggest that we store guest information
# in a dictionary,in which the table number is the key and the people sitting at
# that table are in a list. Each value will thus be a list of "Person" named tuples.
# If not assigned to a table, use 'None' - note that 'None' can be a dictionary key.
#
# Now, while we could use a regular dictionary to store our people,
# we'll be better off with a "defaultdict".  That's because we can initialize
# a defaultdict with a callable which is invoked each time a key doesn't exist.
# Given that we'll use a list as the value for each table, create a defaultdict of lists.
# Moreover, set that to be the "tables_and_guests" attribute in __init__,
# so that every time we create a new guest list, we'll have our defaultdict ready to go


class TableFull(Exception):
    pass


class GuestList(object):
    max_at_table = 10

    def __init__(self):
        self.tables_and_guests = defaultdict(list)

    # Create an assign method to assign someone to a table. thanks to defaultdict
    # since new tables_and_guests is a list and we can append 'person'.
    # We can reassign people, so we'll need to search through the entire guest list.
    def assign(self, person, new_table_number):
        # Check if there's space at table.
        if len(self.tables_and_guests[new_table_number]) == GuestList.max_at_table:
            raise TableFull('NO ROOM AT THAT TABLE!')

        # Look through existing tables; remove if the person is there.
        for table_number, guests in self.tables_and_guests.items():
            if person in guests:
                guests.remove(person)   # TBD
                break
        # Add the person to the new table
        self.tables_and_guests[new_table_number].append(person)

    # Find out how many guests are there in total.
    def __len__(self):
        return sum([len(one_table)
                    for one_table in
                    self.tables_and_guests.values()])

    # Search tables to find which guests are assigned
    def table(self, table_number):
        return self.tables_and_guests[table_number]

    # Find people who are unassigned to a table
    def unassigned(self):
        return self.table(None)

    # Find free space at a table, return a dictionary using dict comprehension.
    # We can ignore 'None'.
    def free_space(self):
        return {table_number: GuestList.max_at_table - len(guests)
                for table_number, guests in self.tables_and_guests.items()
                if table_number}

    # This next one is a tough one.
    # Obtain guest list, sorted by table, last_name, first_name. Problem is:
    # there's no table number attribute. So we need to flip this where: each
    # key is a Person namedtuple and value is the table number.
    # We have to account for guest not assigned (None) also.
    def guests(self):
        guests_dict = {one_guest: table_number
                       for table_number, guests_at_table in
                       self.tables_and_guests.items()
                       for one_guest in guests_at_table}
        return sorted(guests_dict.keys(),
                      key=lambda g: (guests_dict[g] or -1, g.last, g.first))

    # Printing format output with tables and guests per table. This is a mess
    # and not understandable.
    def __repr__(self):
        output = ''
        for table_number, guests_at_table in sorted(self.tables_and_guests.items(),
                                                    key=lambda t: t[0] or -1):
            output += '{0}\n'.format(table_number)

            for one__guest in sorted(guests_at_table,
                                    key=lambda t: t[::-1]):
                output += '\t{0}, {1}\n'.format(one__guest.last, one__guest.first)
        return output


gl = GuestList()
gl.assign(Person('Waylon', 'Dalton'), 1)
gl.assign(Person('Justine', 'Henderson'), 1)
gl.assign(Person('Abdullah', 'Lang'), 3)
gl.assign(Person('Marcus', 'Cruz'), 1)
gl.assign(Person('Thalia', 'Cobb'), 2)
gl.assign(Person('Mathias', 'Little'), 2)
gl.assign(Person('Eddie', 'Randolph'), None)
gl.assign(Person('Angela', 'Walker'), 2)
gl.assign(Person('Lia', 'Shelton'), 3)
gl.assign(Person('Hadassah', 'Hartman'), None)
gl.assign(Person('Joanna', 'Shaffer'), 3)
gl.assign(Person('Jonathon', 'Sheppard'), 2)

print()
print('-------- THE WEDDING PLANNER --------')
print('\nTotal Guests')
print(len(gl))
print('-' * 80)

print('\nGuests at table 2: ')
print(gl.table(2))
print('-' * 80)

print('\nUnassigned guests:')
print(gl.unassigned())
print('-' * 80)

print('\nTotal guests a table 2:')
print(len(gl.table(2)))
print('\nTotal guests a table 3:')
print(len(gl.table(3)))
print('-' * 80)

print('\nRe-assign Joanna to table 2')
p = Person('Joanna', 'Shaffer')
gl.assign(p, 2)
print('\nTotal guests a table 2:')
print(len(gl.table(2)))
print('\nTotal guests a table 3:')
print(len(gl.table(3)))
print('-' * 80)

print('\nFree Space for all tables')
print(gl.free_space())
print('-' * 80)

print('\nPrint out all guests:')
print()
for one_guest in gl.guests():
    print(one_guest)

print('-' * 80)
print('\nFormat print: each table by guests\n')
print(gl)
print()



