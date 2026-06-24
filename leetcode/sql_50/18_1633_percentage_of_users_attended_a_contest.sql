-- LeetCode SQL 50 #18
-- Problem 1633. Percentage of Users Attended a Contest
-- Category: Basic Aggregate Functions
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
# Write your MySQL query statement below
WITH total_users AS (
    SELECT COUNT(DISTINCT user_id) AS users_total
    FROM Users
), users_per_contest AS (
    SELECT contest_id, COUNT(user_id) AS users
    FROM Register
    GROUP BY contest_id
)

SELECT t1.contest_id, ROUND((t1.users / t2.users_total)*100, 2) AS percentage
FROM users_per_contest AS t1
CROSS JOIN total_users AS t2
ORDER BY percentage DESC, t1.contest_id ASC
;
