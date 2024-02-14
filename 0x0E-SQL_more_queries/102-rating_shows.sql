-- Specify the database name as an argument when running the script
USE hbtn_0d_tvshows_rate;

-- List all shows along with their rating sums
SELECT tv_shows.title, SUM(ratings.rating) AS rating_sum
FROM tv_shows
JOIN ratings ON tv_shows.id = ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;

