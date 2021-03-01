-- groups second_table entries by score

SELECT `score`, COUNT(*) AS `number` FROM second_table GROUP BY `score` ORDER BY `number` DESC;