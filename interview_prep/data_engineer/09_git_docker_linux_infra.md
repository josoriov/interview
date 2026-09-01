# Git, Docker, Linux, and Infrastructure - questions and answers

## 1. Why is Git important in data engineering?

Git provides version control, traceability, collaboration, review, rollback, and governance. It is important not only for application code but also for SQL, Airflow DAGs, infrastructure templates, and reporting assets.

## 2. What is a good commit strategy?

Commits should be small, coherent, and descriptive. Each commit should represent one logical change and include enough context for future debugging.

## 3. What would you look for in a pipeline code review?

I would check correctness, idempotence, error handling, logging, configuration, tests, data-quality checks, security, performance, and whether the change affects downstream consumers.

## 4. What is Docker?

Docker packages an application and its dependencies into a container image so it can run consistently across environments.

## 5. What should a good Dockerfile include?

A good Dockerfile should use a suitable base image, pin dependency versions, avoid unnecessary packages, run as a non-root user when possible, use caching effectively, and keep the image small.

## 6. Why pin dependency versions?

Pinned versions make builds reproducible. Without pinning, a dependency update can break a pipeline even if the application code did not change.

## 7. What Linux commands do you use to inspect data or logs?

Useful commands include `head`, `tail`, `less`, `grep`, `awk`, `sed`, `wc`, `cut`, `sort`, `uniq`, `du`, `df`, `find`, and `ps`.

## 8. How would you view logs in real time?

```bash
tail -f application.log
```

For containers:

```bash
docker logs -f container_name
```

## 9. How would you find large files?

```bash
find /path -type f -size +1G
```

Or inspect directory sizes:

```bash
du -h --max-depth=1 /path | sort -h
```

## 10. What is CI/CD for data pipelines?

CI/CD automates testing, validation, packaging, and deployment of pipeline code. It reduces manual errors and makes releases more reliable.

## 11. What would you include in CI for an Airflow repository?

I would include Python linting, unit tests, DAG import tests, dependency checks, SQL validation when possible, and maybe static checks for task naming, retries, and owner metadata.

## 12. What is infrastructure as code?

Infrastructure as code defines cloud resources in version-controlled files instead of creating them manually. This improves reproducibility, reviewability, and rollback.

## 13. What are the advantages of CloudFormation?

CloudFormation lets AWS infrastructure be defined, reviewed, deployed, and updated consistently. It also helps track changes and recreate environments.

## 14. What is least privilege for credentials?

It means a credential or role should have only the permissions required for its task. For example, a pipeline that reads one S3 prefix should not have full administrative access.

## 15. How would you manage secrets?

I would use a secrets manager or secure environment configuration, avoid committing secrets to Git, rotate credentials, restrict access, and audit usage.

## 16. How would you debug a failing container?

I would inspect logs, environment variables, mounted volumes, network access, image version, entrypoint, dependency versions, and resource limits. I might run an interactive shell in the container to reproduce the issue.

## 17. What is a deployment artifact?

A deployment artifact is a packaged version of code or configuration that can be deployed, such as a Docker image, Python wheel, DAG bundle, or infrastructure template.

## 18. What is rollback?

Rollback means returning to a previous known-good version after a deployment causes problems. Good rollback requires versioned artifacts and a clear deployment process.

## 19. How would you explain introducing Git into reporting?

I would say that I moved reporting assets toward software-engineering practices: version control, traceability, review, collaboration, and governance. This improved confidence and reduced operational risk.

## 20. Trick question: does Docker solve all environment problems?

No. Docker improves reproducibility, but problems can still come from missing secrets, wrong configuration, network differences, permissions, incompatible host resources, or external service dependencies.
