-- Create a table named 'unique_id' if it does not exist.
-- The table has two columns: 'id' with a default value of 1 and marked as unique,
-- and 'name' with a VARCHAR(256) datatype.

CREATE TABLE IF NOT EXISTS `unique_id` (
    `id`   INT          DEFAULT 1 UNIQUE,
    `name` VARCHAR(256)
);
