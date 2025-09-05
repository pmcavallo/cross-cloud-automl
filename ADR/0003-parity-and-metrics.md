# ADR 0003: Parity rules & evaluation metrics
Date: 2025-09-05

## Context
Cross-cloud comparison requires identical data and common metrics.
## Decision
Fix target/feature set and deterministic splits. Report AUC, LogLoss, Accuracy, F1, PR-AUC, KS; record runtime/cost and explainability artifacts.
## Consequences
+ Fair comparison  − Fewer platform-specific extras.
## Rollback
If parity breaks, add a new ADR and annotate compare/comparison.md.
## Roadmap link
AI Expert + Orchestrator.
