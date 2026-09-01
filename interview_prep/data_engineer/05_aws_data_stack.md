# AWS Data Stack - questions and answers

## 1. How would you describe a data lake on AWS?

A data lake on AWS usually stores raw and curated data in S3, processes data with services such as Glue or Spark, catalogs metadata with Glue Data Catalog, queries data with Athena, and exposes insights through tools such as QuickSight or external BI platforms.

## 2. What is AWS Glue?

AWS Glue is a managed data integration service. It can run ETL jobs, manage crawlers, and maintain the Glue Data Catalog. Glue jobs often use Spark under the hood.

## 3. What is Athena?

Athena is a serverless query engine that lets you run SQL queries directly over files in S3, commonly using tables defined in the Glue Data Catalog.

## 4. How would you reduce Athena costs?

Athena charges based on data scanned. I would use columnar formats like Parquet, compression, partitioning, partition pruning, selecting only needed columns, avoiding `SELECT *`, and pre-aggregating frequently queried datasets.

## 5. What is the Glue Data Catalog?

It is a metadata catalog that stores table definitions, schemas, partitions, and locations for datasets. Athena, Glue, Spark, and other tools can use it to discover and query data.

## 6. How would you manage permissions in AWS?

I would use IAM roles and policies with least privilege. Access should be granted only to the resources and actions required. For sensitive data, I would also use encryption, audit logging, and separation of duties.

## 7. What does least privilege mean?

Least privilege means giving users, applications, or roles only the minimum permissions they need to perform their job. This reduces the impact of mistakes, credential leaks, or compromised services.

## 8. What is CloudFormation?

CloudFormation is AWS infrastructure as code. It defines AWS resources in templates so infrastructure can be versioned, reviewed, deployed, and reproduced consistently.

## 9. How would you design layers in S3?

A common design is raw, staging, curated, and consumption layers. Raw stores source data as received. Staging standardizes and validates. Curated contains cleaned business-ready datasets. Consumption contains aggregates or models optimized for BI and downstream users.

## 10. What format would you use for analytical datasets?

I would usually choose Parquet because it is columnar, compressed, typed, and efficient for analytical queries. It works well with Spark, Glue, Athena, and many data lake tools.

## 11. How would you update partitions in Athena?

Options include running `MSCK REPAIR TABLE`, adding partitions explicitly with `ALTER TABLE ADD PARTITION`, using Glue crawlers, or configuring partition projection to avoid storing every partition in the catalog.

## 12. What is partition projection?

Partition projection lets Athena infer partition values from table properties instead of reading them from the Glue Data Catalog. It can improve performance and reduce metadata management for tables with many partitions.

## 13. How would you handle sensitive data?

I would classify sensitive fields, apply encryption at rest and in transit, restrict access with IAM and lake permissions, mask or tokenize data when possible, avoid unnecessary replication, and monitor access through logs.

## 14. How would you connect Athena with QuickSight?

I would expose curated Athena tables, define clear datasets in QuickSight, manage permissions, and ensure queries are efficient. If dashboards are slow, I would use SPICE or pre-aggregated tables.

## 15. What would you check if Athena is slow?

I would check file format, compression, partition pruning, data scanned, number of files, query structure, joins, and whether the table has too many small files. Converting CSV to Parquet and compacting files often helps.

## 16. What is S3 eventual consistency and how can it affect pipelines?

Historically, eventual consistency meant that immediately after writing or deleting objects, listings might not reflect the latest state. Modern S3 has strong read-after-write consistency for many operations, but pipeline design should still avoid relying on fragile file-listing assumptions and should use explicit success markers when needed.

## 17. How would you promote data to production?

I would write to staging, validate quality checks, compare row counts and key metrics, update metadata, and only then publish or swap the production table/partition. Promotion should be traceable and reversible.

## 18. What operational metrics would you track in AWS?

I would track job duration, failure rate, records processed, data freshness, data volume, cost, data scanned by Athena, number of files, validation failures, and downstream dashboard refresh status.

## 19. How would you discuss your AWS experience?

I built and maintained AWS Glue and Spark ETL pipelines, delivered curated datasets into Athena and QuickSight, and managed infrastructure changes with CloudFormation. I would emphasize production reliability, cost awareness, and making data usable for downstream teams.

## 20. Design: Prometheus logs to Athena/QuickSight

A good design: ingest raw Prometheus logs into S3, parse and normalize them with Glue/Spark, write curated Parquet partitioned by date, catalog the data in Glue, query through Athena, build aggregated tables for frequent metrics, and expose dashboards in QuickSight.
