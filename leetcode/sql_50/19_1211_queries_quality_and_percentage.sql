-- LeetCode SQL 50 #19
-- Problem 1211. Queries Quality and Percentage
-- Category: Basic Aggregate Functions
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
-- Write your PostgreSQL query statement below
-- quality = ( sum(rating / position) ) / total_n
-- poor_query_percentage = ( rating_lees_than_3 / total_n ) * 100
WITH total_per_name AS (
    SELECT query_name, COUNT(1) AS total
    FROM Queries
    GROUP BY query_name
), poor_queries AS (
    SELECT query_name, COUNT(1) AS poor_total
    FROM Queries
    WHERE rating < 3
    GROUP BY query_name
), rating_div_by_position AS (
    SELECT query_name, SUM(rating::numeric / position::numeric) AS rating_div_pos
    FROM Queries
    GROUP BY query_name
)

SELECT
    t1.query_name,
    ROUND(t3.rating_div_pos / t1.total, 2) AS quality,
    COALESCE(ROUND( (t2.poor_total::numeric / t1.total::numeric) * 100, 2), 0) AS poor_query_percentage
FROM total_per_name AS t1
LEFT JOIN poor_queries AS t2 ON t1.query_name = t2.query_name
LEFT JOIN rating_div_by_position AS t3 ON t1.query_name = t3.query_name
;
