-- LeetCode SQL 50 #23
-- Problem 2356. Number of Unique Subjects Taught by Each Teacher
-- Category: Sorting and Grouping
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
-- Write your PostgreSQL query statement below
SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id
