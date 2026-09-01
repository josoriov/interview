# Data Quality and Observability - questions and answers

## 1. What is data quality?

Data quality means data is fit for its intended use. It is not only about being error-free; it is about being accurate, complete, timely, consistent, valid, and trusted by users.

## 2. Common dimensions of data quality

Important dimensions include completeness, uniqueness, validity, consistency, accuracy, freshness, referential integrity, and distribution stability.

## 3. What checks would you add to a KPI pipeline?

I would check schema, required columns, null rates, duplicate business keys, valid ranges, row counts, freshness, referential integrity, and metric-level anomalies compared with historical baselines.

## 4. How would you detect an anomalous drop in a KPI?

I would compare the current value with recent historical values, seasonality, expected business calendars, and upstream volume. I would also check whether the drop appears in raw data, curated data, or only in the dashboard.

## 5. What is the difference between a data error and a real business change?

A data error usually comes from pipeline failures, missing inputs, schema changes, duplicates, or incorrect transformations. A real business change should be visible consistently across multiple trusted sources and should match external context.

## 6. How would you automate validations?

I would encode checks as code and run them inside the pipeline before publishing data. Results should be logged, stored, and monitored. Critical failures should block publication; warnings may notify but not stop the pipeline.

## 7. What is a data contract?

A data contract is an agreement between data producers and consumers about schema, meaning, freshness, allowed values, and change management. It helps prevent unexpected upstream changes from breaking downstream systems.

## 8. How would you handle an unexpected schema change?

I would fail fast if the change breaks expectations, alert the owner, inspect the upstream change, and decide whether to adapt the pipeline or request a rollback. For compatible changes, such as a new nullable column, I would update the schema and tests.

## 9. What does freshness mean?

Freshness measures how up to date data is. For example, a dashboard may require data no older than one hour or a daily report may require yesterday's data by 8:00.

## 10. What is lineage?

Lineage describes where data comes from, how it is transformed, and where it is consumed. It helps debug issues, assess impact, and understand dependencies.

## 11. How would you reduce reporting errors?

I would centralize metric definitions, automate validations, version-control reporting logic, document assumptions, monitor freshness and anomalies, and reduce manual steps. This connects directly to experience reducing reporting errors by more than 60% through automated validation workflows.

## 12. How would you defend the 60% error reduction in an interview?

I would explain the baseline, the types of errors, the validation checks introduced, how errors were measured, and how the process changed. A credible answer should be specific: fewer manual mistakes, earlier detection, better traceability, and more trusted KPIs.

## 13. What is the difference between code testing and data testing?

Code testing checks whether logic behaves as expected for controlled inputs. Data testing checks whether real datasets satisfy expectations such as uniqueness, completeness, freshness, and valid ranges.

## 14. What would you do if a quality check fails?

I would classify severity. If the issue affects critical data, I would stop publication, alert stakeholders, and investigate. If it is a non-critical warning, I might publish with a note and create a follow-up task. The decision depends on business impact.

## 15. What observability metrics would you record?

I would record row counts, input and output sizes, null rates, duplicate counts, freshness, job duration, failure rate, retry count, schema version, and key business metric distributions.

## 16. How would you avoid alert fatigue?

Alerts should be actionable, deduplicated, prioritized, and tied to clear ownership. Not every warning should page someone. Thresholds should be tuned and reviewed regularly.

## 17. What is reconciliation?

Reconciliation compares data across systems or pipeline stages to confirm they match. For example, comparing transaction totals in a source system with totals in the warehouse after transformation.

## 18. How would you document a critical metric?

I would document the business definition, formula, grain, source tables, filters, exclusions, refresh frequency, owner, known limitations, and example queries.

## 19. How would you handle time zones in KPIs?

I would define a canonical storage timezone, usually UTC, and a business reporting timezone. I would be explicit about day boundaries, daylight saving time, and whether the metric uses event time or processing time.

## 20. Trick question: does a dashboard with no visible errors mean the data is correct?

No. A dashboard can look normal while using stale, incomplete, duplicated, or incorrectly transformed data. Correctness requires validation, monitoring, clear definitions, and trust in the upstream pipeline.
