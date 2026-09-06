# 11 — Interview Cheat Sheet

Use this for the final review, not as a substitute for the full material.

## Opening checklist

```text
1. User, action, and harm
2. Scope / out of scope
3. Exact input and output
4. Business + online + offline + guardrail metrics
5. QPS, data, latency, availability, freshness, privacy, cost
6. Baseline before advanced model
```

## Universal diagram

![Universal diagram](images/11_interview_cheat_sheet_diagram_1_universal-diagram.svg)

## Numbers

```text
QPS avg = requests/day ÷ 86,400
QPS peak = avg × 3–10
concurrency = QPS × latency_seconds
storage = records × bytes × replication
instances = peak load ÷ measured throughput ÷ 0.5–0.7 utilization
raw vector bytes = count × dimensions × bytes/value
LLM work ≈ QPS × (input + output tokens)
```

Always add index/metadata overhead, replicas, peak margin, and loss of one instance.

### Reference anchors

| Quantity | Order of magnitude |
|----------|--------------------|
| Bytes per parameter | fp32 = 4, fp16/bf16 = 2, int8 = 1, int4 = 0.5 |
| Weights (fp16) | 7B ≈ 14 GB, 13B ≈ 26 GB, 70B ≈ 140 GB |
| KV cache per token | `2 × layers × n_kv_heads × head_dim × bytes` (≈ 0.5 MB/tok for a 7B fp16) |
| GPU memory (common) | A100 40/80 GB, H100 80 GB |
| Token throughput (one modern GPU) | ~1k–3k output tok/s (small models), far less for 70B+ |
| Embedding dims | text 384–1536+, images 512–2048 |
| Typical LLM request | input 0.5k–4k tokens, output 100–1k tokens |

```text
KV-cache memory ≈ concurrency × avg_context_tokens × bytes/token
LLM replicas ≈ peak (input + output) tokens/s ÷ tokens/s per replica ÷ utilization
```

Quote dollar figures only as order-of-magnitude anchors (e.g., $/GPU-hr and $/M input/output tokens) and always attach them to a measured workload, since pricing and hardware change; the reasoning—weights + KV memory, prefill vs. decode, tokens per replica—is what transfers.

## Metrics

- Classification: PR-AUC for rare classes; recall at fixed precision; calibration; expected cost.
- Ranking: recall@K, MRR, NDCG, then A/B outcome.
- Regression/forecast: MAE/RMSE/quantile; bias; interval coverage; rolling backtest.
- RAG: retrieval recall@K + answer correctness/grounding/citations/abstention.
- System: semantic success, p95/p99, freshness, fallback, cost.
- Always segment and add safety/product guardrails.

## Data questions

- What is the label, horizon, and maturity delay?
- Is every feature available at prediction time?
- Temporal/entity split? Policy/position bias?
- Impression/exposure log before outcome?
- Schema, freshness, null, distribution, invariant checks?
- Replay, dedupe, idempotent write, backfill?
- PII purpose, access, retention, deletion, lineage?

## Model questions

- What is the simplest baseline?
- Why this model under quality/latency/cost/risk?
- Calibration, threshold, uncertainty, abstention?
- Performance by segment and hard cases?
- Cold start and feedback loops?
- Champion/challenger and promotion gate?

## Serving questions

- Batch, online, streaming, or hybrid—and why?
- Latency budget by hop?
- Peak capacity, batching, cache, sharding, replicas?
- Bounded queues, admission control, priorities?
- Timeout, retry, idempotency, circuit breaker?
- Fallback ladder and failure semantics?
- Model-feature-policy version compatibility?

## RAG and agent questions

- Parsing/OCR quality, semantic chunks, metadata, source version?
- Lexical+dense, filters, reranker, context packing?
- ACL enforced before retrieval and source-link access?
- Citations actually support claims? No-answer behavior?
- Prompt injection: untrusted content, secrets, egress, output validation?
- Tools typed, least privilege, timeout, idempotency, audit?
- Workflow vs. agent? Max steps/tokens/time/cost?
- Confirmation and compensation for effects?

## Evaluation and operations

![Evaluation and operations](images/11_interview_cheat_sheet_diagram_2_evaluation-and-operations.svg)

- Versioned representative, hard, no-answer, and adversarial set.
- Rubric and human calibration; do not trust one LLM judge.
- Trace request to model/data/prompt/index/experiment.
- Monitor infrastructure, service, data/model, and semantic product quality.
- Alert = condition + impact + owner + runbook + mitigation.
- Rollback/kill switch, incident process, restore/failover test.

## Security and responsible AI

- Assets, actors, attack surfaces, blast radius.
- Least privilege, isolation, provenance, signed artifacts, rate limits.
- Poisoning, evasion, extraction, injection, exfiltration, denial of wallet.
- Privacy minimization, consent, encryption, TTL/deletion.
- Fairness metric tied to defined harm; appeal and human review.
- Exact version and faithful explanation for high-risk decisions.

## Strong closing

> “The design uses [baseline/core pattern] because it meets [requirements] at [estimated scale]. The key trade-offs are [quality vs. latency/cost] and [freshness/control vs. complexity]. It degrades to [fallback], is promoted through [evaluation/rollout], and is monitored with [primary semantic and system signals]. I would add [next complexity] only when [measurable trigger].”

## If you get stuck

Return to the chain:

![If you get stuck](images/11_interview_cheat_sheet_diagram_3_if-you-get-stuck.svg)

State an assumption, choose a simple option, explain why, and continue. A coherent incomplete design is stronger than an unconnected list of technologies.
