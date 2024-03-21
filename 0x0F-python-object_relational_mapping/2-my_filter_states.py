#!/usr/bin/python3
"""  SQL query to select states by name """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cu = db.cursor()
    cu.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    query = cu.fetchall()
    for row in query:
        print(row)
    cu.close()
    db.close()
