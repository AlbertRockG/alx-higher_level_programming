-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT tg.`name`, SUM(tsr.`rate`) AS `rating`
    FROM `tv_genres` AS tg
        INNER JOIN `tv_show_genres` AS tsg
        ON tsg.`genre_id` = tg.`id`
        INNER JOIN `tv_show_ratings` AS tsr
        ON tsg.`show_id` = tsr.`show_id`
    GROUP BY tg.`name`
    ORDER BY `rating` DESC;
