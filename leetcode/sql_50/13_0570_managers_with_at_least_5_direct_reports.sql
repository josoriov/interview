-- LeetCode SQL 50 #13
-- Problem 570. Managers with at Least 5 Direct Reports
-- Category: Basic Joins
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
-- Write your PostgreSQL query statement below
WITH reports_per_managerId AS (
    SELECT Employee.managerId, COUNT(Employee.id) as reports
    FROM Employee
    WHERE Employee.managerId is not null
    GROUP BY Employee.managerId
)

SELECT t1.name
FROM Employee as t1
LEFT JOIN reports_per_managerId as t2 ON t1.id = t2.managerId
WHERE t2.reports >= 5
;
