#!/usr/bin/python3
"""This script lists all `cities` that matches the name passed
from the database `hbtn_0e_0_usa`"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    query = "SELECT cities.name FROM cities join states ON cities.state_id =\
        states.id WHERE states.name = %s ORDER BY cities.id ASC"
    cursor.execute(query, (argv[4],))
    cities = cursor.fetchall()
    citiesList = []
    for city in cities:
        citiesList.append(city[0])
    print(', '.join(citiesList))
    cursor.close()
    db.close()
