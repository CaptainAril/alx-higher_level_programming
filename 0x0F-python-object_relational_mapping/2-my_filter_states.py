#!/usr/bin/python3
"""This module takes in argument and displays all values in `states`
table of `hbtn_0e_0_usa` where `name` matches the argument.
"""


import sys
import MySQLdb


if __name__ == "__main__":
    username, password, database_name, state_name = sys.argv[1:]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = BIANRY '{}' ORDER BY id ASC"\
        .format(state_name)
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
