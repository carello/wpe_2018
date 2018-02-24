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
# - Create a GuestList class
# - Create an instance of this class, add our guests (as named tuples) to the guest list, along with a table num.
# - namedtuples should look something like this:
#       defaultdict(<class 'list'>, {24: [Person(first='Chet', last='Smith'), Person(first='Connie', last='Charlier')],
#       7: [Person(first='Joanna', last='Shaffer')], None: [Person(first='Pasta', last='Palumbo')]
#
#   Assume everyone has a unique name.
# - Create reports of: complete guest list by table and a report of which tables aren't full.


# ========================= INSTRUCTIONS==================================
#
# Example how this should work:
# Person should be a named tuple, with "first" and "last" attributes
#   gl = GuestList()
#   gl.assign(Person('Waylon', 'Dalton'), 1)
#   gl.assign(Person('Justine', 'Henderson'), 1)
#   gl.assign(Person('Abdullah', 'Lang'), 3)
#   gl.assign(Person('Mathias', 'Little'), 2)
#   gl.assign(Person('Eddie', 'Randolph'), None)
#
# Now we want to run reports
# 1) How many guests total? run: len(gl) to get an integer back.
# 2) What guests are at a given table? run: gl.table(2) to get a list of of Person object back.
# 3) What guests aren't assigned to any table? run: gl.unassigned() to get a list of Person object back
#
# 4) Given a Person object, we should be able to assign them to a table:
#   p = Person('Joanna', 'Shaffer')
#   gl.assign(p, 3)
# If the person is already in the system, but is assigned to another table (or to no table at all),
# then they will now be assigned to a new table.
# If the person isn't already in the system, then they will be added and then assigned to a table.
# If there is no room at the table (i.e., there are already 10 guests), then we should raise a TableFull exception.
#
# 5) We should also be able to learn how much space is available at each table: gl.free_space()
# Returning The a dictionary of table names (keys) and remaining space (values) for each table.
#
# 6) Run: gl.guest() and get a list of all guests, sorted first by table number, then last name, then first name.
#
# 7) Finally run: print(gl) and get a nicely printed output as:
#    2
#        last, first
#        last, first
#    3
#        last, first
#        last, first
#    4
#        last, first
#        last, first
#        last, first
#
# ==============================================================================

# import

# Create a named tuple. Note namedtuple actually returns a new 'class'.
# Creating a class called Person (right hand side) and assigning to Person (left side)
Person = namedtuple('Person', ['first', 'last'])


# If there is no room at the table (i.e., there are already 10 guests), then we should raise a TableFull exception.
class TableFull(Exception):
    pass


# Create Guestlist
class GuestList(object):

    def __init__(self):
        pass

    # Assign people to a table using append
    # 1) Check if there's space at the table
    def assign(self, person, new_table):
        pass

        # 2) RE-ASSIGN: check tables; remove if person is there


        # 3) Assign to table



    # Find out how many guests there are (total).
    def __len__(self):
        pass


    # Search tables to find which guests are assigned
    def table(self, table_number):
        pass


    # Find which people are unassigned
    def unassigned(self):
        pass


    # Find free space. Ignore 'None'. Return as a dictionary
    def free_space(self):
        pass



    # Obtain guest list by: table num, last, first
    def guests(self):
        pass

    # Output printint format
    def __repr__(self):
        pass


# ==============================

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
