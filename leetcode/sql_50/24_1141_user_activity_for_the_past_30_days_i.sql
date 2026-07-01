-- LeetCode SQL 50 #24
-- Problem 1141. User Activity for the Past 30 Days I
-- Category: Sorting and Grouping
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
-- Write your PostgreSQL query statement below
WITH params AS (
  SELECT
    DATE '2019-07-27' AS end_date,
    DATE '2019-07-27' - 29 AS start_date
)
SELECT activity_date AS day, COUNT(DISTINCT user_id) as active_users
FROM Activity
WHERE activity_date BETWEEN
  (SELECT start_date FROM params)
  AND
  (SELECT end_date FROM params)
GROUP BY activity_date