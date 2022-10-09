#!/usr/bin/python3
"""This script takes in the name of a state as an argument and lists all
`cities` of the state, using the database `hbtn_0e_0_usa`."""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    username, password, database_name, state_name = argv[1:]
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database_name)

    cursor = db.cursor()
    query = """SELECT cities.name
                FROM cities INNER JOIN states ON cities.state_id=states.id
                WHERE states.name=%s ORDER BY cities.id ASC
            """
    cursor.execute(query, (state_name,))
    row = cursor.fetchall()
    cities = []
    for city in row:
        cities.append(city[0])
    print(', '.join(cities))
 