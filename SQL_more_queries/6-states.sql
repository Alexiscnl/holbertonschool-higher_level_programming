-- This script creates the database hbtn_0d_usa and the table states.
-- The table states contains an auto-incremented primary key `id` and a non-null `name`.
CREATE DATABASE IF NOT EXISTS hbtb_0d_usa;
USE hbtb_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT NOT NULL AUTO_INCREMENT  PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
