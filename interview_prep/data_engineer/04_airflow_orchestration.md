# Airflow and Orchestration - questions and answers

## 1. What is Airflow?

Airflow is an orchestration tool used to schedule, coordinate, and monitor workflows. It does not process big data itself; it triggers and manages tasks such as Spark jobs, SQL queries, Python scripts, and data validations.

## 2. What is a DAG?

A DAG is a Directed Acyclic Graph. In Airflow, it defines tasks and dependencies between them. “Acyclic” means the workflow cannot contain circular dependencies.

## 3. What is the difference between Airflow and Spark?

Airflow orchestrates workflows. Spark processes data. Airflow can trigger Spark jobs, but Spark performs the distributed computation.

## 4. How would you design a robust DAG?

A robust DAG should be modular, idempotent, observable, and retry-safe. It should have clear task boundaries, sensible retries, alerts, parameterized dates, external dependency checks, and data quality validation before publishing data.

## 5. What is idempotence in Airflow?

An idempotent task can run multiple times for the same execution date without duplicating data or corrupting the output. This is essential because Airflow tasks may be retried or backfilled.

## 6. What are retries?

Retries allow a failed task to run again automatically. They are useful for transient issues such as temporary network failures. They should not hide deterministic data errors such as schema mismatches.

## 7. What is a backfill?

A backfill reruns a workflow for historical dates. It is useful when logic changes, missing data is repaired, or historical partitions need to be regenerated.

## 8. What is `catchup`?

`catchup=True` means Airflow will create runs for all missed intervals since the DAG start date. `catchup=False` means it will generally run only the latest scheduled interval.

## 9. What are Sensors?

Sensors wait for an external condition, such as a file appearing in S3 or another DAG completing. They are useful but should be used carefully because long-running sensors can consume resources.

## 10. What is XCom and when should you avoid it?

XCom is a mechanism for passing small pieces of metadata between Airflow tasks. It should not be used for large datasets. Large data should be stored in external systems such as S3, databases, or data warehouses.

## 11. How would you handle external dependencies?

I would make dependencies explicit: file sensors, API availability checks, upstream table freshness checks, or control tables. I would add timeouts and clear failure messages so the team knows whether the issue is upstream, downstream, or internal.

## 12. What would you do if a task fails after writing partial data?

The best design is to avoid partial final writes. I would write to a staging location first, validate it, and only then promote it. If partial data already exists, I would clean the affected partition and rerun the task idempotently.

## 13. How would you organize dev, staging, and prod environments?

I would separate configuration, credentials, schedules, data paths, and permissions by environment. Code should be version-controlled and promoted through CI/CD or a controlled deployment process.

## 14. How would you version DAGs?

I would store DAGs in Git, use pull requests and code reviews, tag releases when needed, and avoid manual changes directly in production. For breaking changes, I would coordinate deployment and backfills carefully.

## 15. How would you monitor a DAG?

I would monitor task failures, duration, retries, SLA misses, data freshness, row counts, validation results, and downstream availability. Monitoring should include both workflow-level and data-level signals.

## 16. What is an SLA in Airflow?

An SLA defines the expected completion time for a task or workflow. If the task misses the SLA, Airflow can notify the team. In data pipelines, SLAs often correspond to business deadlines for reports or downstream processes.

## 17. How would you parameterize a daily run?

I would use Airflow's logical date or data interval to process a specific partition, for example `dt={{ ds }}`. The task should not depend on the wall-clock date because backfills need to process historical intervals correctly.

## 18. What is the problem with very large DAGs?

Very large DAGs can be difficult to understand, maintain, and debug. They can also create scheduler overhead. It may be better to split workflows into smaller DAGs with clear contracts.

## 19. How would you explain your experience with Airflow and Spark?

I maintained an Airflow-based Spark pipeline processing more than 2 TB of data weekly. My focus was on stable orchestration, scalable Spark transformations, failure handling, and delivering reliable production datasets for downstream users.

## 20. Design question: DAG from logs to dashboard

A strong design: wait for raw logs, run Spark parsing, validate schema and counts, write curated Parquet partitions, update the catalog, run metric aggregation, refresh the BI dataset, and alert on failures or data-quality anomalies.
