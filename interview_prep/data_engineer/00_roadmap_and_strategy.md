# Roadmap and interview strategy

## Target profile

The target positioning is **Data Engineer with strong analytics ownership**: someone who can build reliable data pipelines, work with cloud-based data stacks, automate data quality checks, support production datasets, and communicate clearly with engineering and business stakeholders.

A strong interview narrative should emphasize:

- 5 years of experience across data engineering, analytics, and ML-adjacent workflows.
- Python, SQL, Spark, Airflow, AWS Glue, Athena, QuickSight, Power BI, Docker, Linux, Git, and CloudFormation.
- Production experience with large-scale data delivery, including Airflow-based Spark pipelines processing more than 2 TB weekly.
- Data quality automation that reduced reporting errors by more than 60%.
- Ability to translate business questions into reliable datasets, metrics, dashboards, and operational processes.

## Areas likely to be evaluated

Most technical interviews for this profile will probably cover SQL, Python, Spark, Airflow, AWS data services, data quality, data modeling, system design for data pipelines, and behavioral questions around ownership and stakeholder communication.

For client-facing interviews, they may also test whether you can explain technical work without sounding too theoretical. A good answer usually has three parts: the concept, the trade-off, and a concrete example from your experience.

## Recommended study plan

**Day 1-2:** SQL, data modeling, and analytics metrics. These are very common in screening rounds and client interviews.

**Day 3-4:** Python for data engineering, data quality, and pipeline reliability.

**Day 5-6:** Spark, Airflow, and AWS. Focus on explaining how the pieces fit together in production.

**Day 7:** System design and behavioral answers using STAR: Situation, Task, Action, Result.

## How to answer in interviews

Use this structure:

1. Give a direct answer first.
2. Explain the reasoning and trade-offs.
3. Mention failure modes or edge cases.
4. Connect to a real project when possible.

Example:

> I would not rely only on a timestamp-based incremental load because late-arriving data and clock issues can cause missing records. I would use a watermark plus a safety window, reprocess recent partitions, and deduplicate by business key. I used this kind of thinking in production pipelines where data correctness mattered more than simply minimizing compute.

## 60-second elevator pitch

I am a Data Engineer with around 5 years of experience building analytics and data platforms across Python, SQL, Spark, Airflow, and AWS. In my recent work, I automated data quality and validation workflows that reduced reporting errors by more than 60%, built reporting infrastructure used by stakeholders, and introduced Git-based governance for analytics assets. Previously, I maintained Airflow-based Spark pipelines processing more than 2 TB weekly and built AWS Glue/Spark ETL pipelines delivering query-ready datasets into Athena and QuickSight. I also have a background in Physics and a Master's in Computational Science, so I combine analytical rigor with practical production experience.

## Questions you should answer very well

1. How would you design a reliable batch data pipeline from raw logs to a dashboard?
2. How do you make a pipeline idempotent?
3. How do you detect and handle data quality issues?
4. How do you optimize a slow SQL query?
5. How do you optimize a slow Spark job?
6. What is the difference between Airflow and Spark?
7. How would you model KPIs for business reporting?
8. How would you explain a reporting discrepancy to a stakeholder?
9. How do you manage production incidents in data pipelines?
10. How do you make your work reproducible and maintainable?
