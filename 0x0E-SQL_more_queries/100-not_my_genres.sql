-- Specify the database name as an argument when running the script
USE your_database;

-- Get all genres
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN (
    -- Get genres linked to Dexter
    SELECT tv_genres.id
    FROM tv_shows
    JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
    JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name ASC;
