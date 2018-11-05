#!/etc/bin/env python3

import sqlite3
from sqlite3 import Error
import time
from datetime import datetime
import sys
from collections import namedtuple


def create_connection(db_file):
    try:
        connected = sqlite3.connect(db_file)
        return connected
    except Error as e:
        print("Unable to create db connection - {}".format(e))
        sys.exit(0)


def create_table(connection, create_table_sql):
    try:
        with connection:
            c = connection.cursor()
            c.execute(create_table_sql)
    except Error as e:
        print("Unable to create table - {}".format(e))
        sys.exit(0)


def create_db(connection):
    sql_create_projects_appointments = """ CREATE TABLE IF NOT EXISTS appointments (
                                        id integer PRIMARY KEY,
                                        title text,
                                        date_start TIMESTAMP,
                                        end_time TIMESTAMP,
                                        comment text
                                    ); """
    try:
        with connection:
            create_table(connection, sql_create_projects_appointments)
    except Error as e:
        print("Cannot create the database table - {}".format(e))
        sys.exit(0)


def create_appointment():
    User_input = namedtuple('User_input', [
        'title',
        'date_start',
        'end',
        'notes'
    ])
    while True:
        title = input("\tEnter a meeting title ->: ").strip()
        if len(title) == 0:
            print("Please enter a meeting title")
        else:
            break
    while True:
        date = input("\tEnter date in MM/DD/YYYY format ->: ").strip()
        if is_date_format(date):
            break
    while True:
        start = input("\tEnter start time in HH:MM ->: ").strip()
        if is_time_format(start):
            break
    while True:
        end = input("\tEnter end time in HH:MM ->: ").strip()
        if is_time_format(end):
            break

    notes = input("\tEnter optional notes for the meeting ->: ").strip()
    date_start = ' '.join((date, start))
    request = User_input(title, date_start, end, notes)
    insert_data(conn, request)
    print("-> Meeting is scheduled\n")


def insert_data(connection, request):
    sql = ''' INSERT INTO appointments(title, date_start, end_time, comment)
                         VALUES(?,?,?,?) '''
    try:
        with connection:
            cur = connection.cursor()
            cur.execute(sql, request)
            connection.commit()
    except Error as e:
        print("Cannot insert data into the dB - {}".format(e))
        sys.exit(0)


def is_date_format(date_text):
    try:
        datetime.strptime(date_text, "%m/%d/%Y").strftime('%m/%d/%Y')
        return True
    except ValueError:
        print("-> ERROR: Bad date format, use MM/DD/YYYY\n")
        return False


def is_time_format(time_text):
    try:
        if len(time_text) == 5:
            time.strptime(time_text, '%H:%M')
            return True
        else:
            print("-> ERROR: Bad time format, use HH:MM\n")
    except ValueError:
        print("-> ERROR: Bad time format, use HH:MM\n")
        return False


def menu():
    print("\nEnter information to schedule an appointment.\n"
          "Program assumes appointments end on the same day as start day.\n"
          "Enter start/end times in 24hour clock format.\n")

    while True:
        print("--- Enter a selection number ---")
        for i, e in enumerate(menu_items):
            for k, v in e.items():
                print('[{}] {}'.format(i + 1, k))

        choice = input("Enter number from menu >>: ").strip()
        if choice.isalnum():
            if choice <= str(len(menu_items)):
                for k, v, in menu_items[int(choice) - 1].items():
                    v()
        else:
            print("Please make a selection from the menu")


if __name__ == '__main__':
    menu_items = [
        {"Create a new appointment": create_appointment},
        {"Exit": exit}, ]
    database = "43v3.db"
    conn = create_connection(database)
    create_db(conn)
    menu()
    print()
