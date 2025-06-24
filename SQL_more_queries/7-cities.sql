-- This script creates the database hbnb_0d_usa and the table cities.
-- The table cities includes an auto-incremented id (PRIMARY KEY),
-- a state_id that references the id of the states table (FOREIGN KEY),
-- and a non-null name column.
CREATE DATABASE IF NOT EXISTS hbtb_0d_usa;
CREATE TABLE IF NOT EXISTS hbnb_0d_usa.cities(
	id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES hbnb_0d_usa.states(id)
);
