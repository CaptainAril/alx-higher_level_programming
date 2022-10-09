#!/usr/bin/python3
"""This script lists all `cities` from the datatbase `hbtn_0e_0_usa`."""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    username, password, database_name = argv[1:]

    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database_name)
    cursor = db.cursor()

    query = """SELECT cities.id, cities.name, states.name
                FROM cities INNER JOIN states ON cities.state_id=states.id
                ORDER BY states.id ASC
                    """
    cursor.execute(query)

    cities = cursor.fetchall()
    for city in cities:
        print(city)

    cursor.close()
    db.close()
