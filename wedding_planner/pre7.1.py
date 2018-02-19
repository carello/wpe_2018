from collections import namedtuple
from collections import Counter
import sys
from itertools import groupby

Person = namedtuple('Person', 'first, last')


# Class with Exception - don't understand this.
class TableFull(Exception):
    def __init__(self, table_num, max_seats):
        self.msg = f'Table {str(table_num)} is already full: ' f'{str(max_seats)} guests'
        super(TableFull, self).__init__(self.msg)
        self.table_num = table_num
        self.max_seats = max_seats


class GuestList(object):
    _MAX_SEATS = 10

    # init with a dictionary
    def __init__(self):
        self._guests = dict()

    # params are namedtuple of a 'person' and table.
    # - Check if there's a table assignment (None or not).
    # - If there's a table match, check to see if it's maxed out.
    def assign(self, person, table=None):
        if table is not None:
            if len([table_num
                    for person, table_num in self._guests.items()
                    if table_num == table]) >= GuestList._MAX_SEATS:
                raise TableFull(table, GuestList._MAX_SEATS)
        self._guests[person] = table

        # TBD - Try above in a conventional format

    # Get a list of people who are not assigned to a table
    def unassigned(self):
        # return [k for k, v in self._guests.items() if v is None]
        return [' '.join(person) for person, v in self._guests.items() if v is None]

    # Get a list of people by table
    def table(self, tab):
        # return [k for k, v in self._guests.items() if v == tab]
        return [' '.join(person) for person, v in self._guests.items() if v == tab]

    # Check to see how much space is available at a table
    def free_space(self):
        return {table_num: GuestList._MAX_SEATS - occupied
                for (table_num, occupied)
                in Counter(self._guests.values()).items()
                if table_num is not None}

        # Conventional non-dictionary-comprehension
        # for table_num, occupied in Counter(self._guests.values()).items():
        #     if table_num is not None:
        #         return {table_num: GuestList._MAX_SEATS - occupied}

    # Not sure why we need a generator, def guest below seems to work without this gen
    def _sort_guests(self):
        """
        Internal generator for sorting guests by table number, last name
        and first name. Unallocated guests are at the end, sorted by last
        name and first name.
        """
        return (item for item in sorted(self._guests.items(),
                                        key=lambda g: (g[1], g[0].last, g[0].first)
                                        if g[1] is not None
                                        else (sys.maxsize, g[0].last, g[0].first)))

    # Get a list of guests only
    def guests(self):
        return [' '.join(person) for person, _ in self._sort_guests()]
        #
        # Try returning not using above generator
        # return [' '.join(person) for person, _ in self._guests.items()]
        #
        # Try using no join - just returns a list
        # return [person for person in self._sort_guests()]

    # We use this for the gl object; gl has no method 'len'
    def __len__(self):
        return len(self._guests)

    # We use this for the gl object; gl has no print string method
    def __repr__(self):
        lines = list()
        for k, v in groupby(self._sort_guests(), key=lambda ln: ln[1]):
            lines.append(str(k))
            for person in list(v):
                lines.append('\t' + person[0].last + ', ' + person[0].first)
        return '\n'.join(lines)


if __name__ == '__main__':
    gl = GuestList()
    gl.assign(Person('Chet', 'Carello'), 100)
    gl.assign(Person('Ray', 'Cherie'), 4)
    gl.assign(Person('Connie', 'Charlier'), 100)
    gl.assign(Person('Pasta', 'Palumbo'))
    gl.assign(Person('Mike', 'Lill'))
    p = Person('Joanne', 'Patience')
    gl.assign(p, 3)

    print('\n--- THE WEDDING PLANNER ---')
    print('\nGuests: {}'.format(gl.guests()))
    print('\nTotal guests: {}'.format(len(gl)))
    print('\nGuests at table {0}: {1}'.format(100, gl.table(100)))
    print('\nNo table assignment: {}'.format(gl.unassigned()))
    print('\nFree "table: space" is: {}'.format(gl.free_space()))
    print()
    print('_' * 50)
    print(gl)
    print('_' * 50)
    print('Re-assign: {}'.format(p))
    gl.assign(p, 100)
    print(gl)
    print()
