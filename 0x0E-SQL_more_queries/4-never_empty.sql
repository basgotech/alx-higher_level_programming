-- Specify the database name as an argument when running the script grapp
USE `your_database`;

-- Create the id_not_null table if it does not exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
