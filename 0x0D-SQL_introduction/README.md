0x0D. SQL - Introduction
SQL

##
Files
0-list_databases.sql
##
Description: Lists all databases of your MySQL server.
Usage:
bash
Copy code
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
1-create_database_if_missing.sql
##
Description: Creates the database hbtn_0c_0 in your MySQL server if it doesn't exist.
Usage:
bash
Copy code
cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
2-remove_database.sql
##
Description: Deletes the database hbtn_0c_0 from your MySQL server if it exists.
Usage:
bash
Copy code
cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
3-list_tables.sql

Description: Lists all tables of a specified database in your MySQL server.
Usage:
bash
Copy code
cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
4-first_table.sql

Description: Creates a table called first_table in the specified database in your MySQL server.
Usage:
bash
Copy code
cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
5-full_table.sql

Description: Prints the full description of the table first_table from the specified database in your MySQL server.
Usage:
bash
Copy code
cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
6-list_values.sql

Description: Lists all rows of the table first_table from the specified database in your MySQL server.
Usage:
bash
Copy code
cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
7-insert_value.sql

Description: Inserts a new row with id=89 and name='Best School' into the table first_table in the specified database in your MySQL server.
Usage:
bash
Copy code
cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
8-count_89.sql

Description: Displays the number of records with id=89 in the table first_table of the specified database in your MySQL server.
Usage:
bash
Copy code
cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
9-full_creation.sql

Description: Creates a table called second_table in the specified database in your MySQL server and adds multiple rows.
Usage:
bash
Copy code
cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
10-top_score.sql

Description: Lists all records of the table second_table from the specified database in your MySQL server, ordered by score (top first).
Usage:
bash
Copy code
cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
11-best_score.sql

Description: Lists all records with a score >= 10 in the table second_table from the specified database in your MySQL server, ordered by score (top first).
Usage:
bash
Copy code
cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
12-no_cheating.sql

Description: Updates the score of Bob to 10 in the table second_table without using Bob's id, only the name field.
Usage:
bash
Copy code
cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
13-change_class.sql

Description: Removes all records with a score <= 5 in the table second_table from the specified database in your MySQL server.
Usage:
bash
Copy code
cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
14-average.sql

Description: Computes the score average of all records in the table second_table from the specified database in your MySQL server.
Usage:
bash
Copy code
cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
15-groups.sql

Description: Lists the number of records with the same score in the table second_table from the specified database in your MySQL server, sorted by the number of records (descending).
Usage:
bash
Copy code
cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
16-no_link.sql

Description: Lists all records of the table second_table from the specified database in your MySQL server, excluding rows without a name value, ordered by descending score.
Usage:
bash
Copy code
cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Author
Basliel Tegegn


