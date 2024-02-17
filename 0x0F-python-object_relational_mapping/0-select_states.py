#!/usr/bin/python3
""" Script that lists all states from the database"""
import MySQLdb
import sys


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    c = db.cursor()
    c.execute("SELECT * FROM states")

    rows = c.fetchall()
    for i in rows:
        print(i)
    c.close()
    db.close()
