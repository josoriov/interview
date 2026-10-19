-- LeetCode SQL 50 #30
-- Problem 1731. The Number of Employees Which Report to Each Employee
-- Category: Advanced Select and Joins
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
-- Write your PostgreSQL query statement below
with total_products as (
    select
        count(*) as total_products
    from
        Product
), products_per_customer as (
    select
        customer_id, count(distinct product_key) as num_products
    from
        Customer
    group by
        customer_id
)

select
    customer_id
from
    products_per_customer
where
    num_products = (select total_products from total_products)