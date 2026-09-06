# AI Systems Design Interview Preparation

This is a self-contained, end-to-end study pack for AI Systems Design interviews. It covers predictive ML, search, ads, recommendation, forecasting, feature platforms, serving (including LLM serving internals), generative AI, RAG, agents, alignment (RLHF/DPO), exploration/bandits, evaluation, MLOps, reliability, safety, privacy, and cost.

The goal is not to memorize architectures. It is to turn an ambiguous request into measurable requirements, select the simplest design that satisfies them, quantify scale, reason about data and model behavior, and defend trade-offs.

The examples use a ByteByteGo-style interview flow: clarify requirements, estimate capacity, draw a simple high-level design, define the data model/interfaces, then discuss scalability, performance, reliability, and resiliency. Start simple, get buy-in, and add detail only when a requirement or bottleneck justifies it.

## Recommended order

1. [Study plan and interview strategy](00_study_plan_and_strategy.md)
2. [Design framework and estimation](01_design_framework_and_estimation.md)
3. [ML foundations](02_ml_foundations.md)
4. [Data, features, and training](03_data_features_training.md)
5. [Serving, scalability, and reliability](04_serving_scalability_reliability.md)
6. [LLMs, RAG, and generative systems](05_llm_rag_and_generative_systems.md)
7. [Evaluation, observability, and safety](06_evaluation_observability_safety.md)
8. [MLOps, infrastructure, and cost](07_mlops_infrastructure_and_cost.md)
9. [Solved classical ML cases](08_solved_classical_ml_cases.md)
10. [Solved generative AI cases](09_solved_generative_ai_cases.md)
11. [Mock interviews and question bank](10_mock_interviews_and_questions.md)
12. [Interview cheat sheet](11_interview_cheat_sheet.md)
13. [Technical glossary](12_technical_glossary.md)

## How to study

For every case, make three passes:

1. **Read:** understand why each choice was made.
2. **Reconstruct:** close the notes and draw the solution in 35 minutes.
3. **Defend:** spend 10 minutes answering “why not the alternative?”, “how does it fail?”, and “how do you measure it?” aloud.

A practice interview should spend roughly 5-8 minutes clarifying scope, 10-15 minutes proposing a high-level design with quick estimates, 15-20 minutes on two or three deep dives, and 3-5 minutes wrapping up trade-offs, failure modes, and next steps.

## Definition of readiness

You should be able to:

- separate business, online, offline, and guardrail metrics;
- define labels without leakage and features available at prediction time;
- explain how offline and online paths remain consistent;
- estimate QPS, storage, bandwidth, memory/GPU needs, and approximate cost;
- size LLM capacity from tokens, KV-cache memory, and prefill-vs-decode, not QPS alone;
- distinguish alignment (RLHF/DPO) from fine-tuning, and exploration/bandits from exploitation;
- design graceful degradation, observability, rollback, and incident response;
- defend batch vs. streaming, sync vs. async, build vs. buy, and quality vs. latency/cost;
- design RAG with authorization, citations, evaluation, and injection defenses;
- adapt when the interviewer changes a requirement.

The central chain is:

> business goal → user experience → metrics → data/labels → model → serving → feedback → operations

## Diagram rendering

Architecture diagrams are checked in as SVG files under `images/` so GitHub renders them directly in Markdown without Mermaid support. Keep diagrams intentionally high level in the first pass; add caches, queues, shards, or extra model stages only when the surrounding example explicitly motivates them.
