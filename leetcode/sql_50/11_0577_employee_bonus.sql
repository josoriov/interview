-- LeetCode SQL 50 #11
-- Problem 577. Employee Bonus
-- Category: Basic Joins
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
-- Write your PostgreSQL query statement below
SELECT t1.name, t2.bonus
FROM Employee as t1
LEFT JOIN Bonus as t2 ON t1.empId = t2.empId
WHERE t2.bonus IS NULL or t2.bonus < 1000
;
