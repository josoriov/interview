-- LeetCode SQL 50 #16
-- Problem 1251. Average Selling Price
-- Category: Basic Aggregate Functions
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
-- Write your PostgreSQL query statement below
WITH sale_prices AS
(
    SELECT t1.*, t2.price, t2.start_date, t2.end_date, (t1.units * t2.price) AS sale_total
    FROM UnitsSold AS t1
    LEFT JOIN Prices AS t2 ON t1.product_id = t2.product_id AND t1.purchase_date BETWEEN t2.start_date AND t2.end_date
), sale_average AS (
    SELECT t3.product_id, SUM(t3.units)::numeric AS units, SUM(t3.sale_total)::numeric AS sale_total
    FROM sale_prices AS t3
    GROUP BY t3.product_id
), products AS (
    SELECT DISTINCT(product_id) AS product_id
    FROM Prices
)

SELECT t4.product_id, COALESCE(ROUND(t5.sale_total / t5.units, 2), 0) AS average_price
FROM products AS t4
LEFT JOIN sale_average AS t5 ON t4.product_id = t5.product_id
;
