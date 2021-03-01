-- list all records in second_table only if they have a name

SELECT `score`, `name` FROM second_table WHERE `name` IS NOT NULL and `name` != "" ORDER BY `score` DESC;