-- Specify the database name as an argument

-- List all cities with corresponding state names using JOIN method
SELECT cities.id, cities.name, states.name AS state_name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
