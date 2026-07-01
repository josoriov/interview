-- LeetCode SQL 50 #22
-- Problem 550. Game Play Analysis IV
-- Category: Basic Aggregate Functions
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
-- Write your PostgreSQL query statement below
WITH day_after_first_login AS (
    SELECT player_id, MIN(event_date) + INTERVAL '1 DAY' AS day_after
    FROM Activity
    GROUP BY player_id
)

SELECT ROUND(COUNT(t2.player_id)::numeric / COUNT(DISTINCT t1.player_id)::numeric, 2) AS fraction
FROM Activity as t1
LEFT JOIN day_after_first_login as t2 ON t1.player_id = t2.player_id AND t1.event_date = t2.day_after