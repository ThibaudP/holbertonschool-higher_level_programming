-- display the top 3 city temperatures in july and august

SELECT `city`, AVG(`value`) AS `avg_temp` FROM `temperatures` WHERE `month` BETWEEN 7 AND 8 GROUP BY `city` ORDER BY `avg_temp` DESC LIMIT 3;