-- Create database/table (hbtn_0d_usa/states)
CREATE DATABASE hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE states (id INT UNIQUE KEY AUTO_INCREMENT NOT NULL PRIMARY KEY , name VARCHAR(256) NOT NULL);
