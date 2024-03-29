-- Lists all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT DISTINCT tg.`name`
    FROM `tv_genres` AS tg
        LEFT JOIN `tv_show_genres` AS tsg
        ON tg.`id` = tsg.`genre_id`
        LEFT JOIN `tv_shows` AS ts
        ON ts.`id` = tsg.`show_id`
        WHERE tg.`name` NOT IN (SELECT tg.`name`
                                    FROM `tv_genres` AS tg
                                        INNER JOIN `tv_show_genres` AS tsg
                                        ON tg.`id` = tsg.`genre_id`
                                        INNER JOIN `tv_shows` AS ts
                                        ON ts.`id` = tsg.`show_id`
                                        WHERE ts.`title` = "Dexter")
    ORDER BY tg.`name`;
