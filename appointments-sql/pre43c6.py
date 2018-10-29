#!/etc/bin/env python3

import sqlite3
from datetime import datetime
import sys
import os.path

database = "43v3.db"


def create_connection(db_file):
    exists = os.path.isfile(database)
    if exists:
        connected = sqlite3.connect(db_file)
        return connected
    else:
        print("Can't connect to database")
        sys.exit(0)


def view_db(connection, date_view):
    cur = connection.cursor()
    cur.execute("SELECT * FROM appointments WHERE date_start LIKE '{}%' ORDER BY date_start ASC".format(date_view))
    rows = cur.fetchall()

    if len(rows) == 0:
        print("\tNo appointments are scheduled for that date.")
    else:
        for row in rows:
            print('\t START: {} - END: {}, \n\t\tSUBJECT: {}\n\t\tCOMMENTS: {}'
                  .format(row[2], row[3], row[1], row[4]))


def validate(date_text):
    try:
        if date_text != datetime.strptime(date_text, "%m/%d/%Y").strftime('%m/%d/%Y'):
            raise ValueError
        return True
    except ValueError:
        return False


def view(connection):
    while True:
        sel_date = input("Enter a date to view (format: MM/DD/YYYY), or Q to exit ->: ").lower()
        if sel_date == 'q':
            break

        if validate(sel_date):
            view_db(connection, sel_date)
            print()
        else:
            print('Bad date, please enter as: MM/DD/YYYY')


if __name__ == '__main__':
    conn = create_connection(database)
    view(conn)
    print()
