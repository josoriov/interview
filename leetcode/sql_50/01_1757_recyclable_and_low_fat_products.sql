-- LeetCode SQL 50 #01
-- Problem 1757. Recyclable and Low Fat Products
-- Category: Select
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
-- Write your PostgreSQL query statement below
select product_id
from Products
where low_fats = 'Y' and recyclable = 'Y
