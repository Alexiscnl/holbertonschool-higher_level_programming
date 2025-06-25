-- List all TV show titles that belong to the genre 'Comedy'
-- Uses one SELECT statement with multiple JOINs
-- Relates tv_shows to tv_genres through tv_show_genres
-- Filters by genre name = 'Comedy' (ID may vary)
-- Results are sorted by tv_shows.title in ascending order
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
