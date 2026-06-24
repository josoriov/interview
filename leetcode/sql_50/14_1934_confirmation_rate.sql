-- LeetCode SQL 50 #14
-- Problem 1934. Confirmation Rate
-- Category: Basic Joins
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
-- Write your PostgreSQL query statement below
WITH total_messages AS (
    SELECT user_id, COUNT(1) AS total_messages
    FROM Confirmations
    GROUP BY user_id
), confirmed_messages AS (
    SELECT user_id, COUNT(1) AS confirmed_messages
    FROM Confirmations
    WHERE action = 'confirmed'
    GROUP BY user_id
)

SELECT
    t1.user_id,
    ROUND(COALESCE(t3.confirmed_messages, 0)::numeric / COALESCE(t2.total_messages, 1)::numeric, 2) AS confirmation_rate
FROM Signups AS t1
LEFT JOIN total_messages AS t2 ON t1.user_id = t2.user_id
LEFT JOIN confirmed_messages AS t3 ON t1.user_id = t3.user_id
;

