#!/usr/bin/python3
"""  lists all data from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    query = db.cursor()
    query.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    fetch = query.fetchall()
    for data in fetch:
        print(data)
    query.close()
    db.close()
