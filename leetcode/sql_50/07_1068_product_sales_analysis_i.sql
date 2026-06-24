-- LeetCode SQL 50 #07
-- Problem 1068. Product Sales Analysis I
-- Category: Basic Joins
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
-- Write your PostgreSQL query statement below
SELECT t2.product_name, t1.year, t1.price
FROM Sales as t1
LEFT JOIN Product as t2 ON t1.product_id = t2.product_id
