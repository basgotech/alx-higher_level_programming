#!/usr/bin/python3
""" SQL query to select states by name """
import MySQLdb
import sys


if __name__ == "__main__":
    my_db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    ftech = my_db.cursor()
    ftech.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    query = ftech.fetchall()
    for row in query:
        print(row)
    ftech.close()
    my_db.close()
