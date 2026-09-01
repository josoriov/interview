# System Design for Data Pipelines - questions and answers

## 1. How should you approach a system design question?

Start by clarifying requirements: data sources, volume, latency, consumers, SLAs, quality expectations, security, cost, and failure tolerance. Then propose an architecture, explain trade-offs, discuss failure modes, and close with monitoring and operational considerations.

## 2. Design a daily batch pipeline from events to dashboard

Ingest raw events into S3, validate file arrival, run Spark/Glue transformations, write curated Parquet partitioned by date, update the catalog, run data-quality checks, build aggregate tables, refresh the BI dataset, and alert on failures or anomalies.

## 3. How would you design idempotence?

Each run should process a specific data interval and write deterministic output. I would write to staging, validate, then replace the target partition atomically. Rerunning the same interval should produce the same result without duplicates.

## 4. How would you handle one year of backfills?

I would split the backfill by partitions, control concurrency, prioritize critical periods, monitor cost, validate outputs, and avoid overwhelming downstream systems. I would run a sample first before launching the full backfill.

## 5. Batch or streaming?

Batch is simpler and often enough for daily or hourly reporting. Streaming is useful when low latency is required, but it adds complexity in state management, exactly-once semantics, monitoring, and operational support.

## 6. How would you design an architecture for Prometheus data?

Raw logs or metrics land in S3. Spark/Glue parses and normalizes timestamps, labels, and metric values. Curated Parquet is partitioned by date and maybe service. Athena exposes SQL access, and QuickSight or another BI tool consumes aggregated operational metrics.

## 7. How would you design pipeline monitoring?

I would monitor workflow status, task duration, input volume, output volume, data freshness, validation results, cost, and dashboard refresh status. Alerts should be actionable and tied to ownership.

## 8. How would you control costs?

I would use efficient formats, partitioning, compaction, query pruning, appropriate cluster sizing, lifecycle policies, and pre-aggregations. I would also monitor data scanned and compute usage.

## 9. How would you handle multiple consumers?

I would create curated datasets with clear contracts and avoid building one-off logic inside every consumer. If consumers have different latency or grain needs, I would provide separate consumption tables derived from the same trusted layer.

## 10. How would you handle schema changes?

I would validate schema at ingestion, classify changes as compatible or breaking, version contracts, notify consumers, and update transformation logic through a controlled release process.

## 11. How would you design data lineage?

I would capture source tables, transformations, output tables, pipeline run IDs, code versions, and dependencies. Lineage can be stored through metadata tables, catalog tags, orchestration metadata, or dedicated lineage tools.

## 12. How would you protect sensitive data?

I would apply encryption, access controls, least privilege, masking, tokenization where appropriate, data retention policies, audit logs, and separation between raw sensitive data and curated consumption layers.

## 13. How would you design a pipeline control table?

A control table can store pipeline name, run ID, data interval, status, start time, end time, row counts, input paths, output paths, code version, and error message. It helps with observability and reruns.

## 14. How would you handle late-arriving data?

I would use event time, watermarks, safety windows, and partition reprocessing. For example, reprocess the last three days daily and deduplicate by business key.

## 15. How would you design exactly-once behavior?

In many batch pipelines, practical exactly-once behavior comes from idempotent writes, deterministic partition replacement, unique business keys, and transactional table formats when available. The key is preventing duplicate final records after retries.

## 16. What if downstream users require data before 8:00?

I would work backward from the SLA, define upstream deadlines, monitor freshness, optimize critical tasks, add alerts before the deadline, and prepare fallback or partial-publication strategies if acceptable.

## 17. How would you decide between materializing and querying on demand?

I would materialize if the query is expensive, reused, business-critical, or needed for low-latency dashboards. I would query on demand if usage is rare, logic changes frequently, or freshness requirements are strict.

## 18. What would you do if a dashboard becomes critical for leadership?

I would treat it as a production data product: document definitions, add quality checks, monitor freshness, define ownership, version changes, optimize performance, and establish an incident response process.

## 19. Full design: credit-risk batch scoring

Ingest application and customer data, compute features as of the scoring date, validate feature quality, load a versioned model, generate scores, write results to a production table, monitor distributions and drift, and expose outputs to decision systems or analysts.

## 20. How should you close a system design answer?

Summarize the architecture, repeat the main trade-offs, explain how you would monitor and operate it, and mention what you would improve later if requirements grow.
