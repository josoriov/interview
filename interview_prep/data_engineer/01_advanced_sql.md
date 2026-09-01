# Advanced SQL - questions and answers

## 1. How would you find duplicate records by business key?

```sql
SELECT customer_id, event_date, COUNT(*) AS n
FROM events
GROUP BY customer_id, event_date
HAVING COUNT(*) > 1;
```

To keep only one record, I would use `ROW_NUMBER()`:

```sql
WITH ranked AS (
  SELECT *,
         ROW_NUMBER() OVER (
           PARTITION BY customer_id, event_date
           ORDER BY updated_at DESC
         ) AS rn
  FROM events
)
SELECT *
FROM ranked
WHERE rn = 1;
```

The key idea is to define a **business key** and a deterministic rule for choosing the winning record.

## 2. What is the difference between `WHERE` and `HAVING`?

`WHERE` filters rows before aggregation. `HAVING` filters groups after `GROUP BY`.

```sql
SELECT country, COUNT(*) AS users
FROM customers
WHERE status = 'active'
GROUP BY country
HAVING COUNT(*) > 100;
```

First, only active users are selected. Then countries with more than 100 users are kept.

## 3. What are window functions and when would you use them?

Window functions calculate metrics over a set of related rows without collapsing the result like `GROUP BY` does. They are useful for rankings, running totals, previous-row comparisons, deduplication, and partition-level metrics.

```sql
SELECT
  user_id,
  order_id,
  order_date,
  SUM(amount) OVER (
    PARTITION BY user_id
    ORDER BY order_date
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS cumulative_amount
FROM orders;
```

## 4. What is the difference between `ROW_NUMBER`, `RANK`, and `DENSE_RANK`?

`ROW_NUMBER` assigns unique numbers even when there are ties. `RANK` leaves gaps after ties. `DENSE_RANK` does not leave gaps.

For scores 100, 90, 90, 80:

- `ROW_NUMBER`: 1, 2, 3, 4.
- `RANK`: 1, 2, 2, 4.
- `DENSE_RANK`: 1, 2, 2, 3.

## 5. How would you calculate the difference between the current value and the previous one?

```sql
SELECT
  metric_date,
  value,
  value - LAG(value) OVER (ORDER BY metric_date) AS delta_vs_previous_day
FROM daily_metrics;
```

`LAG` allows comparison with a previous row according to a defined order.

## 6. How would you implement an incremental load?

I need a control column such as `updated_at`, `created_at`, a watermark, or an increasing ID.

```sql
SELECT *
FROM source_table
WHERE updated_at > (SELECT max_loaded_at FROM pipeline_state);
```

Then I would use a `MERGE` or upsert in the target table to insert new records and update changed ones.

## 7. What problems can appear with timestamp-based incremental loads?

They can miss data because of late-arriving events, clock synchronization issues, old timestamps in updated records, or source-system delays. A common mitigation is to reprocess a safety window, for example the last 1-3 days, and deduplicate by business key.

## 8. What is a `MERGE` and why is it useful?

A `MERGE` combines inserts, updates, and sometimes deletes based on a match condition between source and target. It is very useful for incremental pipelines.

```sql
MERGE INTO target t
USING staging s
ON t.id = s.id
WHEN MATCHED THEN UPDATE SET
  value = s.value,
  updated_at = s.updated_at
WHEN NOT MATCHED THEN INSERT (id, value, updated_at)
VALUES (s.id, s.value, s.updated_at);
```

## 9. What is a CTE?

A CTE, written with `WITH`, lets you split a query into readable steps. It does not always improve performance; its main value is usually clarity.

```sql
WITH active_users AS (
  SELECT * FROM users WHERE status = 'active'
)
SELECT country, COUNT(*)
FROM active_users
GROUP BY country;
```

## 10. How would you optimize a slow SQL query?

I would first inspect the execution plan and identify the bottleneck: full table scans, expensive joins, high-cardinality `COUNT(DISTINCT)`, missing partition filters, unnecessary columns, or skewed data. Then I would reduce the amount of data scanned, push filters earlier, select only required columns, use proper join keys, pre-aggregate if needed, and materialize intermediate results when the query is repeatedly used.

## 11. What is the difference between `INNER JOIN`, `LEFT JOIN`, and `FULL OUTER JOIN`?

`INNER JOIN` keeps only matching rows from both tables. `LEFT JOIN` keeps all rows from the left table and adds matching rows from the right table when available. `FULL OUTER JOIN` keeps all rows from both tables, with nulls where there is no match.

## 12. How would you detect orphan records?

I would use a `LEFT JOIN` and filter where the parent key is missing.

```sql
SELECT o.*
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;
```

This finds orders that reference a customer that does not exist.

## 13. What are a fact table and a dimension table?

A fact table stores measurable business events, such as orders, payments, sessions, or transactions. A dimension table stores descriptive context, such as customer, product, country, date, or channel.

Example: `fact_orders` contains `order_id`, `customer_id`, `product_id`, `amount`, and `order_date`; `dim_customer` contains customer attributes.

## 14. What is the grain of a table?

The grain defines what one row represents. For example, one row per order, one row per customer per day, or one row per event. It is crucial because it determines how metrics should be calculated and prevents double counting.

## 15. How would you calculate daily and monthly active users?

```sql
SELECT event_date, COUNT(DISTINCT user_id) AS dau
FROM events
GROUP BY event_date;
```

```sql
SELECT DATE_TRUNC('month', event_date) AS month,
       COUNT(DISTINCT user_id) AS mau
FROM events
GROUP BY 1;
```

The important detail is to define what “active” means: login, purchase, session, click, or another business event.

## 16. Why can `COUNT(DISTINCT)` be expensive?

It often requires keeping a large set of unique values, which can be memory-intensive and slow in distributed engines. Alternatives include pre-aggregation, approximate distinct counts such as HyperLogLog, or modeling the data to avoid repeated expensive calculations.

## 17. How would you handle `NULL` values in joins and metrics?

I would be explicit. In joins, `NULL = NULL` is not true in standard SQL, so null keys do not match. In metrics, I would decide whether null means unknown, missing, not applicable, or zero. For example, `COALESCE(amount, 0)` is valid only if missing amount should really be treated as zero.

## 18. How would you calculate a conversion rate?

```sql
SELECT
  COUNT(DISTINCT CASE WHEN purchased = 1 THEN user_id END) * 1.0 /
  COUNT(DISTINCT user_id) AS conversion_rate
FROM user_events;
```

A good answer must define the numerator, denominator, time window, attribution logic, and whether repeated conversions are allowed.

## 19. How would you explain a discrepancy between two dashboards?

I would compare metric definitions, filters, time zones, refresh times, source tables, joins, deduplication rules, and aggregation grain. Then I would produce a small reproducible query showing where the numbers diverge. The goal is not just to fix one dashboard, but to standardize the metric definition.

## 20. Trick question: does `SELECT DISTINCT` fix duplicates?

Not necessarily. It hides duplicate rows in the output, but it does not explain why duplicates exist. Real deduplication requires a business key, a rule for choosing the correct record, and ideally a fix upstream.
