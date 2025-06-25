-- List all TV shows that have at least one genre linked
-- Display: tv_shows.title - tv_show_genres.genre_id
-- Uses one SELECT statement with an INNER JOIN
-- Results are sorted by tv_shows.title (ASC), then by genre_id (ASC)
-- Only shows with at least one genre are included
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
