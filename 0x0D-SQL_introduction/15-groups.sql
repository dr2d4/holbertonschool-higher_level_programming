-- Select - count, group and sort desc
SELECT score, count(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;
