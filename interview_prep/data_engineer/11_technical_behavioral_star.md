# Technical Behavioral Questions using STAR

## 1. Tell me about a project where you improved data quality

**Situation:** Reporting errors were reducing trust in operational KPIs.

**Task:** Improve reliability and reduce manual validation work.

**Action:** I automated Python-based validation workflows, added checks for schema, completeness, duplicates, and metric consistency, and integrated the results into the reporting process.

**Result:** Reporting errors were reduced by more than 60%, and stakeholders had more confidence in recurring KPI reporting.

## 2. Tell me about a large-scale project

I maintained an Airflow-based Spark pipeline processing more than 2 TB of data weekly. The main challenge was ensuring stable large-scale data delivery. I focused on orchestration, monitoring, failure handling, and scalable Spark transformations so downstream teams could rely on the data.

## 3. Example of working with non-technical stakeholders

I built and maintained reporting infrastructure and Power BI dashboards used for recurring decision-making. I translated stakeholder questions into metric definitions, validated the data, and communicated limitations clearly so decisions were based on trusted information.

## 4. Example of ownership

Ownership means not only writing the pipeline but also understanding the data, monitoring failures, communicating with users, documenting assumptions, and improving the process over time. A good example is taking responsibility for reporting quality and introducing automated validation instead of relying on manual checks.

## 5. Example of process improvement

Introducing Git-based version control for reporting assets improved traceability, governance, and collaboration. It made reporting changes reviewable and reduced the risk of undocumented manual edits.

## 6. What was a difficult technical challenge?

A strong answer can focus on large-scale Spark/Airflow pipelines: handling data volume, scheduling reliability, debugging failures, and ensuring downstream datasets remained correct. Explain the specific bottleneck, what you tested, and how the solution improved stability.

## 7. What do you do when you do not know something?

I clarify the requirement, isolate the unknown, research reliable documentation, create a small reproducible test, ask targeted questions if needed, and document what I learn. In production, I also communicate uncertainty clearly instead of guessing.

## 8. How do you handle deadline pressure?

I separate must-have from nice-to-have, communicate risks early, prioritize the critical path, and avoid compromising data correctness silently. If a deadline is at risk, I propose options with trade-offs.

## 9. How would you explain a production failure?

I would explain what happened, the impact, how it was detected, what immediate mitigation was taken, the root cause, and what preventive action was added. I would avoid blaming people and focus on improving the system.

## 10. What differentiates you from other candidates?

I combine strong analytical training from Physics and Computational Science with practical production experience in Python, SQL, Spark, Airflow, AWS, reporting infrastructure, and data quality. I can work across engineering and business contexts.

## 11. Why Data Engineering?

I like building reliable systems that turn raw data into useful, trusted information. Data engineering combines software, analytics, infrastructure, and business impact, which matches my experience and interests.

## 12. Why this role?

A good answer should connect the role to production data platforms, cloud workflows, stakeholder impact, and opportunities to own reliable data products. Mention the technologies from the job description when relevant.

## 13. How do you receive feedback?

I treat feedback as a way to improve the product and my engineering habits. I try to understand the underlying concern, ask clarifying questions, and turn feedback into specific changes.

## 14. How do you prioritize bugs versus new features?

I prioritize based on business impact, severity, affected users, data correctness, SLA risk, and long-term maintainability. Critical data correctness issues usually come before new features.

## 15. How do you collaborate with software engineering teams?

I align on data contracts, interfaces, deployment processes, logging, ownership, and incident response. Good collaboration prevents upstream changes from silently breaking downstream data products.

## 16. How do you collaborate with business teams?

I clarify definitions, ask what decision the metric supports, explain limitations, and provide reproducible numbers. I try to make trade-offs understandable without oversimplifying the technical details.

## 17. What is your biggest technical achievement?

A strong answer is reducing reporting errors by more than 60% through automated data validation, or maintaining large-scale Airflow/Spark pipelines processing more than 2 TB weekly. Choose the one that best matches the role.

## 18. What is a technical weakness?

Choose a real but manageable weakness. Example: “Earlier in my career, I focused more on delivering analyses than on making assets version-controlled and governed. I improved this by introducing Git-based workflows and treating reporting assets more like production code.”

## 19. How do you handle ambiguity?

I clarify the business objective, define assumptions, propose an initial scope, validate with stakeholders, and iterate. In data work, ambiguity often comes from metric definitions, ownership, and data availability.

## 20. Interview closing

A strong closing: “Based on our conversation, I see this role as requiring reliable data engineering, stakeholder communication, and production ownership. That fits well with my experience in Spark/Airflow pipelines, AWS data workflows, and data quality automation. I would be excited to contribute to making your data products more reliable and useful.”
