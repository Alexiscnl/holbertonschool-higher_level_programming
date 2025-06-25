-- List all TV shows with their genre ID (or NULL if no genre linked)
-- Display: tv_shows.title - tv_show_genres.genre_id
-- Uses one SELECT statement with a LEFT JOIN
-- Ensures shows with no genre are included (genre_id = NULL)
-- Results sorted by title (ASC), then genre_id (ASC)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
