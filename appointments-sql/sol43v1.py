#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('appointments.db')

with conn:
    c = conn.cursor()

    title = input("Enter title: ")
    starts_at = input("Enter starting timestamp: ")
    ends_at = input("Enter ending timestamp: ")
    comment = input("Enter comment: ")

    c.execute('''INSERT INTO Appointments 
    (title, starts_at, ends_at, comment) 
    VALUES (?,?,?,?)''', (title, starts_at, ends_at, comment))

