--- CReate the database hbnb_dev_db
--- Create the user hbnb_dev with password hbnb_dev_pwd
--- hbnb_dev should have all the privileges on hbnb_dev_db
--- hbnb_dev should have SELECT privilege on performance_schema
--- check if the user and database exists

--- DATABASE hbnb_dev_db
CREATE IF NOT EXISTS DATABASE hbnb_dev_db;

--- Use the DATABASE
USE hbnb_dev_db;

--- create the USER 
CREATE IF NOT EXISTS USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

--- give the user privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

--- give the user privileges on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
