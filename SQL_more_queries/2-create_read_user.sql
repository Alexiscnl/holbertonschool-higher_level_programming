-- Create DB and user_0d_2 with read-only access
CREATE DATABASE IF NOT EXISTS hbtb_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbnb_0d_2.* TO 'user_0d_2'@'localhost';
