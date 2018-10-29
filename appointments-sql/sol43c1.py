#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('appointments.db')

c = conn.cursor()

query = '''SELECT * FROM Appointments ORDER BY starts_at'''

for one_row in c.execute(query):
    print(one_row)
