# 12 — Technical Glossary

This glossary defines the technical vocabulary most likely to appear in an AI Systems Design interview. Definitions emphasize what a term means, why it matters to a system, and the trade-off it usually introduces.

## A

### A/B test

A randomized controlled online experiment in which traffic is assigned to a control or treatment and product outcomes are compared. Randomization supports causal conclusions when assignment is stable, sample sizes are adequate, and interference is controlled. An A/B test should declare a primary metric, guardrails, randomization unit, minimum detectable effect, duration, and stopping rule before launch.

### Abstention

A policy that lets a model decline to predict, answer, or act when confidence or evidence is inadequate. Abstention trades **coverage**—the fraction of requests answered—for lower risk. In high-risk systems, abstention commonly routes a case to a human, requests more information, or invokes a stronger model.

### Active learning

A labeling strategy in which the system selects particularly informative examples for human annotation, such as uncertain, novel, or disagreement-heavy cases. It can reduce labeling cost but may create a biased training distribution. Evaluation data must remain independently sampled.

### Agent

A model-driven system that chooses actions or tools dynamically, observes their results, and repeats until it reaches a stopping condition. A production agent needs bounded steps, time, tokens, and cost; tool authorization; state management; loop detection; auditing; and human approval for consequential actions. If the sequence is known in advance, a deterministic workflow is usually safer.

### ANN — Approximate Nearest Neighbor

A family of algorithms that retrieves vectors close to a query vector without comparing against every vector exactly. ANN trades some retrieval recall for much lower latency and compute. Common index families include HNSW and IVF/PQ. Always measure ANN recall against exact search on a representative sample.

### Autoregressive decoding

Generation in which a model produces one token at a time, conditioned on the input and all previously generated tokens. Because output tokens are sequential, decode latency behaves differently from parallel input processing, or **prefill**. This distinction is central to LLM throughput and capacity planning.

## B

### Backfill

Recomputing historical data, features, embeddings, predictions, or indexes for an earlier interval. Safe backfills use bounded partitions, controlled concurrency, versioned outputs, idempotent writes, reconciliation checks, and an atomic switch after validation.

### Backpressure

A mechanism that prevents producers from overwhelming slower consumers. It can include bounded queues, reduced intake, rate limiting, delayed processing, or load shedding. Without backpressure, overload often becomes unbounded memory usage and extreme tail latency.

### Bandit

An online decision strategy that balances exploiting known-good actions with exploring uncertain or new ones. Variants include ε-greedy, UCB, Thompson sampling, and contextual bandits. Bandits are the online complement to offline ranking: they discover value in items or treatments the current policy would never expose. Logged propensities are required to keep learning unbiased.

### Baseline

The simplest credible solution used as a comparison point: a constant predictor, business rule, popularity list, lexical search, or small model. A more complex model is justified only if it improves net utility over the baseline after latency, cost, risk, and operational burden are included.

### Batch inference

Generating predictions for many records on a schedule rather than during an interactive request. It is efficient, reproducible, and easy to retry, but its outputs can become stale and cannot use current request context.

### BM25

A lexical ranking function based on term frequency, inverse document frequency, and document-length normalization. It is strong for exact names, identifiers, and rare terms, making it a useful baseline and complement to dense semantic retrieval.

### Brier score

The mean squared difference between predicted probabilities and binary outcomes. It measures probabilistic accuracy and reflects both discrimination and calibration; lower is better.

## C

### Calibration

The degree to which predicted probabilities match observed frequencies. Among predictions near 0.8, a calibrated model should be correct about 80% of the time. Calibration matters whenever thresholds, risk, pricing, or human interpretation depend on probability. Platt scaling, isotonic regression, and temperature scaling are common post-training methods.

### Canary deployment

Sending a small fraction of real production traffic to a new model or system version before wider rollout. It limits blast radius and exposes production behavior. Canary metrics must include semantic quality and safety, not only service health.

### Candidate generation

