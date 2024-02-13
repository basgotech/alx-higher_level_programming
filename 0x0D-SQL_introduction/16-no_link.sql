-- Lists all records of the 'second_table' table in the 'hbtn_0c_0' database.
-- This SELECT statement retrieves records where the 'name' column is not NULL,
-- displaying the 'score' and 'name' columns. The results are ordered by descending
-- score.

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
