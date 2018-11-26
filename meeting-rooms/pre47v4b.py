#!/usr/bin/env  python3

from datetime import datetime
from datetime import timedelta
from collections import defaultdict
from pprint import pprint
from dec1 import get_subject


class MeetingRoomTakenException(Exception):
    pass


class MeetingRoom(object):
    appointments = defaultdict(list)

    def __init__(self, name):
        self.name = name

    def check_overlap(self, start_meeting):
        form = '%H:%M'
        try:
            for room, val in MeetingRoom.appointments.items():
                # check room match
                if room == self.name:
                    for one_item in val:
                        # check date match
                        if one_item[0] == start_meeting.date():
                            # check time overlaps
                            if (start_meeting.time() >= one_item[1]) \
                                    and (start_meeting.time() < one_item[2]):
                                raise MeetingRoomTakenException(print(
                                    f"Could not schedule appointment "
                                    f"on {start_meeting.date()} "
                                    f"at {start_meeting.time().strftime(form)}\n"
                                    f"\t-> Meeting on {one_item[0]} "
                                    f"at {one_item[1].strftime(form)} "
                                    f"will be using the room "
                                    f"until {one_item[2].strftime(form)}"))
            else:
                return True
        except MeetingRoomTakenException:
            print("Exception is caught")
            return False


    @staticmethod
    @get_subject("drumming")
    def get_date_time(*args, result):
        date_time_combo = args[0]
        meeting_length = args[1]
        date_time_f = datetime.strptime(date_time_combo, '%Y-%m-%d %H:%M:%S')
        meeting_end_f = date_time_f + timedelta(hours=meeting_length)
        return date_time_f, meeting_end_f, result

    def add_meeting(self, *args):
        date_time_obj, meeting_end_obj, res = self.get_date_time(*args)

        if self.check_overlap(date_time_obj):
            MeetingRoom.appointments[self.name].append(
                [date_time_obj.date(), date_time_obj.time(), meeting_end_obj.time(), res])

    @staticmethod
    def display():
        form = '%H:%M'
        print("\nCurrent meetings:\n=================")
        for room, val in sorted(MeetingRoom.appointments.items()):
            print("ROOM: {}".format(room))
            for one_item in sorted(val):
                print(f"\tDATE:\t{one_item[0]}")
                print(f"\tSTART:\t{one_item[1].strftime(form)}")
                print(f"\tEND:\t{one_item[2].strftime(form)}")
                print(f"\tEVENT:\t{one_item[3]}")
                print()


# ---- TESTING ----
mr1 = MeetingRoom("San Jose 1")
mr1.add_meeting("1959-10-14 10:00:00", 3)
mr1.add_meeting("1959-10-14 11:30:00", 3)
mr2 = MeetingRoom("San Jose 2")
mr2.add_meeting("2018-11-18 15:30:00", 2)
mr2.add_meeting("2000-01-28 12:30:00", 4)
mr2.add_meeting("2000-01-28 13:30:00", 2)
mr3 = MeetingRoom("Chicago 10")
mr1.add_meeting("1960-10-14 11:00:00", 1.5)
mr3.add_meeting("2018-09-28 09:30:00", 2)
mr2.add_meeting("2018-09-28 09:30:00", 2)
mr3.add_meeting("2018-09-28 11:30:00", 1)
mr4 = MeetingRoom("Santa Barbara 5")

MeetingRoom.display()
print()

# --- Exploring Options to delete appointments ----
#pprint(MeetingRoom.appointments)
#print()
#for k,v in MeetingRoom.appointments.items():
#    print(k, v[1])
#print()
#for k,v in MeetingRoom.appointments.items():
#    del(k, v[1])

#pprint(MeetingRoom.appointments)
#MeetingRoom.display()
