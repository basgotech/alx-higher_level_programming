import MySQLdb
import sys

def list_states(username, password, database):
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database)

        # Create a cursor object
        cursor = db.cursor()

        # Execute the SQL query
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

        # Fetch all the rows
        states = cursor.fetchall()

        # Print the results
        for state in states:
            print(state)

        # Close the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)
