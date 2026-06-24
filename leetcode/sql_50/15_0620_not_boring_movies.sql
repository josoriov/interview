-- LeetCode SQL 50 #15
-- Problem 620. Not Boring Movies
-- Category: Basic Aggregate Functions
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
-- Write your PostgreSQL query statement below
SELECT *
FROM Cinema
WHERE description <> 'boring' AND id % 2 = 1
ORDER BY rating DESC
;
