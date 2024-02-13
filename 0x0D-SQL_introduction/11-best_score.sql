-- Retrieves the 'score' and 'name' columns from the 'second_table' table
-- where the 'score' is greater than or equal to 10, and orders the result set
-- in descending order based on the 'score' column.
-- This SELECT statement filters the rows in the 'second_table' table to
-- include only those with a 'score' greater than or equal to 10. The result
-- set is then ordered in descending order based on the values in the 'score'
-- column.

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