The first stage of a large-scale search or recommendation system. It cheaply reduces millions of possible items to hundreds or thousands that a more expensive ranker can score. Candidate sources can include lexical search, ANN, collaborative filtering, popularity, follows, and exploration.

### Champion/challenger

A deployment pattern in which the current production model is the champion and one or more candidate models are challengers. Challengers are evaluated offline, in shadow mode, or on controlled traffic before promotion.

### Chunking

Dividing documents into retrieval units before embedding and indexing. Small chunks improve precision but lose surrounding context; large chunks preserve context but increase noise and token cost. Good chunking follows semantic structure and is tuned through retrieval and answer evaluation.

### Circuit breaker

A resilience mechanism that temporarily stops calls to a failing or overloaded dependency. It prevents repeated failures from consuming resources and worsening an incident. After a cooldown, a half-open state sends limited probes to test recovery.

### Concept drift

A change in the relationship between inputs and target, formally a change in `P(Y|X)`. A model can fail even if input distributions look stable. Concept drift is different from covariate drift and normally requires mature labels or reliable outcome proxies to detect.

### Context window

The maximum token sequence an LLM can process in one request, including system instructions, conversation history, retrieved evidence, tool results, and expected output. A larger context window does not guarantee better reasoning; it increases memory, latency, and cost and can introduce irrelevant evidence.

### Continuous batching

An LLM-serving technique that adds and removes requests from an active batch as sequences begin and finish, rather than waiting for the entire static batch. It improves accelerator utilization and throughput while preserving interactive streaming.

### Control plane

The part of a system that manages configuration, deployments, versions, permissions, policies, experiments, and routing. It is separate from the **data plane**, which processes actual requests and data. Separation reduces blast radius and allows controlled change.

### Covariate drift

A change in the input distribution `P(X)`. It signals that production data differs from a reference period, but does not prove model quality has degraded. Seasonality and product changes can create harmless covariate drift.

## D

### Data lineage

Metadata that records where data came from, how it was transformed, and which datasets, features, models, indexes, or outputs depend on it. Lineage supports debugging, auditing, reproducibility, impact analysis, and deletion requests.

### Data plane

The runtime path that ingests data or handles user requests and produces outputs. In an AI service it may include authorization, retrieval, feature lookup, inference, post-processing, and response delivery.

### Data poisoning

An attack or failure in which malicious or corrupted examples enter training data, retrieval corpora, or feedback and influence future behavior. Defenses include source provenance, access control, anomaly detection, robust evaluation, delayed promotion, and signed/versioned artifacts.

### Data parallelism

Distributed training in which each worker holds a copy of the model and processes a different subset of a batch, then synchronizes gradients. It scales well until communication or input throughput dominates.

### Dense retrieval

Retrieval based on similarity between learned vector embeddings. It captures semantic similarity and paraphrases better than exact lexical matching, but may struggle with rare identifiers and requires an ANN index at scale.

### Distillation

Training a smaller student model to reproduce the behavior or outputs of a larger teacher. It can reduce serving latency and cost, but the student may lose rare capabilities or inherit the teacher's errors and biases.

### Distribution shift

An umbrella term for production data or outcome relationships differing from training or reference data. It includes covariate, label/prior, and concept drift. The correct response depends on which distribution changed and whether performance is affected.

### DPO — Direct Preference Optimization

An alignment method that optimizes a policy directly on preference pairs (chosen vs. rejected responses) without training a separate reward model or running online reinforcement learning. It is simpler and more stable than classic RLHF and often competitive in quality, but the learned behavior is still bounded by the preference data it was trained on.

## E

### Embedding

A dense numerical vector representing semantic or structural properties of text, images, users, or items. Similar objects are intended to be near one another under a chosen distance metric. Embeddings support retrieval, clustering, recommendation, and similarity features; their model and version are part of the index contract.

### Error budget

The amount of unreliability allowed by an SLO. If availability target is 99.9%, the remaining 0.1% is the error budget. Teams can use its consumption rate to balance feature releases against reliability work.

### Exactly-once effect

