# 09 — Solved Generative AI Cases

## Case 1: Design a permission-aware enterprise knowledge assistant

### 1. Clarify and scope

Employees ask questions over internal documents from several repositories. Answers must cite sources and respect existing permissions. Assume 100k employees, 10 questions/user/day, 5× peak, p95 first token below 2 seconds, and 99.9% availability. Knowledge changes within minutes. The assistant is advisory and must abstain when evidence is weak.

V1 does not execute business actions or search the public web.

### 2. Metrics

- Business: self-service resolution and time saved, validated against support outcomes.
- Online: accepted/helpful answer, successful follow-up, escalation; guardrails for severe factual error, unauthorized disclosure, latency, and cost.
- Retrieval: recall@20/MRR on labeled sources, with zero ACL violation.
- Generation: correctness, groundedness, citation entailment, completeness, correct abstention.

### 3. Scale

One million queries/day ≈ 12 average QPS and perhaps 60 peak. If the average uses 2k input and 400 output tokens, raw work at peak is about 144k tokens/s; model/provider capacity and price require measured prefill/decode benchmarks and routing. Ten million chunks × 768 × 2 bytes ≈ 15 GB raw vectors, plus ANN/metadata/replicas—small enough for regional replicated indexes, though tenant/ACL strategy may drive partitioning.

### 4. Ingestion architecture

![4. Ingestion architecture](images/09_solved_generative_ai_cases_diagram_1_4-ingestion-architecture.svg)

Use source document ID, content hash, version, effective time, tenant, owner, language, path, and ACL. Incremental upserts avoid re-embedding unchanged chunks. Deletion/tombstones propagate to both indices, caches, and replicas. The original document/ACL store is source of truth; indices are rebuildable.

### 5. Query architecture

![5. Query architecture](images/09_solved_generative_ai_cases_diagram_2_5-query-architecture.svg)

Authorization is enforced at retrieval and again when resolving a source link. Never trust a tenant ID supplied in prompt text. Cache keys include tenant/access scope and policy version; avoid response caching for highly dynamic permissions.

Hybrid retrieval handles exact policy IDs and semantic questions. Retrieve perhaps 50 from each source, fuse, rerank top 50, and pack 5–10 non-duplicated chunks. Tune these values using component evaluation rather than intuition.

### 6. Prompt and correctness

The system prompt treats documents as untrusted evidence, not instructions; asks for supported claims and source IDs; requires “I do not have enough authorized evidence” when needed; and never invents links. The backend maps source IDs to URLs after permission checks.

Validate structured output, citation existence, and whether cited text supports claims. High-risk topics can use a specialized verifier or human escalation. The assistant should distinguish “no relevant document” from “a document may exist but is not accessible,” avoiding permission side channels.

### 7. Evaluation

Build a golden set from real questions across teams/languages, including outdated documents, conflicting sources, no-answer cases, revoked access, malicious document instructions, and users with different ACLs asking the same question.

Evaluate parsing, index freshness, retrieval, reranking, answer quality, citations, ACL safety, latency, and cost separately. Human experts adjudicate high-impact facts; calibrated LLM judges can scale routine rubric scoring. Online A/B tests compare resolution and time saved while guarding disclosure and complaints.

### 8. Threats and failures

- Prompt injection in documents: mark context untrusted, keep tools absent/allowlisted, never reveal secrets, detect suspicious instructions.
- Cross-tenant leak: identity-derived filtering at every store/cache, automated negative tests, audit logs.
- Poisoning: source allowlist, provenance, owner, version, anomaly review.
- Index down: lexical fallback or explicit temporary unavailability.
- Model saturation: smaller model, shorter context/output, queue/admission control.
- Parser failure: quarantine document; never publish corrupted extraction.
- Stale ACL: fail closed for sensitive sources and monitor propagation lag.

### 9. Rollout and evolution

Start read-only with one low-risk corpus. Offline eval → employee dogfood → small canary → department A/B. Use kill switches by corpus/model/retrieval source. Add conversational memory only with consent and TTL. Add tools later as separate workflows with scoped authorization and confirmation.

Why not fine-tune on all documents? Knowledge and permissions change frequently, deletion is difficult, citations are weaker, and training-time memorization can leak. Fine-tuning may later improve format or task behavior, while RAG remains the knowledge path.

---

## Case 2: Design an AI customer-support agent that can issue refunds

### 1. Clarify and risk-tier the product

The assistant answers support questions, checks orders, troubleshoots, and may issue eligible refunds. Assume chat p95 first token below 2 seconds, but tool actions can take longer. A wrong answer is recoverable; an unauthorized refund or disclosure is not. Human agents are available.

