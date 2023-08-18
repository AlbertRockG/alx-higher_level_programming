-- Creates the MySQL server user user_0d_1.
-- Grant all privileges to user_0d_1.
-- Its password should be user_0d_1_pwd.
-- The creation should not fail if the user already exists.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