The guarantee that an external operation has one final effect despite retries or duplicate delivery. It is typically achieved through idempotency keys, deduplication, transactions, checkpoints, and replay—not by merely selecting a queue advertised as exactly once.

### Exposure or impression log

A record of what a user was shown, at which position, by which model and experiment, before an outcome occurred. It is essential for unbiased ranking analysis, attribution, A/B tests, and feedback-loop reconstruction.

## F

### Feature

A measurable input supplied to an ML model, such as account age, seven-day transaction count, an embedding, or current device type. A valid feature must have a precise definition, owner, type, freshness expectation, and prediction-time availability.

### Feature store

A platform for defining, computing, discovering, and serving reusable ML features. It often contains an offline store for historical point-in-time training data, an online low-latency store, a registry, and materialization pipelines. It reduces reuse and parity problems but adds infrastructure and governance cost.

### Fine-tuning

Updating a pretrained model's parameters using task- or domain-specific examples. Fine-tuning is useful for stable behavior, style, format, or specialized tasks. It is generally not the best mechanism for frequently changing facts, document-level access control, source citations, or easy deletion; RAG is better suited to those requirements.

### Fallback

A safe lower-quality behavior used when the primary path is unavailable or too slow. Examples include a previous model, cached output, popularity ranking, lexical search, smaller LLM, or human handoff. Fallback rate must be monitored because it can conceal an outage.

### Flash Attention

An attention implementation that reduces memory usage and memory I/O by tiling the computation and recomputing intermediate values instead of materializing the full attention matrix. It enables longer context lengths and higher throughput at the same GPU memory, with no change to the model's mathematical output.

## G

### GQA / MQA — Grouped-Query / Multi-Query Attention

Attention variants that reduce the KV-cache footprint by sharing key/value heads. Multi-query attention uses a single shared K/V head; grouped-query attention has several query heads share one K/V head. Both shrink KV memory and can improve decode throughput at a possible small cost to quality relative to multi-head attention.

### Groundedness

The degree to which generated claims are supported by provided authoritative evidence. Groundedness is narrower than factuality: a statement may be true in the world but unsupported by the retrieved sources. In RAG, evaluate claim-level support and citation correctness.

### Guardrail

A metric, rule, or system control that limits unacceptable regressions while optimizing a primary objective. Examples include safety-event rate, complaint rate, fairness gaps, p99 latency, and maximum cost per successful task.

## H

### Hallucination

A generated statement that is unsupported, incorrect, fabricated, or inconsistent with the relevant evidence. Mitigations include retrieval, tools for authoritative facts, structured output, claim verification, uncertainty/abstention, and human review. Prompting alone cannot guarantee elimination.

### HNSW — Hierarchical Navigable Small World

A graph-based ANN index. Search traverses a hierarchy of proximity graphs to find nearby vectors quickly. HNSW often achieves high recall and low latency but consumes significant memory and can make large updates or distributed sharding operationally complex.

### Human-in-the-loop

A design in which humans label data, review uncertain outputs, approve consequential actions, adjudicate disagreements, or handle exceptions. The queue, priority, reviewer guidance, privacy, latency, and feedback quality are part of the system design.

### Hybrid retrieval

Combining lexical and dense retrieval, often followed by rank fusion and reranking. It covers both exact-term and semantic matches and is a common default for enterprise RAG and product search.

## I

### Idempotency

The property that repeating the same operation produces the same final effect as executing it once. Mutating APIs commonly accept an idempotency key and store the completed result so a timed-out client can retry without duplicating a payment, refund, or job.

### Inference

Running a trained model on input to obtain a prediction, ranking score, embedding, or generated output. Inference may be batch, streaming, nearline, or synchronous online.

### Inverse propensity weighting

A method for correcting exposure bias by weighting observed outcomes by the inverse probability that the existing policy exposed the item/action. It relies on logged propensities and becomes unstable when probabilities are very small.

### IVF/PQ — Inverted File Index / Product Quantization

