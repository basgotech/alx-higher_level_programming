-- List all shows without the genre 'Comedy'
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
    SELECT tv_shows.id
    FROM tv_show_genres
    JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
    WHERE tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title ASC;
