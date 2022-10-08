#!/usr/bin/python3
"""Python script that lists all `states` from the database `hbtn_0e_
"""


import MySQLdb
import sys


if __name__ == "__main__":
    username, password, database_name = sys.argv[1:]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        if state[1][0] == 'N':
            print(state)

    cursor.close()
    db.close()
