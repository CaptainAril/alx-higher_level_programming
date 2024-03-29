-- This script lists the number of records with the same score in table `second_table
-- The result shold display:
--     * the score
--     * the number of records for this score with the label number
-- The list should be sorted by number of records (descending)
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
