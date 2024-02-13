-- Lists the number of records with the same score in the 'second_table' table
-- of the 'hbtn_0c_0' database.
-- This SELECT statement groups the records by score, counts the number of records
-- for each score, and displays the score along with the corresponding number of records.
-- The list is sorted in descending order by the number of records.

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC, score;
