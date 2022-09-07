-- This script lists all records of table `second_table` of database `hbtn_0c_0` in MySQL server
-- Displays both score and name, and ordered by score in descending order
SELECT score, name FROM second_table WHERE score>=10 ORDER BY score DESC;
