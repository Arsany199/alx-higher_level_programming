#!/usr/bin/python3
"""script that lists all cities from the database"""
import MySQLdb
from sys import argv


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM cities\
              INNER JOIN states ON cities.state_id = states.id\
              ORDER BY cities.id")

    rows = c.fetchall()
    for i in rows:
        print(i)

    c.close()
    db.close()
