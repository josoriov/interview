-- LeetCode SQL 50 #21
-- Problem 1174. Immediate Food Delivery II
-- Category: Basic Aggregate Functions
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
-- Write your PostgreSQL query statement below
WITH first_orders as (
    SELECT customer_id, MIN(order_date) as first_order
    FROM Delivery
    GROUP BY customer_id
),
immediate_orders as (
    SELECT t1.customer_id, 
        CASE
            WHEN t1.first_order = t2.customer_pref_delivery_date THEN 1
            ELSE 0
        END AS is_immediate
    FROM first_orders as t1
    LEFT JOIN Delivery as t2 ON t1.customer_id = t2.customer_id AND t1.first_order = t2.order_date
)

SELECT ROUND(100.0*SUM(is_immediate)::numeric/COUNT(is_immediate)::numeric, 2) immediate_percentage 
FROM immediate_orders
;
