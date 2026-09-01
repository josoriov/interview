# 10 — Mock Interviews and Question Bank

## How to run a mock

Use a blank page and a 45-minute timer. Do not read the solution files. Record yourself. At minute 35, inject one changed requirement. At the end, score the ten categories in the study plan and write three specific improvements.

### Mock A: Search for a marketplace

Design product search over 500M listings for 100M daily users. Support text and image queries, personalization, availability, and sponsored items. p99 <250 ms.

Interviewer injects:

- minute 15: inventory/price changes must appear within one minute;
- minute 30: launch in five countries with different restricted-item policies;
- minute 35: traffic will spike 20× during a campaign.

Expected coverage: lexical+dense retrieval, multimodal embeddings, eligibility/index freshness, multi-stage ranking, sponsored-auction separation, exposure logs, query/item cold start, latency budget, cache, overload control, relevance vs. conversion, and policy by market.

### Mock B: Account-takeover detection

Detect suspicious logins and decide allow, challenge, or block at 50k peak TPS and p99 <60 ms. Labels are delayed and attackers adapt.

Expected coverage: cost-sensitive thresholds, streaming velocity/device graph features, point-in-time correctness, delayed/biased labels, active-active/fallback rules, calibration, adversarial drift, privacy, and appeal.

### Mock C: Medical-document assistant

Design an assistant that summarizes a patient's record for clinicians and cites evidence. It must never expose another patient's data and is not allowed to make an autonomous diagnosis.

Expected coverage: identity/patient/role authorization, structured and unstructured retrieval, temporal/conflicting evidence, abstention, citations, clinician-in-the-loop, audit, severe-error evaluation, red teaming, residence/retention, and explicit scope.

### Mock D: Real-time content moderation

Moderate text, images, and video at global social-network scale. Some categories must be blocked before publication; others can be reviewed later.

Expected coverage: policy taxonomy and regional versioning, cascade of hashes/rules/small/large models, video sampling, uncertainty and human review, adversarial evolution, appeals, fairness, latency vs. recall, active learning, and reviewer safety.

### Mock E: Coding agent for internal repositories

Design an agent that answers questions, proposes patches, runs tests, and optionally opens a pull request. It must not leak secrets or modify production.

Expected coverage: repository indexing, branch/worktree isolation, least-privilege tools, sandbox/network egress, prompt injection in code/docs, secret scanning, bounded loop, test feedback, approval before external side effects, audit, eval tasks, and rollback.

## Rapid questions with model answers

### Product and metrics

**Why is accuracy often insufficient?** It ignores imbalance, error cost, ranking position, calibration, and product impact. Choose a metric at the operating point and business loss.

**Offline metric improved but A/B did not. Why?** Dataset mismatch, proxy misalignment, position/policy effects, serving skew, novelty, latency regression, poor segment performance, or insufficient power.

**How do you choose a threshold?** Estimate FP/FN/review costs, examine calibrated curves by segment, choose policy bands, validate online, and govern changes.

**What is a guardrail?** A metric that must not degrade while optimizing the primary goal: safety events, complaints, latency, fairness, or cost.

### Data and training

**How do you detect leakage?** Reconstruct prediction-time availability, audit timestamps/joins, split by time/entity, remove suspicious variables, and compare offline to logged online features.

**What is point-in-time correctness?** Every training feature reflects only information effective before that row's prediction cutoff.

**Why log impressions?** Outcomes are interpretable only relative to what the system exposed and where; otherwise recommendation/ranking labels are biased or missing.

**When do you need a feature store?** Reuse, millisecond serving, historical joins, and governance at organizational scale—not merely because ML exists.

**How do you handle delayed labels?** Mature cohorts before labeling, use temporal gaps, track early proxies separately, and avoid evaluating recent unknowns as negatives.

**Data drift versus concept drift?** P(X) changing is covariate drift; P(Y|X) changing is concept drift. Only the latter necessarily invalidates the learned mapping.

### Serving and reliability

**Batch or online?** Let freshness and interaction decide. Batch is simpler and cheaper; online supplies current context under a strict SLO; hybrid often wins.