An ANN approach that first assigns vectors to coarse clusters and searches selected clusters; product quantization compresses vectors into compact codes. It reduces memory and can scale to very large corpora, trading away some recall and requiring tuning of cluster/probe and quantization parameters.

## K

### KV cache

The cached attention keys and values for tokens already processed by a transformer during generation. It avoids recomputing the entire prefix for every new token. KV-cache memory grows with concurrent sequences, context length, layers, and model dimensions, often limiting LLM serving capacity.

## L

### Label

The target outcome used to train or evaluate a supervised model, such as fraud confirmed within 60 days, a completed view, or a defect verified by inspection. A label definition must include source of truth, horizon, maturity delay, attribution rules, and treatment of unobserved cases.

### Label leakage

Using information that directly or indirectly reveals the target but would not be available at prediction time. It creates unrealistically high offline performance and production failure.

### Latency percentiles

`p50`, `p95`, and `p99` are latency values below which 50%, 95%, and 99% of requests complete. Tail percentiles matter because averages can hide severe slowdowns affecting a meaningful number of users.

### LLM-as-a-judge

Using an LLM to grade another system's outputs against a rubric. It scales evaluation but can be biased by model family, answer order, verbosity, prompt wording, or shared errors. Calibrate against human judgments, blind identities/order, and never use it as the sole authority for safety-critical decisions.

### LoRA — Low-Rank Adaptation

A parameter-efficient fine-tuning technique that learns small low-rank update matrices while keeping most base-model weights frozen. It reduces training memory and storage but does not remove the need for representative data, evaluation, serving, or safety controls.

## M

### MoE — Mixture of Experts

An architecture in which only a subset of specialized "expert" networks is activated per token, selected by a routing function. It raises model capacity for a given inference FLOP budget, but routing decisions, load balancing across experts, memory (all experts must be resident), and uneven token-to-expert distribution add operational complexity.

### Model card

A document describing a model's intended use, training/evaluation data, metrics and segments, limitations, risks, owner, version, and operational constraints. A system card extends this to prompts, retrieval, tools, policies, and end-to-end behavior.

### Model registry

A versioned catalog of model artifacts and metadata, including provenance, metrics, approvals, feature schema, deployment state, and rollback target. It is a control-plane component rather than merely artifact storage.

### Model router

A component that selects a model or path based on task, risk, language, context length, latency, availability, or budget. Routing can reduce cost through cascades but needs evaluation of routing mistakes and consistent safety policies.

### Model parallelism

Splitting a model across accelerators because it does not fit or execute efficiently on one. Tensor and pipeline parallelism are variants. They introduce communication cost, topology constraints, and more complicated failure recovery.

### Multi-tenancy

Serving multiple customers or organizations on shared infrastructure while isolating their data, permissions, quotas, performance, encryption, logs, and costs. Tenant identity should come from authenticated credentials and be enforced at every storage, cache, index, and tool layer.

## N

### NDCG — Normalized Discounted Cumulative Gain

A ranking metric that rewards relevant items more when they appear near the top and supports graded relevance. Normalization makes scores comparable across queries with different ideal result quality.

### Negative sampling

Selecting a manageable subset of negative examples when all negatives are too numerous. In recommendation, unseen items are not automatically genuine negatives. Sampling policy changes the learned objective and may require correction or calibration.

## O

### Offline/online parity

Consistency between feature computation and preprocessing during training and production serving. Shared definitions, versioned schemas, compute-once/materialize-twice, and comparisons between logged online vectors and offline reconstruction reduce skew.

### Online learning

Updating a model continuously or frequently as new events arrive. It adapts rapidly but increases exposure to noise, poisoning, feedback loops, and hard-to-reproduce regressions. Guarded incremental learning and champion/challenger evaluation are essential.

### Orchestrator

A component that coordinates a multi-step pipeline or request: selecting retrieval, tools, models, retries, and state transitions. A deterministic orchestrator follows explicit workflows; an agentic one delegates more planning to a model.

## P

### Paged attention

