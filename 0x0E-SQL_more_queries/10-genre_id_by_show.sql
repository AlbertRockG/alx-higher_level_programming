-- Lists all shows contained in hbtn_0d_tvshows
SELECT ts.`title`, tsg.`genre_id`
    FROM `tv_shows` AS ts
        INNER JOIN `tv_show_genres` AS tsg
        ON `show_id`
    WHERE ts.`id` = tsg.`show_id`
    ORDER BY ts.`title` ASC, tsg.`genre_id`;
