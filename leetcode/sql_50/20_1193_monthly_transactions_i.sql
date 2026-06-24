-- LeetCode SQL 50 #20
-- Problem 1193. Monthly Transactions I
-- Category: Basic Aggregate Functions
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
-- Write your PostgreSQL query statement below
SELECT
    to_char(date_trunc('month', trans_date), 'YYYY-MM') AS month,
    country,
    COUNT(*) AS trans_count,
    COUNT(*) FILTER (WHERE "state" = 'approved') AS approved_count,
    SUM(amount) AS trans_total_amount,
    COALESCE(SUM(amount) FILTER (WHERE "state" = 'approved'), 0) AS approved_total_amount
FROM Transactions
GROUP BY date_trunc('month', trans_date), country
;