A KV-cache memory-management scheme that allocates the cache in fixed-size pages rather than one contiguous block per request. It reduces fragmentation and waste, allowing more concurrent sequences to share a GPU and lowering serving cost.

### PEFT — Parameter-Efficient Fine-Tuning

A family of methods that adapt a model by updating only a small set of parameters while the base weights stay frozen. It drastically lowers training memory and storage and makes adapters cheap to swap, but still requires the same evaluation, serving, safety, and rollback controls as any model change.

### Point-in-time correctness

The property that every training example uses only feature values that were available at its historical prediction cutoff. It requires temporal joins against effective timestamps rather than joining to the latest value known today.

### Precision and recall

Precision is the fraction of predicted positives that are truly positive. Recall is the fraction of actual positives detected. Raising one often lowers the other through threshold changes. The correct operating point depends on false-positive and false-negative cost.

### Prefill

The relatively parallel LLM computation that processes all input tokens and initializes the KV cache before output generation. Time to first token includes prefill and queueing; long prompts directly increase it.

### Prefix/prompt caching

Reusing the KV cache of a shared prompt prefix (system instructions, few-shot examples, or a long preamble) across requests so the prefill computation is not repeated. It reduces cost and time-to-first-token for workloads with heavy common boilerplate, but cache keys must respect tenant and permission scope.

### Prompt

The complete input context supplied to a generative model. It can contain system instructions, developer/application rules, user content, examples, retrieved evidence, tool descriptions/results, and output constraints. It is broader than the user's visible message.

### Prompt engineering

The disciplined design, structuring, testing, and versioning of model inputs to elicit reliable behavior from a pretrained generative model **without changing its weights**. It is an empirical engineering activity: define desired behavior, construct instructions and context, evaluate on a representative set, inspect failures, and iterate under quality, latency, cost, and safety constraints.

A production prompt usually contains some of these elements:

1. **Role and objective:** the task and intended user outcome.
2. **Instruction hierarchy:** system/application constraints separated from user input.
3. **Context:** authoritative evidence, state, or retrieved documents clearly marked as data.
4. **Examples:** demonstrations of desired input-output behavior, or few-shot prompting.
5. **Output contract:** JSON schema, fields, citation format, length, or tone.
6. **Uncertainty policy:** when to ask a question, abstain, or escalate.
7. **Safety boundaries:** prohibited behavior and handling of untrusted input.

Common techniques include:

- **zero-shot prompting:** instructions without examples;
- **few-shot prompting:** examples included in context;
- **decomposition:** breaking a complex task into explicit stages;
- **structured prompting:** schemas or constrained outputs;
- **retrieval augmentation:** injecting relevant external evidence;
- **tool prompting:** describing typed operations the model may request;
- **self-consistency or sampling:** comparing multiple candidate outputs when the value justifies the extra cost.

Prompt engineering is not simply “writing clever wording,” and it cannot guarantee factual correctness, authorization, deterministic compliance, or safe external actions. Those require retrieval, tools, schema validators, policy enforcement, permissions, tests, and human review outside the model.

Prompts should be treated like software artifacts: version them with model, retriever, tool, and policy versions; review changes; test regressions; measure token cost and latency; use shadow/canary rollout; and preserve rollback. Evaluate task success, instruction adherence, format validity, safety, robustness to adversarial or unusual inputs, and performance across languages and segments.

Choose an alternative when appropriate:

- Use **RAG** when the problem is missing, changing, private, or citable knowledge.
- Use **fine-tuning** when stable behavior, style, or a repeated specialized task cannot be achieved reliably or economically in context.
- Use **deterministic code** for exact calculations, authorization, validation, and irreversible effects.
- Use **model routing or distillation** when prompt length/model size makes latency or cost unacceptable.

An interview-quality explanation is: “Prompt engineering controls behavior through versioned instructions, context, examples, and output constraints at inference time; it must be evaluated like code and reinforced with deterministic system controls because the prompt alone is not a security or correctness boundary.”

### Prompt injection

