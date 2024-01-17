-- create a user and then give him all the privileges
CREATE USER `user_0d_1` IDENTIFIED BY `user_0d_1_pwd`;
GRANT ALL PRIVILEGES ON * . * TO `user_0d_1`@`localhost`;
FLUSH PRIVILEGES;
