-- LeetCode SQL 50 #02
-- Problem 584. Find Customer Referee
-- Category: Select
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
-- Write your PostgreSQL query statement below
select "name"
from Customer
where referee_id <> 2 or referee_id is null;
