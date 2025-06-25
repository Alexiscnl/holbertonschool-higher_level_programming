-- List all TV shows that have no genre linked
-- Display: tv_shows.title - tv_show_genres.genre_id
-- Uses one SELECT statement with a LEFT JOIN
-- Filters to include only rows where genre_id IS NULL
-- Results sorted by title (ASC), then genre_id (ASC)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
