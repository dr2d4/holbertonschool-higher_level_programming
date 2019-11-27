-- More select with join
SELECT tg.name, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_show_genres
         LEFT JOIN tv_genres tg ON tv_show_genres.genre_id = tg.id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
