#!/usr/bin/python3
"""Script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument."""
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL database
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    # Create a cursor object using cursor() method
    cur = conn.cursor()

    # Construct the query with a parameterized query to avoid SQL injection
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"

    # Execute the query with the parameter as a tuple
    cur.execute(query, (sys.argv[4],))

    # Fetch all the rows and print them
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    conn.close()
