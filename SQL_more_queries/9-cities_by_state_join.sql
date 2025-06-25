-- List all cities with their corresponding state names
-- Using an INNER JOIN between `cities` and `states`
-- Sorted by cities.id in ascending order
-- Output format: cities.id - cities.name - states.name
-- Only one SELECT statement is used
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
ON cities.state_id = states.id;
