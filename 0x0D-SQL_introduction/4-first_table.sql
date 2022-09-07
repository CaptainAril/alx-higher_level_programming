-- This script creates a table `first_table` in the current database
-- first_table description:
--   *  id INT
--   *  name VARCHAR(256)
-- if table already exists, script should not fail
-- Use of SELECT and SHOW statements not allowed
CREATE TABLE IF NOT EXISTS first_table (
       id INT,
       name VARCHAR(256)
       ) ;
