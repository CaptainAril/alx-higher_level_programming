-- This script converts database `hbtn_0c_0` to UTF*(utf8mb4, collate utf8mb4_unicode_ci) in MySQL server
-- Convert all the following to UTF8:
-- 	   * Database hbtn_0c_0
-- 	   * Table first_table
--	   * Field name in first_table
USE `hbtn_0c_0`
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