Decompose autonomy:

- Tier 0: answer from approved knowledge.
- Tier 1: read-only tools such as order status.
- Tier 2: reversible/low-value actions under deterministic policy.
- Tier 3: high-value or ambiguous cases require explicit human approval.

### 2. Metrics

- Business: correctly resolved contacts and handling-time savings net of refund/incident cost.
- Product: first-contact resolution, escalation, customer satisfaction.
- Agent: task completion by scenario, plan/tool selection, argument accuracy.
- Guardrails: unauthorized action rate (target zero), over-refund value, repeat contact, disclosure, safety, latency, cost.

Containment alone is dangerous: an agent can avoid escalation by giving bad answers.

### 3. Architecture

![3. Architecture](images/09_solved_generative_ai_cases_diagram_3_3-architecture.svg)

The LLM proposes actions; a deterministic policy service checks identity, ownership, item, time window, previous refunds, amount limits, jurisdiction, risk signals, and agent version. The payment system accepts an idempotency key derived from case/action, preventing duplicate refunds after retry.

### 4. State and tool contracts

Maintain server-side case state, not hidden prompt state: authenticated customer/account, order selection, verified facts, actions proposed/executed, approvals, and budget. Tools have typed schemas, minimum permissions, timeouts, structured error codes, and redacted outputs. The model never receives payment credentials or unrestricted database/query tools.

Use a bounded loop with maximum steps, tokens, wall time, and spend. Repeated tool calls trigger loop detection and escalation. Cancellation propagates; partial state is checkpointed.

### 5. Knowledge and conversations

RAG retrieves only current, approved policies filtered by market/product/date. Citations can be internal while the user receives a concise explanation. Summaries reduce context but are treated as fallible; authoritative state comes from backend systems. Persistent memory is opt-in and should not store payment or sensitive support details unnecessarily.

### 6. Evaluation

Create multi-turn scenario suites:

- eligible and ineligible refunds;
- partial/duplicate orders;
- user changes order midway;
- tool timeouts and conflicting state;
- malicious requests and injected order notes;
- policy changes;
- ambiguous identity and account takeover;
- cancellation immediately before execution.

Score final resolution, factual statements, tool sequence, argument correctness, policy compliance, unnecessary steps, and side effects. Run tools in a simulator for deterministic replay. Red-team prompt injection through customer messages and tool-returned text.

Shadow mode lets the agent recommend actions beside human agents without execution. Then canary read-only, then tightly capped refundable amounts with review. Compare to human baseline and inspect every early action.

### 7. Failure and recovery

- LLM/model down: static help/search and human handoff.
- RAG down: read-only tools still work, but do not improvise policy.
- order tool down: state outage, create resumable case, no action.
- payment timeout: query idempotency key/status before retry.
- policy service unavailable: fail closed for refunds.
- suspicious behavior: lock action path, preserve audit, escalate.

### 8. Key design reasoning

The strongest decision is not which LLM to use. It is separating probabilistic planning from deterministic authorization and execution, constraining autonomy by risk, and making every side effect auditable, idempotent, confirmable, and recoverable.

---

## Case 3: Design a high-volume meeting summarization system

### Requirements and design

Upload recordings up to two hours; return transcript, chaptered summary, decisions, and action items within five minutes after upload. This is asynchronous. Use a job ID, progress, cancellation, webhook, and idempotency key.

![Requirements and design](images/09_solved_generative_ai_cases_diagram_4_requirements-and-design.svg)

Process audio in overlapping chunks; reconcile timestamps/speakers. Summarize chunks, then synthesize a global summary with references to transcript spans. Extract action items into a schema with owner, action, due date, evidence span, and confidence. Do not infer an owner/date when absent.

Scale workers independently for transcoding, ASR, and LLM stages; use queue age for autoscaling, checkpoint each stage, and send poison jobs to a dead-letter/review queue. Avoid retrying the whole two-hour job. Tenant quotas, maximum media length, and budget prevent denial of wallet.

Evaluate word error rate by language/noise, speaker attribution, decision/action precision and recall, unsupported claim rate, end-to-end completion time, cost per audio hour, and human edit distance. Test cross-talk, accents, names, silence, corrupted media, and prompt injection spoken in the meeting.

Privacy requires explicit consent, tenant isolation, encryption, short-lived signed URLs, retention/deletion, redacted logs, and a clear policy on provider training. For sensitive customers, offer regional/self-hosted processing. If synthesis fails, return a transcript and partial summary rather than lose completed work.
