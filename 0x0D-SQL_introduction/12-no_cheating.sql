-- Updates the 'score' of the record with the name 'Bob' to 10 in the 'second_table' table.
-- This UPDATE statement modifies the 'score' column for the record in the 'second_table'
-- table where the 'name' is 'Bob', setting the 'score' to 10.
-- Note: The script assumes that the 'name' column is unique, and it updates the first
-- occurrence of 'Bob' found in the 'second_table' table.

UPDATE second_table SET score = 10 WHERE name = 'Bob';
