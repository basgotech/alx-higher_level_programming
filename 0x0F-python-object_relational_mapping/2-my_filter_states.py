#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    """ Creating a cursor object """
    cursor = db.cursor()

    """ SQL query to select states by name """
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    
    """ Executing the query """
    cursor.execute(query, (sys.argv[4],))

    """ Fetching and displaying the results """
    results = cursor.fetchall()
    for row in results:
        print(row)

    """ Closing cursor and connection """
    cursor.close()
    db.close()
