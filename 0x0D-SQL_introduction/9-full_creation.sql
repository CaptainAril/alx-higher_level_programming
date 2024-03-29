-- This script creates a table `second_table` in the database `hbtn_0c_0` in MySQL server.
-- If table already exists, script should not fail
-- Use of SELECT and SHOW statements not allowed
-- second_table description:
--     *  id INT
--     *  name VARCHAR(256)
--     *  score INT
--  row records:
--     *  1, "John", 10
--     *  2, "Alex", 3
--     *  3, "Bob", 14
--     *  4, "George", 8
CREATE TABLE IF NOT EXISTS second_table (
       id INT,
       name VARCHAR(256),
       score INT
       ) ;
INSERT INTO second_table (id, name, score)
VALUES
       (1, "John", 10),
       (2, "Alex", 3),
       (3, "Bob", 14),
       (4, "George", 8) ;
