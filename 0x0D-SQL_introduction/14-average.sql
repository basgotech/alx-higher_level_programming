-- Computes the average score of all records in the 'second_table' table
-- from the 'hbtn_0c_0' database.
-- This SELECT statement calculates the average score using the AVG() function.
-- The result is assigned the column name 'average'.
-- Note: Replace 'hbtn_0c_0' with the actual name of your database.

SELECT AVG(score) AS average FROM second_table;
