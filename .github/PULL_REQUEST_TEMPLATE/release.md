# Release PR — vX.Y.Z

**What**
- Summarize the release (scaffold, notebooks, governance, ADRs, tests).

**Why now**
- Portfolio milestone aligned to AI Expert + Layer 2 Orchestrator roadmaps.

**Roadmap alignment**
- AI Expert: evaluation, fairness, explainability.
- Orchestrator: multi-cloud orchestration, governance, release hygiene.

**Files touched**
- CHANGELOG.md, README.md, docs/release-notes-<tag>.md (optional).

**Risk and rollback**
- Low; docs-only changes. Rollback by deleting tag and reverting CHANGELOG bump.

**How to test (one line)**
\python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r env\requirements.txt; python scripts\generate_synthetic_credit.py --rows 5000 --seed 42 --outdir data; pytest -q tests\test_smoke.py\`n
**Results / screenshots**
- Attach board screenshot (Release column), notebook previews, artifact paths.

---

## PR Checklist (repo)
- [ ] Scope is a small, testable chunk (release docs only)
- [ ] Files to touch are listed and limited
- [ ] Rollback path documented
- [ ] Roadmap link noted (AI Expert / Orchestrator)
- [ ] No unrelated code changes
- [ ] All tests pass locally (smoke)
- [ ] README/CHANGELOG updated
- [ ] ADRs added/updated if needed
- [ ] One-line setup/run/test provided
- [ ] Conventional commit message
- [ ] Labels set (roadmap:orchestrator, artifact:governance)

## Release Checklist (repo)
- [ ] CHANGELOG updated with version/date
- [ ] Repro run using one-liners (above)
- [ ] Artifact integrity checked (paths, sizes, sample outputs)
- [ ] Release notes drafted/attached
- [ ] Screenshots or demo links attached
- [ ] Next-step plan linked (issues/milestones)
- [ ] Tag created and pushed (e.g., vX.Y.Z)
- [ ] Release notes published

## Links
- Project board: Cross-Cloud AutoML Orchestration
- Relevant issues: #<init> #<aws> #<gcp> #<compare> #<rai> #<gov> #<release>

