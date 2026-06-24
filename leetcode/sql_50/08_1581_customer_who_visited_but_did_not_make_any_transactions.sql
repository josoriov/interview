-- LeetCode SQL 50 #08
-- Problem 1581. Customer Who Visited but Did Not Make Any Transactions
-- Category: Basic Joins
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
-- Write your PostgreSQL query statement below
WITH visit_count AS (
    SELECT t1.visit_id, COUNT(t2.transaction_id) as transactions
    FROM Visits t1
    LEFT JOIN Transactions as t2 ON t1.visit_id = t2.visit_id
    GROUP BY t1.visit_id
)

SELECT t3.customer_id, COUNT(t4.visit_id) as count_no_trans
FROM Visits as t3
LEFT JOIN visit_count as t4 ON t3.visit_id = t4.visit_id
WHERE t4.transactions = 0
GROUP BY t3.customer_id
;
