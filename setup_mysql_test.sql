-- Create the database hbnb_test_db
-- Create the user hbnb_test with password hbnb_test_pwd
-- hbnb_test should have all the privileges on hbnb_test_db
-- hbnb_test should have SELECT privilege on performance_schema
-- check if the user and database exists

-- DATABASE hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Use the DATABASE
USE hbnb_test_db;

-- create the USER 
DROP USER IF EXISTS 'hbnb_test'@'localhost';
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- give the user privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- give the user privileges on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Reload the grant table by flushing the privileges
FLUSH PRIVILEGES;
