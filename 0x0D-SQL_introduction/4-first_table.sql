--Creates a table named 'first_table' if it does not already exist.

--Table Structure:
--  - 'id': Integer field representing the identifier.
--  - 'name': Variable character field with a maximum length of 256 characters.

--  Note: This script ensures that the table is only created if it doesn't exist,
--  preventing any conflicts or errors.

CREATE TABLE IF NOT EXISTS first_table (
  id INT,
  name VARCHAR(256)
);

