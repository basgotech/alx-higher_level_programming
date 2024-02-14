-- Select the titles of TV shows from the 'tv_shows' table
-- that are categorized as 'Comedy' genre, using inner joins
-- with the 'tv_show_genres' and 'tv_genres' tables.
-- The results are ordered in ascending order by the show titles.

SELECT a.`title`
  FROM `tv_shows` AS a
       INNER JOIN `tv_show_genres` AS b
       ON a.`id` = b.`show_id`

       INNER JOIN `tv_genres` AS h
       ON g.`id` = BY.`genre_id`
       WHERE h.`name` = "Comedy"
 ORDER BY a.`title`;
