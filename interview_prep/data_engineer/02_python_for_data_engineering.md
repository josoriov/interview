# Python for Data Engineering - questions and answers

## 1. What characterizes good Python code for pipelines?

Good pipeline code is readable, modular, testable, observable, configurable, and idempotent. It should separate extraction, transformation, validation, and loading. It should also have clear logging, error handling, and no hidden assumptions.

## 2. How would you structure a Python pipeline?

I would split it into functions or modules such as `extract()`, `transform()`, `validate()`, and `load()`. Configuration should come from environment variables, YAML files, or a parameter system, not hardcoded values.

```python
def run_pipeline(config):
    raw = extract(config.source)
    transformed = transform(raw)
    validate(transformed)
    load(transformed, config.target)
```

## 3. How would you handle errors in a pipeline?

I would distinguish between retryable errors and non-retryable errors. Network timeouts or temporary service failures can be retried. Schema mismatches or invalid data should fail fast, log useful context, and trigger an alert. Errors should be explicit rather than silently ignored.

## 4. Why avoid code with hidden side effects?

Hidden side effects make pipelines difficult to test and debug. A function that transforms data should not unexpectedly write files, update databases, or modify global state. Clear boundaries make production behavior easier to reason about.

## 5. How would you process a file that does not fit in memory?

I would stream or chunk the file instead of loading it all at once. With pandas, I could use `chunksize`. For larger workloads, I would use Spark or another distributed engine.

```python
import pandas as pd

for chunk in pd.read_csv("large_file.csv", chunksize=100_000):
    processed = transform(chunk)
    write_chunk(processed)
```

## 6. What is the difference between list, tuple, set, and dictionary?

A list is ordered and mutable. A tuple is ordered and immutable. A set stores unique elements and is useful for membership checks. A dictionary maps keys to values and is useful for structured lookups.

## 7. When would you use generators?

Generators are useful when processing data lazily, especially when the full dataset should not be kept in memory. They are common in streaming, file parsing, and pipeline stages that produce records one by one.

```python
def read_lines(path):
    with open(path) as f:
        for line in f:
            yield line.strip()
```

## 8. What is idempotence in a Python pipeline?

An idempotent pipeline can be run multiple times with the same input and produce the same final result without duplicating data or corrupting state. This matters for retries, backfills, and production recovery.

## 9. What makes logging useful?

Useful logs include the pipeline name, run ID, input range, record counts, validation results, output location, and error context. Logs should help answer: what ran, what data was processed, what changed, and where it failed.

## 10. How would you test data transformations?

I would create small input datasets with known expected outputs and test edge cases such as nulls, duplicates, invalid values, empty inputs, and boundary dates.

```python
def test_transform_removes_invalid_rows():
    input_rows = [{"id": 1, "value": 10}, {"id": 2, "value": None}]
    result = transform(input_rows)
    assert len(result) == 1
```

## 11. What are type hints and why do they matter?

Type hints document expected input and output types and help static analysis tools catch errors earlier. They also make code easier to read for other engineers.

```python
def normalize_country(country: str) -> str:
    return country.strip().upper()
```

## 12. What is the difference between `copy` and `deepcopy`?

A shallow copy copies the outer object but keeps references to nested objects. A deep copy recursively copies nested objects. This matters when working with mutable structures such as dictionaries containing lists.

## 13. How would you manage configuration?

I would keep environment-specific values outside the code. For example, source paths, database names, thresholds, and credentials should come from configuration files, environment variables, Airflow variables, or a secrets manager.

## 14. Why should credentials not be stored in code?

Hardcoded credentials are a security risk, difficult to rotate, and can leak through Git. Credentials should be stored in a secrets manager or environment-specific secure configuration with least-privilege access.

## 15. How would you implement simple schema validation?

I would check required columns, data types, nullable fields, uniqueness, and valid ranges before loading data downstream.

```python
required = {"customer_id", "event_date", "amount"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Missing columns: {missing}")
```

## 16. What problems can appear when using pandas in production?

Pandas is excellent for moderate-sized data, but it can fail with large datasets because it is memory-bound and single-machine. Production concerns include memory usage, slow operations, implicit type conversions, and inconsistent behavior across environments.

## 17. How would you optimize pandas code?

I would avoid row-by-row loops, use vectorized operations, select only necessary columns, use appropriate data types, process in chunks, and move to Spark when the workload is too large for a single machine.

## 18. What is a pure function and why is it useful?

A pure function returns the same output for the same input and has no side effects. Pure functions are easier to test, reason about, and reuse in pipeline transformations.

## 19. How would you design a CLI for a pipeline?

I would expose parameters such as start date, end date, environment, input path, output path, and run mode. The CLI should validate arguments and print clear logs.

```bash
python run_pipeline.py --start-date 2026-01-01 --end-date 2026-01-31 --env prod
```

## 20. Interview question: what would you do if your script works locally but fails in production?

I would compare Python versions, dependency versions, environment variables, permissions, input data, file paths, memory limits, and network access. I would add logs around the failing step, reproduce the production input locally if possible, and then create a test or deployment check to prevent recurrence.
