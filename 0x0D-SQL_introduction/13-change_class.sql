-- Removes all records from the 'second_table' table in the 'hbtn_0c_0' database
-- where the 'score' is less than or equal to 5.
-- This DELETE statement removes records from the 'second_table' table where the
-- 'score' column is less than or equal to 5.
-- Note: Exercise caution when using DELETE statements, as they permanently remove
-- records from the specified table.

DELETE FROM hbtn_0c_0.second_table WHERE score <= 5;
