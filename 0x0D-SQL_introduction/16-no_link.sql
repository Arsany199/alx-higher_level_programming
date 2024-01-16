-- list all rec. if the name doesn't exist skip it
SELECT score, name
FROM second_table
WHERE name!=""
ORDER BY score DESC;
