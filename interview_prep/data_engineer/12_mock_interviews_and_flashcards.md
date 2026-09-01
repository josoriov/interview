# Mock Interviews and Quick Flashcards

## Mock interview 1 - SQL + data quality

1. How would you deduplicate records by business key?
2. What is the difference between `WHERE` and `HAVING`?
3. How would you calculate a conversion rate?
4. How would you investigate a reporting discrepancy?
5. What data-quality checks would you add before publishing a KPI table?

Strong answers should mention business keys, deterministic deduplication, metric definitions, time zones, row counts, freshness, nulls, and stakeholder impact.

## Mock interview 2 - Spark + Airflow

1. What is the difference between Airflow and Spark?
2. What is a shuffle and why is it expensive?
3. How would you optimize a Spark join?
4. What is idempotence in Airflow?
5. How would you handle a failed task that wrote partial data?

Strong answers should mention orchestration versus processing, shuffle cost, broadcast joins, partitioning, staging writes, retries, and safe reruns.

## Mock interview 3 - AWS system design

1. Design a pipeline from raw logs in S3 to dashboards in QuickSight.
2. How would you reduce Athena cost?
3. How would you manage permissions?
4. How would you handle schema changes?
5. What would you monitor?

Strong answers should mention S3 layers, Glue/Spark, Parquet, Glue Catalog, Athena, QuickSight, IAM, least privilege, quality checks, and operational metrics.

## Mock interview 4 - ML-adjacent workflows

1. What is feature engineering?
2. What is data leakage?
3. How would you design daily batch scoring?
4. How would you monitor drift?
5. How would you collaborate with data scientists?

Strong answers should mention prediction time, temporal splits, feature validation, model versioning, reproducibility, and production scoring.

## Quick flashcards

**Q:** What is the grain of a table?

**A:** The meaning of one row, such as one order, one user per day, or one event.

**Q:** What is idempotence?

**A:** The ability to rerun a process with the same input and get the same final result without duplicates or corruption.

**Q:** What is a Spark shuffle?

**A:** Data movement across partitions/nodes, often caused by joins or aggregations.

**Q:** Why is Parquet good for analytics?

**A:** It is columnar, compressed, typed, and supports predicate pushdown.

**Q:** What is least privilege?

**A:** Granting only the minimum permissions required for a task.

**Q:** What is data freshness?

**A:** How up to date the data is compared with business expectations.

**Q:** What is a data contract?

**A:** An agreement about schema, meaning, freshness, and change management between producers and consumers.

**Q:** Why can `COUNT(DISTINCT)` be expensive?

**A:** It may require maintaining large sets of unique values across distributed workers.

**Q:** What is data leakage?

**A:** Using information in model training that would not be available at prediction time.

**Q:** What does Airflow do?

**A:** It orchestrates, schedules, and monitors workflows; it does not process big data itself.

## Checklist before an interview

- Prepare a 60-second pitch.
- Prepare one story about data quality improvement.
- Prepare one story about large-scale Spark/Airflow pipelines.
- Prepare one story about AWS Glue/Athena/QuickSight.
- Review SQL window functions and joins.
- Review idempotence, backfills, retries, and partial failures.
- Practice explaining technical trade-offs in simple English.
- Prepare 3 questions for the interviewer about data stack, team ownership, and production maturity.
