-- LeetCode SQL 50 #25
-- Problem 1070. Product Sales Analysis III
-- Category: Sorting and Grouping
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
-- Write your PostgreSQL query statement below
WITH earliest_year AS (
    SELECT product_id, MIN(year) as year, MIN(price) as price
    FROM Sales
    GROUP BY product_id
)

SELECT t1.product_id, t1.year as first_year, sum(t2.quantity) as quantity, t1.price
FROM earliest_year as t1
INNER JOIN Sales t2 ON t1.product_id = t2.product_id AND t1.year = t2.year
GROUP BY t1.product_id, t1.year, t1.price