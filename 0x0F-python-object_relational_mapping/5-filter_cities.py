#!/usr/bin/python3
"""script that takes in the name of a state as an argument
and lists all cities of that state"""
import MySQLdb
from sys import argv


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    c = db.cursor()
    c.execute("SELECT * FROM cities as c \
                INNER JOIN states as s \
                   ON c.state_id = s.id \
                ORDER BY c.id")

    rows = c.fetchall()
    for i in rows:
       j.append(i[1])
    print(", ".join(j))

    c.close()
    db.close()
