# ADR 0002: Cloud budget guardrails
Date: 2025-09-05

## Context
AutoML costs can spike; we need hard guardrails.
## Options
1) No caps  2) Soft caps (monitor)  3) Hard caps + cleanup
## Decision
Choose **hard caps** (Autopilot candidates/time; Vertex milli-node-hours + early stopping) and **mandatory cleanup** of endpoints/models/datasets.
## Consequences
+ Predictable cost  − Longer queues, fewer trials.
## Rollback
Relax caps behind a new ADR when justified.
## Roadmap link
Layer 2 Orchestrator.