An attack in which untrusted text attempts to alter model instructions, reveal data, or cause unsafe tool use. It may be direct from a user or indirect through retrieved documents, web pages, emails, or tool output. Defenses require separation of instructions and data, least-privilege tools, external authorization, secret isolation, output validation, sandboxing, and adversarial testing. Telling the model to “ignore injection” is not sufficient.

### Prompt template

A parameterized prompt with fixed instructions and typed placeholders for user input, retrieved context, or application state. Templates improve consistency and versioning, but placeholders must preserve trust boundaries so untrusted content cannot masquerade as system instructions.

### Prompt tuning

A parameter-efficient adaptation method that learns continuous “soft prompt” vectors while keeping the base model frozen. Despite the similar name, it changes learned parameters and is different from manual prompt engineering.

### PR-AUC — Area Under the Precision-Recall Curve

A summary of precision-recall trade-offs across thresholds. It is usually more informative than ROC-AUC when the positive class is rare, though operating-point metrics are still necessary.

### Pruning

Removing parameters from a trained model to reduce size or latency. Structured pruning (dropping heads, layers, or channels) yields hardware speedups; unstructured pruning (zeroing individual weights) sparsifies the model but often needs sparse kernels to convert into real latency gains. Both require quality revalidation.

## Q

### QLoRA

A PEFT variant that quantizes the frozen base model (typically to 4 bits) while training low-rank LoRA adapters on top. It makes fine-tuning large models possible on much less memory, at some risk that quantization of the base model interacts with adapter quality.

### Quantization

Representing model weights, activations, or embeddings with fewer bits, such as int8 or int4 instead of fp16/fp32. It reduces memory and may increase throughput, with possible quality loss and hardware-dependent benefits.

## R

### RAG — Retrieval-Augmented Generation

A design in which external evidence is retrieved at request time and placed into a generative model's context. RAG supports changing/private knowledge, citations, and deletion without changing model weights. It consists of an ingestion/indexing path and a query/retrieval/generation path, both of which require separate evaluation.

### Rate limiting

Restricting requests or work per identity, tenant, route, or time window to protect capacity, fairness, cost, and security. Good limits distinguish interactive and batch traffic and return explicit retry behavior.

### Reranker

A more accurate, expensive model that reorders a small candidate set produced by retrieval. Cross-encoders jointly examine query and candidate and commonly improve search/RAG quality at the cost of latency.

### Reward hacking

A failure mode in which a policy optimized against a reward model (or proxy metric) exploits that model's blind spots rather than improving true behavior—for example, verbosity, sycophancy, or gaming a rubric. Mitigations include KL control toward a reference policy, diverse preference data, an uncontaminated evaluation set, and human spot-checks.

### RLAIF — Reinforcement Learning from AI Feedback

Using a model-generated preference signal, rather than human labels, to align a policy. It scales annotation but inherits the judge model's biases and errors, so its outputs still require human calibration for anything high-stakes.

### RLHF — Reinforcement Learning from Human Feedback

An alignment approach that first trains a reward model on human preference comparisons, then optimizes the policy (commonly with PPO) against that reward plus a KL penalty toward a reference model. It can improve instruction following and safety but is more complex, and its quality is bounded by the reward model and preference data.

### RPO and RTO

Recovery Point Objective is the maximum acceptable amount of data loss measured in time. Recovery Time Objective is the maximum acceptable time to restore service. They determine replication, backups, failover, and operational testing.

## S

### Semantic cache

A cache that reuses an answer or intermediate result when a new request is semantically similar rather than byte-identical. It can reduce LLM cost but risks stale, incorrect, personalized, or cross-tenant responses. Similarity threshold, ACL scope, version, TTL, and validation are critical.

### Shadow deployment

Sending copies of production inputs to a candidate system without using its outputs for real decisions. It measures latency, reliability, and disagreement under real traffic, but cannot establish causal product impact.

### SLI, SLO, and SLA

- **SLI:** measured indicator, such as successful-request ratio or p99 latency.
- **SLO:** internal target for that indicator.
- **SLA:** external commitment, often with contractual consequences.

