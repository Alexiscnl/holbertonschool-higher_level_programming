-- List all TV shows that belong to the genre 'Comedy'
-- Uses one SELECT statement with multiple JOINs
-- Links tv_shows to tv_genres via tv_show_genres
-- Filters by genre name = 'Comedy' (regardless of genre ID)
-- Results are sorted in ascending order by show title
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
