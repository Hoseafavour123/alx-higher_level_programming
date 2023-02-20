-- List records with a name value from second_table in hbtn_0c_0

SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