### Speculative decoding

An LLM decoding optimization in which a small draft model proposes several candidate tokens and a large model verifies them in parallel. It accelerates generation when the draft agrees with the target often, without changing the output distribution, but adds complexity and only pays off when the two models are well aligned.

### Streaming inference

Continuously consuming events and updating predictions or state with low delay. It is useful when value decays quickly but adds ordering, state, watermark, replay, and backpressure complexity.

### Structured output

Model output constrained to a machine-readable schema such as JSON with typed fields. It reduces parsing ambiguity but does not guarantee semantic correctness; the application must validate schema, values, permissions, and business rules.

## T

### Temperature

A decoding parameter that scales token probabilities. Lower values make output more concentrated and often more repeatable; higher values increase diversity. Temperature zero does not guarantee identical output across model/runtime versions or distributed implementations.

### Thompson sampling

A bandit algorithm that maintains a posterior distribution over each action's reward and, on each decision, samples a value from each posterior and picks the action with the highest sample. It naturally balances exploration and exploitation and handles cold start well, but depends on a reasonable prior and reward model.

### Token

A unit of text processed by a language model, often a word fragment rather than a full word. Input and output tokens drive context limits, latency, KV-cache use, and API cost.

### Tool calling

A pattern in which a model emits a structured request to invoke an external function or API. The application validates authorization and arguments, executes the tool, and returns structured results. The model proposes; deterministic software authorizes and executes.

### Training-serving skew

A mismatch between data, features, or preprocessing used during training and those used during production inference. It often causes strong offline results and weak production behavior.

### TTFT — Time to First Token

Elapsed time from request arrival until the first generated token is returned. It includes queueing, routing, retrieval/tool work, and LLM prefill. It is a key perceived-latency metric for streaming applications.

## V

### Vector database

A storage and retrieval system optimized for vectors and similarity search, commonly with metadata filtering and ANN indexes. It is not automatically the source of truth for documents or permissions; original content, ACLs, and versions should remain authoritative elsewhere.

## W

### Watermark

In stream processing, an estimate that events earlier than a given event time have mostly arrived. It lets a system finalize windows while defining how much late data it tolerates and how later corrections are handled.

### Workflow

A predefined sequence or state machine of steps, validations, and branches. Workflows are preferable to agents when the process is known because they are more predictable, testable, and auditable.

## Quick distinction table

| Often-confused terms                 | Distinction                                                    |
|--------------------------------------|----------------------------------------------------------------|
| Prompt engineering vs. fine-tuning   | Changes inference-time context vs. changes model parameters    |
| Prompt engineering vs. prompt tuning | Human-designed text/context vs. learned soft-prompt parameters |
| RAG vs. fine-tuning                  | Retrieves current evidence vs. adapts stable behavior/task     |
| Dense vs. lexical retrieval          | Semantic vectors vs. term matching                             |
| Shadow vs. canary vs. A/B            | No effect vs. limited effect vs. causal comparison             |
| Calibration vs. accuracy             | Probability reliability vs. fraction correct                   |
| Covariate vs. concept drift          | `P(X)` changes vs. `P(Y\|X)` changes                           |
| Batch vs. streaming                  | Scheduled bounded data vs. continuous event processing         |
| Idempotency vs. deduplication        | Repetition is safe vs. duplicates are detected/removed         |
| SLO vs. SLA                          | Internal reliability target vs. external commitment            |
| Groundedness vs. factuality          | Supported by supplied evidence vs. true in the world           |
| Workflow vs. agent                   | Predetermined control flow vs. model-selected actions          |
| RLHF vs. DPO                         | Reward model + RL vs. direct preference optimization           |
| Prefill vs. decode                   | Parallel input processing vs. sequential token generation      |
| MHA vs. GQA/MQA                      | One K/V head per query head vs. shared K/V heads               |
| Pruning vs. quantization vs. distillation | Remove weights vs. fewer bits vs. train a smaller student |
