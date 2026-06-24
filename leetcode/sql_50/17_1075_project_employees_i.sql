-- LeetCode SQL 50 #17
-- Problem 1075. Project Employees I
-- Category: Basic Aggregate Functions
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
-- Write your PostgreSQL query statement below
SELECT t1.project_id, ROUND(AVG(t2.experience_years)::numeric, 2) AS average_years
FROM Project AS t1
LEFT JOIN Employee AS t2 ON t1.employee_id = t2.employee_id
GROUP BY t1.project_id
;