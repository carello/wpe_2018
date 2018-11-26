#!/usr/bin/env  python3

from collections import defaultdict
import arrow
import weakref


class MeetingRoomTakenException(Exception):
    pass


class Meeting(object):
    def __init__(self, starts_at_str, meeting_length):
        self.starts_at = arrow.get(starts_at_str)
        self.ends_at = self.starts_at.shift(hours=meeting_length)

    def __contains__(self, other):
        #print(other)
        if ((other.starts_at >= self.starts_at) and
                (other.starts_at < self.ends_at)):
            return True

    def __repr__(self):
        return f"Meeting from {self.starts_at} to {self.ends_at}"


class MeetingRoom(object):
    _counter = 0
    _instances = list()

    def __init__(self, name):
        self.name = name
        self.meetings = []
        type(self)._counter += 1
        self._instances.append(weakref.ref(self))

    def add_meeting(self, starts_at_str, meeting_length):
        new_meeting = Meeting(starts_at_str, meeting_length)
        for one_meeting in self.meetings:
            if new_meeting in one_meeting:
                raise MeetingRoomTakenException(
                    f'There is already a meeting from {one_meeting.starts_at} to {one_meeting.ends_at}')
        self.meetings.append(new_meeting)

    # not sure what this is doing  - if anything...
    def __repr__(self):
        return '\n'.join([f"[{index}: {one_meeting}]"
                          for index, one_meeting in enumerate(self.meetings)])

    @classmethod
    def get_instances(cls):
        dead = list()
        for ref in cls._instances:
            obj = ref()
            if obj is not None:
                yield obj
            else:
                dead.append(ref)
        cls._instances += dead

    @staticmethod
    def display2():
        for mr in MeetingRoom.get_instances():
            print(mr.name)
            for meet in mr.meetings:
                print('\t', meet)
            print()

    @staticmethod
    def view():
        my_list = defaultdict(list)
        for mr in MeetingRoom.get_instances():
            for meet in mr.meetings:
                my_list[mr.name].append(meet)

        for room, val in sorted(my_list.items()):
            print("ROOM: {}".format(room))
            for one_item in val:
                print("\tEVENT: {}".format(one_item))
            print()


# ---- TESTING ----
mr1 = MeetingRoom("San Jose 1")
mr1.add_meeting("1959-10-14 10:00:00", 3)
#mr1.add_meeting("1959-10-14 11:30:00", 3)
mr1.add_meeting("1960-10-14 11:00:00", 1.5)

mr2 = MeetingRoom("San Jose 2")
mr2.add_meeting("2000-01-28 12:30:00", 4)
#mr2.add_meeting("2000-01-28 13:30:00", 2)
mr2.add_meeting("2018-11-18 15:30:00", 2)
mr2.add_meeting("2018-09-28 09:30:00", 2)

mr3 = MeetingRoom("Chicago 10")
mr3.add_meeting("2018-09-28 09:30:00", 2)
mr3.add_meeting("2018-09-28 11:30:00", 1)

mr4 = MeetingRoom("Santa Barbara 5")
mr5 = MeetingRoom("Santa Barbara 7")
'''
print(mr1.name)
pprint(mr1.meetings)
print()
pprint(mr2.name)
pprint(mr2.meetings)
print()
print(mr3.name)
pprint(mr3.meetings)
print()
print(mr4.name)
pprint(mr4.meetings)
print()
total_mrs = (MeetingRoom._counter)
print(total_mrs)
'''
#MeetingRoom.display2()
MeetingRoom.view()




'''
# --- Exploring Options to delete appointments ----
pprint(MeetingRoom.appointments)
print()
for k,v in MeetingRoom.appointments.items():
    print(k, v[1])
print()
for k,v in MeetingRoom.appointments.items():
    del(k, v[1])

pprint(MeetingRoom.appointments)
MeetingRoom.display()
'''