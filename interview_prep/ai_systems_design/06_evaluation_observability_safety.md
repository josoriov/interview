# 06 — Evaluation, Observability, Safety, and Responsible AI

## Evaluation stack

- unit tests for transforms, schemas, prompts, parsers, and policies;
- component tests for retrieval, model, and tools;
- end-to-end integration tests;
- offline quality on held-out, hard, and adversarial data;
- shadow, canary, and A/B online evaluation;
- load, resilience, safety, privacy, and cost tests.

An evaluation should block or inform a decision. Without a threshold, owner, and action, it is only decoration.

Build versioned eval sets from stratified real traffic, incidents, long tail, critical segments, no-answer cases, and adversarial variations. Synthetic data broadens coverage but cannot be the only truth. Prevent train/eval duplication and benchmark contamination; retain a stable core and rotating portion.

For generation, decompose “good” into factuality, relevance, completeness, instruction following, grounding/citations, style, safety, and correct abstention. Use anchored rubrics, double annotation on a sample, adjudication, and agreement measurement.

## Segments and online experiments

Report confidence intervals and sample sizes by country/language/device, new vs. frequent user, class/difficulty, tenant/source, version, input length, and protected group where legal and relevant. Averages can hide severe harm.

For A/B tests predeclare hypothesis, primary metric, guardrails, minimum detectable effect, sticky randomization unit, duration/power, exclusions, sample-ratio checks, and ramp plan. Distinguish statistical significance from practical value; watch novelty, carryover, interference, and learning effects.

## Four observability planes

1. **Infrastructure:** CPU/GPU/memory, saturation, queues, disk, network, restarts, quotas.
2. **Service:** QPS, p50/p95/p99, timeout/error, retries, cache hit, fallback, cost.
3. **Data/model:** schema, freshness, nulls, distributions, score drift, calibration, delayed performance, offline/online skew.
4. **Product/semantic:** conversion, task success, complaints, overrides, abstention, groundedness, tool failures, safety events.

Correlate by request/trace ID, model/data/prompt/index version, experiment, tenant, and region.

## Drift and alerting

Distinguish covariate P(X), label/prior P(Y), concept P(Y|X), prediction, and feedback/policy drift. Distribution tests are signals, not proof of performance loss. Compare against correct seasonality/window and confirm with mature labels when possible.

Every alert needs condition/window, severity/impact, owner, dashboard/traces, triage steps, mitigation/rollback, and resolution criteria. Prefer SLO burn-rate alerts and group symptoms by likely cause.

## Incident response

Declare an incident and commander; limit harm via rollback, kill switch, fallback, or rate limit; preserve evidence/timeline; diagnose by changes, versions, and segments; recover and verify semantic quality; communicate impact; write a blameless postmortem with owned actions.

## Security threat model

Assets include training data, weights, prompts, tools, credentials, outputs, and availability. Threats include poisoning/backdoors, adversarial evasion, extraction/inversion/membership inference, prompt injection, supply-chain compromise, exfiltration, tenant crossing, denial of wallet, and output injection.

Controls include provenance/checksums, RBAC/ABAC, least privilege, isolation, quotas/rate limits, anomaly detection, redaction, sandboxing, egress controls, approvals, signed artifacts, and immutable audit logs.

## Privacy, fairness, explainability

Privacy: data minimization and purpose, consent/legal basis, classification/residency, encryption, access audit, TTL/deletion, redaction/tokenization, and separation of training/evaluation/logging. Differential privacy, federated learning, secure aggregation, or enclaves are specialized options with utility and operational costs.

Fairness begins with the harm and population. Evaluate demographic parity, equal opportunity, equalized odds, calibration, or group error/coverage as appropriate; they cannot always coexist. Audit historical labels, representation, proxy features, and appeals.

Separate system transparency, global behavior, local reason, source evidence, and actionable explanation. Feature importance is not causality. High-risk decisions need exact version records, faithful reason codes, human review, and appeal.

Red-team multilingual/obfuscated prompts, poisoned documents, malicious tool arguments, cross-tenant access, extreme inputs, multi-turn jailbreaks, feedback poisoning, and downstream rendering/execution. Turn every confirmed issue into a regression test.
