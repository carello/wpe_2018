#!/etc/bin/env python3

import sqlite3
from datetime import datetime
import sys
import os.path
import holidays
import arrow


def create_connection(db_file):
    exists = os.path.isfile(db_file)
    if exists:
        connected = sqlite3.connect(db_file)
        return connected
    else:
        print("Can't connect to database")
        sys.exit(0)


def view_date():
    sel_date = input("Enter date (MM/DD/YYY): ")
    if validate(sel_date):
        cur = conn.cursor()
        cur.execute("SELECT * FROM appointments WHERE date_start LIKE '{}%' "
                    "ORDER BY date_start ASC".format(sel_date))
        rows = cur.fetchall()

        if len(rows) == 0:
            print("\tNo appointments are scheduled for that date.")
        else:
            for row in rows:
                print(prn_template.format(row[2], row[3], row[1], row[4]))
                for country in the_holidays:
                    starts_at = arrow.get(row[2], 'MM/DD/YYYY HH:mm').date()
                    if starts_at in the_holidays[country]:
                        print('\t\t{} Holiday: {}'.format(country, the_holidays[country].get(starts_at)))
                print()
    else:
        print("Not a valid date or format, use MM/DD/YYYY\n")


def view_all():
    cur = conn.cursor()
    query = '''SELECT * FROM Appointments ORDER BY date_start ASC'''
    for row in cur.execute(query):
        print(prn_template.format(row[2], row[3], row[1], row[4]))
        for country in the_holidays:
            starts_at = arrow.get(row[2], 'MM/DD/YYYY HH:mm').date()
            if starts_at in the_holidays[country]:
                print('\t\t{} Holiday: {}'.format(country, the_holidays[country].get(starts_at)))
        print()


def validate(date_text):
    try:
        if date_text != datetime.strptime(date_text, "%m/%d/%Y").strftime('%m/%d/%Y'):
            raise ValueError
        return True
    except ValueError:
        return False


def menu():
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
        {"View all appointments": view_all},
        {"Enter a Date": view_date},
        {"Exit": exit}, ]

    database = "43v3.db"
    COUNTRIES = ['US', 'MX']
    the_holidays = {country: holidays.CountryHoliday(country) for country in COUNTRIES}
    prn_template = '\t START: {} - END: {} \n\t\tSUBJECT: {}\n\t\tCOMMENTS: {}'
    conn = create_connection(database)
    menu()
    print()
