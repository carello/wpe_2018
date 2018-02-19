
# This example uses a set in the defaultdict. Interesting approach.

from collections import defaultdict
from collections import namedtuple

Person = namedtuple('Person', 'firstname, lastname')

class TableFull(Exception):
    """The requested table is already full."""
    pass


class GuestList(object):

    _MAX_GUESTS_PER_TABLE = 10

    def __init__(self):
        self._tables = defaultdict(set)

    def __len__(self):
        return sum([len(self._tables[t]) for t in self._tables])

    # This really should be '__repr__' , not  '__str__' (changed)
    def __repr__(self):
        rv = ''
        for table in self.guests():
            rv += f'Table: {table[0]}\n'
            for guest in table[1]:
                rv += f'\t{guest.lastname}, {guest.firstname}\n'
        return rv

    def assign(self, person, table):
        for t in self._tables:
            self._tables[t].discard(person)

        if table and len(self._tables[table]) >= self._MAX_GUESTS_PER_TABLE:
            raise TableFull

        self._tables[table].add(person)

    def free_space(self):
        # return {t: self._MAX_GUESTS_PER_TABLE - len(self._tables[t])
        #        for t in self._tables if self._tables[t]}
        return {t: self._MAX_GUESTS_PER_TABLE - len(self._tables[t])
                for t in self._tables if t}

    def guests(self):
        return sorted([(t, sorted(self._tables[t],
                                  key=lambda x: (x.lastname, x.firstname)))
                       for t in self._tables],
                      key=lambda x: (x[0] if isinstance(x[0], int) else 0))

    def table(self, table_number):
        return list(self._tables[table_number])

    def unassigned(self):
        return list(self._tables[None])


if __name__ == "__main__":
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
    gl.assign(Person('Jonathon', 'Sheppard'), 2)

    print('Guest List contains %d entries' % len(gl))
    print()
    print(gl.table(2))
    print()
    print(gl.unassigned)
    print()
    print(gl.free_space())
    print()
    print(gl.guests())
    print()
    print(gl)

