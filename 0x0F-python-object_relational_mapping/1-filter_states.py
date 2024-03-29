#!/usr/bin/python3
"""  lists all attribute from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3], port=3306)
    fetch = database.cursor()
    fetch.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    query = fetch.fetchall()
    for rows in query:
        print(rows)
    fetch.close()
    database.close()
