-- Create new user  with password ('user_0d_1': 'user_0d_1_pwd) and grant all privileges
CREATE USER IF NOT EXISTS `user_0d_2`@`localhost` IDENTIFIED BY 'user_0d_2_pwd';
GRANT ALL PRIVILEGES ON *.* TO `user_0d_1`@`localhost`;
FLUSH PRIVILEGES;

-- Create database hbtn_0d_2 if not exists
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
