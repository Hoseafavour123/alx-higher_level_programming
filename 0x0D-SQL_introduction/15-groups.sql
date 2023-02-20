-- List the number of records with the same score on second table in hbtn_0c_c
-- database

SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score
ORDER BY score DESC;
