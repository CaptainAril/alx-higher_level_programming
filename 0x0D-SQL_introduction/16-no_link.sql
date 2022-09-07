-- This script lists all records of table `second_table` in MySQL server
-- Don't list rows without a name vallue
-- Result should display in order score and name; ordered by score (descending)
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
