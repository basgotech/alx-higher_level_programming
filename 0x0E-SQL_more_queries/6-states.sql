-- Create a database named 'hbtn_0d_usa' if it does not exist.
-- Within the 'hbtn_0d_usa' database, create a table named 'states' with the following structure:
-- - 'id' column as the primary key, an auto-incremented integer, and not nullable.
-- - 'name' column with a VARCHAR(256) datatype and not nullable.

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
    PRIMARY KEY(`id`),
    `id`   INT          NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL
);
