#!/usr/bin/python3
"""Script that takes in an argument and displays all values
in the states table but safe from mySQL injections"""
import MySQLdb
from sys import argv


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    c = db.cursor()
    c.execute("SELECT * FROM states WHERE BINARY name = %s".format(argv[4]))

    rows = c.fetchall()
    for i in rows:
        print(i)

    c.close()
    db.close()
