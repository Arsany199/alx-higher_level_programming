--  lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT name, SUM(rate) AS rating
FROM tv_genres AS g
INNER JOIN tv_show_genres AS t
ON t.genre_id = g.id
INNER JOIN tv_show_rating AS r
ON r.show_id = t.show_id
GROUP BY name
ORDER BY rating DESC;
