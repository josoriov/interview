# Data Modeling, Analytics, and BI - questions and answers

## 1. What is dimensional modeling?

Dimensional modeling organizes data into fact and dimension tables to make analytical queries understandable, performant, and business-friendly.

## 2. What is a star schema?

A star schema has a central fact table connected to dimension tables. It is common in BI because it is easy to understand and efficient for many reporting queries.

## 3. What is a fact table?

A fact table stores measurable events or transactions, such as orders, payments, sessions, or machine events. It usually contains foreign keys to dimensions and numeric measures.

## 4. What is a dimension?

A dimension contains descriptive attributes used to filter, group, or explain facts. Examples include customer, product, date, location, or channel.

## 5. What is an SCD?

SCD means Slowly Changing Dimension. It describes how dimension attributes change over time and how those changes are stored.

## 6. When would you use SCD Type 2?

I would use SCD Type 2 when historical context matters. For example, if a customer changes segment, past orders should still be associated with the segment at the time of purchase.

## 7. What is a semantic layer?

A semantic layer centralizes metric definitions, business logic, and relationships so different dashboards and tools calculate metrics consistently.

## 8. How would you avoid discrepancies between Power BI and QuickSight?

I would centralize the metric logic in curated tables or a semantic layer, align filters and time zones, version-control definitions, and document metric ownership. BI tools should consume the same trusted data model.

## 9. What is a well-defined KPI?

A well-defined KPI has a clear business meaning, formula, data source, grain, filters, refresh frequency, owner, and known limitations. It should be reproducible with a query.

## 10. How would you design department-wide reporting infrastructure?

I would identify core business questions, define canonical datasets and KPIs, build curated tables, automate refreshes, add data quality checks, version-control assets, and provide documentation for stakeholders.

## 11. How would you version dashboards?

I would keep report definitions, semantic models, SQL queries, and configuration in Git when possible. Changes should go through review, testing, and release notes for major metric changes.

## 12. What did you learn by introducing Git into reporting?

Git improves traceability, collaboration, governance, and rollback capability. It turns reporting assets from manual artifacts into controlled analytical products.

## 13. What is an aggregate table?

An aggregate table stores precomputed metrics at a higher grain, such as daily revenue by country. It improves dashboard performance and reduces repeated expensive computation.

## 14. When would you materialize a query?

I would materialize a query when it is expensive, reused frequently, business-critical, or needed by multiple consumers. I would not materialize everything because it increases storage, maintenance, and freshness complexity.

## 15. How would you design an operational dashboard?

I would focus on actionable metrics, clear thresholds, freshness indicators, drill-down paths, and ownership. Operational dashboards should help users detect issues and decide what to do next.

## 16. What would you check if a dashboard loads slowly?

I would check query complexity, data volume, joins, calculated fields, filters, BI extract settings, aggregation level, and whether the dashboard is querying raw data instead of optimized tables.

## 17. How would you tell a stakeholder that a metric is not ready?

I would be transparent: explain what is missing, the risk of using the metric now, the validation steps needed, and a realistic path to make it production-ready. The goal is to protect trust, not just deliver numbers quickly.

## 18. What is the difference between ad hoc reporting and production reporting?

Ad hoc reporting answers one-off questions quickly. Production reporting is recurring, governed, documented, tested, and monitored because decisions depend on it.

## 19. How would you prioritize new metrics?

I would consider business impact, urgency, number of users, data availability, implementation complexity, risk, and whether the metric fits existing definitions or requires new modeling.

## 20. Interview question: how do you explain your BI role without sounding like only a dashboard developer?

I would emphasize that the work includes data modeling, pipeline reliability, quality checks, metric governance, stakeholder alignment, and production support. Dashboards are only the visible layer of a broader data product.
