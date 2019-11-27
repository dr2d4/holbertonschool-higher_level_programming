-- More select with join and sub select
SELECT name
FROM tv_genres
WHERE id NOT IN (SELECT TSG.genre_id
                 FROM tv_shows
                          INNER JOIN tv_show_genres TSG ON tv_shows.id = TSG.show_id
                 WHERE tv_shows.title = "Dexter")
ORDER BY name;
