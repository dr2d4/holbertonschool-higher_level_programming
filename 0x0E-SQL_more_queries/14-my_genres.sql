-- More select with join
SELECT tv_genres.name
FROM tv_shows
         INNER JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
         INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE title = 'Dexter'
ORDER BY tv_genres.name;
