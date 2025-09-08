# Cross-Cloud AutoML + Responsible AI
## AWS SageMaker Autopilot Results
- Guardrails: 10 candidates, 30m runtime
- Best model: ID `oRfFOwTwTv1ez-010...` (F1 optimized)
- Artifacts: [metrics.json](artifacts/aws/metrics.json), [predictions.csv](artifacts/aws/predictions.csv)
- Optimized metric: **F1** (class imbalance baseline).
- Cost attribution: **Sep 2025 = $10.22** (SageMaker $8.614 + EC2/VPC/S3 ≈ $1.61); this repo was the sole Sept usage.
- Smoke check (one line):  
  `Get-Item artifacts/aws/metrics.json, artifacts/aws/predictions.csv, aws/screenshots/*.png | Select-Object Name, Length`

## [Unreleased]
- feat(aws): Autopilot run complete with metrics, predictions, and explainability
