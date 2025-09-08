# ADR: AWS Autopilot Guardrails

**Title:** AWS Autopilot Guardrails  
**Date:** 2025-09-08  

## Context  
Running AWS SageMaker Autopilot without constraints can lead to runaway costs and idle resources (endpoints left running). For a fair cross-cloud shootout, we need consistent budget caps and cleanup protocols across AWS and GCP.  

## Options  
1. Unlimited search / default runtime (risk: unpredictable costs).  
2. Cap max candidates and runtime; batch predictions only; manual cleanup.  
3. Use managed endpoints for inference (risk: ongoing charges).  

## Decision  
We chose option 2:  
- Cap **max candidates = 10**  
- Cap **max runtime = 30 minutes**  
- Use **Batch Transform** only (no persistent endpoints)  
- Cleanup all endpoints, models, transform jobs post-run  
- Attribute costs explicitly (September AWS bill = , fully project-bound)  

## Consequences  
- Costs predictable and bounded within free-tier safety.  
- Tradeoff: potentially missing best model due to early cutoff, but ensures reproducibility and comparability with GCP Vertex AI.  
- Documentation updated (README, CHANGELOG) to record results, screenshots, and costs.  

## Rollback  
If stricter guardrails harm model quality, relax candidate/runtime caps (with ADR amendment). If Autopilot costs exceed expectations, fall back to a smaller dataset slice.  

## Roadmap Link  
- **AI Expert Roadmap:** Demonstrates cost-aware ML automation with explainability.  
- **Layer 2 Orchestrator Roadmap:** Enforces cross-cloud budget parity and governance.  

