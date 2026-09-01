# 07 — MLOps, Infrastructure, and Cost

## Architecture principle and build vs. buy

For every component ask: which requirement does it satisfy, what is its source of truth, who operates it, how does it fail/recover, what simpler alternative exists, and how could it be replaced?

Managed APIs provide fast time-to-market and strong models but introduce variable cost, quotas, privacy/residency questions, provider changes, and lock-in. Self-hosting gives control and optimization but requires accelerators, serving expertise, patching, safety work, and capacity management.

```text
TCO = compute + storage + network + licenses
    + engineering/on-call + security/compliance
    + opportunity cost + risk
```

Benchmark on your workload: quality, p95/TTFT, throughput, availability, cost per successful task, and constraints.

## CI/CD/CT and lineage

Use isolated dev/staging/prod, infrastructure as code, redacted/synthetic non-prod data, code/data/model/security/load tests, immutable artifact registry, and gated promotion. Continuous training must not directly imply automatic deployment.

Track artifact URI/hash, code/config/environment, dataset and feature schema, global/segment metrics, serving requirements, approvals, owner, expiry, and rollback target. For LLM apps, version model, prompt, tools, policies, retriever, embedding model, chunker, and knowledge/index together.

## Compute

Containers package runtime; orchestrators schedule, health-check, roll out, and scale it. GPU workloads need compatible drivers, node pools/placement, preloaded weights, warm-up before readiness, topology awareness for partitioned models, limits, and GPU/KV-cache observability. Serverless works for sporadic small models only when cold start fits the SLO.

Data parallel training replicates the model and splits batches. Tensor/model/pipeline parallelism is needed when the model does not fit a device and increases communication/operational complexity. Use durable checkpoints, integrity checks, restartability, and spot/preemptible nodes only with acceptable lost-work risk.

Keep compute near data to reduce egress, latency, and residency problems. Cache datasets and use efficient partitions/formats.

## Cost optimization

Training: sample and ablate first, early-stop trials, use mixed precision, reuse features/embeddings, checkpoint on spot, shut down idle resources, and consider smaller models/PEFT.

Inference: measure cost per successful task; use routing/cascades, batching, cache, quantization/distillation, shorter input/output, async processing, and capacity matched to traffic. RAG: incremental embeddings by content hash, sensible chunks, compact vectors, filters, index lifecycle, and reranking only top N.

Model compression spans three families, often combined: **quantization** (fewer bits per weight/activation), **distillation** (a smaller student learns from a larger teacher), and **pruning** (removing weights, heads, or layers). Structured pruning (e.g., dropping attention heads or layers) yields real hardware speedups and memory savings; unstructured pruning (zeroing individual weights) sparsifies the model but rarely translates directly to latency without sparse kernels. Validate every compression technique on the eval set because the quality loss is rarely uniform across segments, tasks, or long-tail inputs.

For LLM capacity, use distributions of QPS, concurrency, input/output length, TTFT deadline, model/tenant mix, cache rate, and tool variability. Benchmark prefill and decode separately, include 30–50% margin, and tolerate loss of a replica.

## Multi-tenancy and supply chain

Derive tenant identity from credentials and enforce it in every database, index, cache, tool, and log. Add namespace/isolation, per-tenant encryption/access, quota/fair scheduling, noisy-neighbor protection, cost attribution, and tenant deletion/export.

Pin dependencies, maintain an SBOM, scan artifacts, verify model/dataset provenance and licenses, keep secrets outside images/prompts, patch vulnerabilities, and mirror critical artifacts.

## Disaster recovery

Define RPO and RTO, backup/replication/retention, tested restoration, rebuild of derived indices, replicated artifact registry, degraded/manual modes, and provider exit plan. Original documents, metadata, and ACLs are usually the source of truth; a vector index should be rebuildable.

## Decision shortcuts

| Situation                  | Start                    | Evolve when                            |
|----------------------------|--------------------------|----------------------------------------|
| Daily scoring, low traffic | Batch + database         | Fresh context creates value            |
| Recommendation at scale    | Retrieval + ranker       | More stages improve net utility        |
| Knowledge assistant        | Hybrid RAG               | Fine-tune repeated behavior, not facts |
| Low-volume LLM             | API                      | TCO/control justifies hosting          |
| One team's features        | Warehouse + KV if needed | Reuse/skew justify feature platform    |
| Small index                | Single node + replica    | RAM/QPS/SLO require sharding           |
| High-impact action         | Workflow + approval      | Autonomy proves safe and valuable      |

Describe capabilities before vendor names: “a durable partitioned log with replay and consumer groups.” This shows transferable reasoning and avoids pretending one product guarantees the entire system.
