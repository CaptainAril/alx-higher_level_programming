#!/usr/bin/python3
"""This script lists all `states` that matches the name passed
from the database `hbtn_0e_0_usa`"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    query = "SELECT cities.id, cities.name, states.name FROM states\
        join cities ON cities.state_id = states.id ORDER BY cities.id ASC"
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
