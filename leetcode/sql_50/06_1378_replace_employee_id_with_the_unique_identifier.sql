-- LeetCode SQL 50 #06
-- Problem 1378. Replace Employee ID With The Unique Identifier
-- Category: Basic Joins
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
-- Write your PostgreSQL query statement below
select t2.unique_id, t1.name
from Employees as t1
left join EmployeeUNI as t2
    on t1.id = t2.id
;
