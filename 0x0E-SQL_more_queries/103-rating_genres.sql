-- Specify the database name as an argument when running the script
USE hbtn_0d_tvshows_rate;

-- List all genres along with their rating sums
SELECT tv_genres.name, SUM(ratings.rating) AS rating_sum
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
JOIN ratings ON tv_shows.id = ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;

