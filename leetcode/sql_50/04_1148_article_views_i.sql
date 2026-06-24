-- LeetCode SQL 50 #04
-- Problem 1148. Article Views I
-- Category: Select
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
-- Write your PostgreSQL query statement below
select distinct(t1.author_id) as id
from Views as t1
where t1.author_id = t1.viewer_id
order by t1.author_id asc
