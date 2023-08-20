-- Lists all genres of the show Dexter.
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT tg.`name`     AS `name`
    FROM `tv_genres` AS tg
        INNER JOIN `tv_show_genres` AS tsg ON tg.`id` = tsg.`genre_id`
        INNER JOIN `tv_shows`       AS ts  ON ts.`id` = tsg.`show_id`
    WHERE ts.`title` = "Dexter"
    ORDER BY `name`;

