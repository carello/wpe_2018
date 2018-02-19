

from collections import namedtuple
from collections import defaultdict
from pprint import pprint

# Create a named tuple. Note namedtuple actually returns a new 'class'.
# Creating a class called Person (right hand side) and assigning to Person (left side)
Person = namedtuple('Person', ['first', 'last'])


class TableFull(Exception):
    pass


class GuestList(object):
    max_at_table = 10

    def __init__(self):
        self.tables_and_guests = defaultdict(list)

    # Create an assign method to assign someone to a table. Thanks to defaultdict
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
    # this puts out only name and you can tell order because you don't have tables.
    # not a useful method. The '__repr__' below is better and clearer.
    def guests(self):
        print('--- Print tables_and_guests, you can see its a dict. ---')
        print(type(self.tables_and_guests))
        print(self.tables_and_guests)

        print('\n##################')
        guests_dict = {the_guest: table_number
                       for table_number, guests_at_table in
                       self.tables_and_guests.items()
                       for the_guest in guests_at_table}


        print('--- Print out the guest_dict, we can see reversed defaultdict. ---')
        print(guests_dict)
        print('##################\n')
        print('--- Print out sorted guest_dict ---')
        print(sorted(guests_dict.keys(),
                      key=lambda g: (guests_dict[g] or -1, g.last, g.first)))
        print()
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
print('TEST')
for one_guest, v in gl.guests():
    print(one_guest, v)
print('\nEND')
print('-' * 80)
print('\nFormat print: each table by guests\n')
print(gl)
print()



