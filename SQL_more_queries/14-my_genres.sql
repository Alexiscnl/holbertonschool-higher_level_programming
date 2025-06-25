-- List all genres linked to the TV show 'Dexter'
-- Uses one SELECT statement with multiple JOINs
-- Relates tv_shows to tv_genres through tv_show_genres
-- Filters by title = 'Dexter' (regardless of its ID)
-- Results are sorted in ascending order by genre name
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
