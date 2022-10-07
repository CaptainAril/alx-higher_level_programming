#!/usr/bin/python3
"""Python script that lists all `states` from the database `hbtn_0e_0_usa`."""


import sys
import MySQLdb


if __name__ == "__main__":
    username, password, database_name = sys.argv[1:]

    db = MySQLdb.connect(
        host="localhost", port=3306, user=username,
        passwd=password, db=database_name)

    cursor = db.cursor()
    sql = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(sql)
    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
