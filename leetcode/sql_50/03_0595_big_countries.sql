-- LeetCode SQL 50 #03
-- Problem 595. Big Countries
-- Category: Select
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
-- Write your PostgreSQL query statement below
select t1.name, t1.population, t1.area
from World as t1
where t1.area >= 3000000 or t1.population >= 25000000;
