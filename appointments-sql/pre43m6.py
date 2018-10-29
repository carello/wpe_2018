#!/etc/bin/env python3

import sqlite3
from sqlite3 import Error
import time
from datetime import datetime
import sys

database = "43v3.db"


def create_connection(db_file):
    try:
        connected = sqlite3.connect(db_file)
        return connected
    except Error as e:
        print(e)
        print("Unable to create db connection")
        sys.exit(0)


def create_table(connection, create_table_sql):
    try:
        c = connection.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        print("Unable to create table")
        sys.exit(0)


def create_db(connection):
    sql_create_projects_appointments = """ CREATE TABLE IF NOT EXISTS appointments (
                                        id integer PRIMARY KEY,
                                        title text,
                                        date_start text,
                                        end_time text,
                                        comment text
                                    ); """

    try:
        create_table(connection, sql_create_projects_appointments)
    except Error as e:
        print(e)
        print("Cannot create the database connection.")
        sys.exit(0)


def insert_data(connection, request):
    sql = ''' INSERT INTO appointments(title, date_start, end_time, comment)
                         VALUES(?,?,?,?) '''
    #sql = "INSERT INTO appointments VALUES(null, '{}', '{}', '{}', '{}')".format(*request)
    try:
        cur = connection.cursor()
        cur.execute(sql, request)
        connection.commit()
    except Error as e:
        print(e)
        print("Unable to add data to the db")
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


def menu(connection):
    print("Enter information to schedule an appointment.\n"
          "Program assumes appointments end on the same day as start day.\n"
          "Enter start/end times in 24hour clock format.\n")

    while True:
        status = input("Enter: M to make an appointment, or Q to exit ->: ").lower()
        if status == 'q':
            break

        else:
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

            notes = input("\tEnter any notes for the meeting ->: ").strip()
            date_start = ' '.join((date, start))
            request = (title, date_start, end, notes)
            insert_data(connection, request)
            print("-> Meeting is scheduled\n")


if __name__ == '__main__':
    conn = create_connection(database)
    create_db(conn)
    menu(conn)
    print()
