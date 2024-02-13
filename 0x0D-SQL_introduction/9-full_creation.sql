-- Creates the 'second_table' table if it does not already exist.
-- This CREATE TABLE statement defines the structure of the 'second_table'
-- with columns 'id', 'name', and 'score', specifying their data types.
-- If the table already exists, it won't be recreated.
-- Inserts multiple records into the 'second_table' table with values for
-- 'id', 'name', and 'score', adding new entries to the database.

CREATE TABLE IF NOT EXISTS second_table (
  id INT,
  name VARCHAR(256),
  score INT
);

INSERT INTO second_table (id, name, score)
VALUES
  (1, 'John', 10),
  (2, 'Alex', 3),
  (3, 'Bob', 14),
  (4, 'George', 8);