**What is training-serving skew?** Features/preprocessing differ between offline training and online inference. Share definitions, version schemas, and compare vectors.

**Why can GPU utilization mislead?** High utilization can coexist with queueing/OOM; low utilization can reflect memory or batching limits. Also monitor queue age, tokens/s, memory, and tail latency.

**How do you reduce tail latency?** Deadlines, parallel I/O, right-sized pools, caches, bounded queues, request shaping, batching by length, circuit breakers, and fallbacks.

**What does graceful degradation mean?** Preserve a safe subset of value using old/smaller models, cached/precomputed results, rules, or read-only behavior when dependencies fail.

**How do you deploy a model safely?** Offline gates, shadow, warm/health check, canary, online guardrails, atomic routing, and tested rollback.

### Recommendation/search

**Why retrieval then ranking?** Cheap retrieval reduces millions to hundreds; expensive contextual ranking then meets latency while preserving quality.

**Dense or lexical retrieval?** Dense handles semantic similarity; lexical handles exact/rare terms. Hybrid often improves recall.

**How do you handle new items?** Content features/embeddings, creator/category priors, and bounded exploration until interaction data arrives.

**Why are clicks biased?** Users can click only displayed items; position and the previous ranker affect exposure. Log propensity or run controlled exploration.

### LLM and RAG

**RAG or fine-tuning?** RAG for changing/private facts, deletion, access control, and citations; fine-tuning for stable behavior/style. They can coexist.

**How do you evaluate RAG?** Evaluate parsing, retrieval recall/ranking, context selection, generation/grounding/citations, and end-to-end task success separately.

**How do you prevent tenant leaks?** Derive tenant from authenticated identity; enforce filters/ACLs in retrieval, stores, caches, and source-link resolution; test negative access cases.

**Why can long context hurt?** Higher latency/cost/KV memory, more irrelevant evidence, and attention failures. Retrieve and pack relevant evidence.

**What is prompt injection?** Untrusted content attempts to override instructions or induce tool/data misuse. Treat content as data, enforce permissions outside the model, allowlist tools, and validate effects.

**When should an agent act autonomously?** Only when the value warrants variability and actions are bounded, authorized, idempotent, auditable, recoverable, and evaluated. Prefer workflows for known steps.

**What if an LLM is nondeterministic?** Use distributions and repeated trials, schema constraints, deterministic code for hard rules, version all components, and evaluate outcome rates rather than one run.

### Safety and operations

**What makes an alert actionable?** Impact/severity, threshold/window, owner, evidence, runbook, mitigation, and resolution criterion.

**How do you monitor without immediate labels?** Input/feature/score distributions, proxy outcomes, slice behavior, human review, and delayed backfill of true performance—without confusing proxies with truth.

**How do you explain a high-risk decision?** Preserve exact versions and inputs, provide faithful governed reason codes/evidence, state uncertainty/limitations, and offer human review or appeal.

**How do you protect privacy in logs?** Minimize, redact/tokenize, encrypt, restrict access, set retention, avoid raw prompts when unnecessary, and audit access.

**What belongs in a postmortem?** Impact, timeline, detection, root/contributing causes, mitigation, what went well/poorly, and owned preventive actions—not blame.

## Trade-off drills

Answer each in 60 seconds using: requirement → option A/B → decision → trigger to revisit.

1. HNSW vs. IVF/PQ.
2. API model vs. self-hosted model.
3. one large model vs. cascade/router.
4. feature store vs. warehouse plus KV.
5. event-driven streaming vs. frequent micro-batch.
6. active-active vs. active-passive region.
7. response cache vs. semantic cache.
8. human review before vs. after action.
9. one global model vs. regional models.
10. rules inside model vs. post-model policy service.

## Questions to ask the interviewer at the end

- Which part of this system is currently the hardest in your organization: data, modeling, serving, or evaluation?
- How are product and ML teams aligned on success and guardrails?
- What level of ownership does this role have over production operations and incident response?
- How does the team evaluate and safely roll out model or prompt changes?
