#!/usr/bin/python3
"""script that list all the states from a database"""

import sys
import MySQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states")

    rows = c.fetchall()
    for stat in row:
        print(stat)

    c.close()
    db.close()
