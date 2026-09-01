# Spark and Big Data - questions and answers

## 1. What is Spark?

Spark is a distributed processing engine used to process large datasets across a cluster. It provides APIs such as DataFrames and SQL, and it is commonly used for ETL, batch processing, large-scale analytics, and ML feature preparation.

## 2. What is the difference between a transformation and an action?

Transformations define a new DataFrame or RDD, but they are lazy. Examples are `select`, `filter`, and `join`. Actions trigger execution, such as `count`, `show`, `collect`, and `write`.

## 3. Why is Spark lazy?

Spark is lazy so it can build an execution plan and optimize it before running. This allows Spark to push filters, reduce unnecessary work, and plan stages more efficiently.

## 4. What is a shuffle?

A shuffle is data movement across partitions or nodes. It happens during operations such as joins, aggregations, `groupBy`, and repartitioning. Shuffles are expensive because they involve network, disk, and serialization overhead.

## 5. How would you optimize a join in Spark?

I would check table sizes, join keys, partitioning, skew, and data formats. If one table is small, I may use a broadcast join. I would filter early, select only needed columns, use compatible partitioning, and avoid unnecessary shuffles.

```python
from pyspark.sql.functions import broadcast

result = large_df.join(broadcast(small_df), "customer_id", "left")
```

## 6. What is data skew?

Data skew happens when some keys have much more data than others, causing a few partitions to process disproportionately large workloads. This can make a Spark job slow even if most tasks finish quickly.

## 7. What is salting?

Salting is a technique to reduce skew by adding a random or calculated suffix to hot keys, spreading them across multiple partitions. After processing, the salt can be removed or aggregated away.

## 8. What is the difference between `repartition` and `coalesce`?

`repartition` increases or decreases partitions and performs a full shuffle. `coalesce` usually reduces partitions with less data movement. `repartition` is useful when redistributing data evenly; `coalesce` is useful before writing fewer output files.

## 9. Why should you avoid too many small files?

Small files create overhead for metadata, scheduling, and file listing. Query engines like Spark and Athena can become slower because they need to open and process many tiny files. Compaction can improve performance.

## 10. Why is Parquet often better than CSV for analytics?

Parquet is columnar, compressed, typed, and supports predicate pushdown. CSV is row-based, text-heavy, and does not preserve types reliably. For analytical queries, Parquet usually scans less data and performs better.

## 11. What is predicate pushdown?

Predicate pushdown means applying filters as close to the storage layer as possible so the engine reads less data. With Parquet, Spark can often skip row groups that do not match the filter.

## 12. How would you choose partitions in a data lake?

I would choose partitions based on common query filters and data volume, often by date. A good partition should reduce scans without creating too many small files. For example, `dt=YYYY-MM-DD` is common for event data.

## 13. What is `cache` and when would you use it?

`cache()` stores a DataFrame in memory or memory plus disk for reuse. I would use it when the same expensive intermediate result is reused multiple times. I would not cache blindly because it consumes cluster memory.

## 14. Why can `collect()` be dangerous?

`collect()` brings all data to the driver. If the dataset is large, the driver can run out of memory. In production, it is safer to use aggregations, samples, `limit`, or write results to storage.

## 15. What would you check if a Spark job is slow?

I would inspect the Spark UI: stages, tasks, shuffle read/write, skew, spills, executor memory, number of partitions, input size, and slow tasks. Then I would optimize joins, partitioning, data format, filtering, and output file sizes.

## 16. What is a partition in Spark?

A partition is a chunk of data processed by one task. The number and size of partitions affect parallelism and overhead. Too few partitions underuse the cluster; too many create scheduling overhead.

## 17. How would you handle schema evolution?

I would define expected schemas, validate incoming data, version schema changes, and use formats that support evolution when appropriate. Backward-compatible changes, such as adding nullable columns, are easier than changing data types or removing columns.

## 18. How would you write data safely?

I would write to a temporary path first, validate the output, and then atomically promote or register the final dataset. For partitioned data, I would avoid partially overwriting good partitions and make retries safe.

## 19. How would you process Prometheus logs in Spark?

I would parse raw logs from the landing zone, enforce schema, normalize timestamps and labels, deduplicate records if needed, derive metrics, write curated Parquet datasets partitioned by date, and expose them through Athena or another query layer.

## 20. How would you discuss your experience with 2 TB weekly pipelines?

I would focus on reliability, monitoring, failure handling, data volume, and production ownership. A strong answer is: I maintained an Airflow-orchestrated Spark pipeline processing more than 2 TB weekly, where the key challenges were stable scheduling, scalable transformations, data correctness, and recoverability after failures.
