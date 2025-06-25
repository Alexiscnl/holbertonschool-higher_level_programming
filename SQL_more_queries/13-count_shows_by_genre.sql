-- List all genres and the number of shows linked to each
-- Display: genre name - number of linked shows
-- Uses one SELECT statement with a JOIN and COUNT()
-- Only genres with at least one linked show are included
-- Results are grouped by genre name and sorted by number_of_shows in descending order
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;

