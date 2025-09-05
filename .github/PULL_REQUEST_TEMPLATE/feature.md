# Feature PR — <feature-name>

**What**
- Short summary of the change (scope must be a small, testable chunk).

**Why now**
- User value + roadmap link (AI Expert / Orchestrator).

**Roadmap alignment**
- AI Expert: <evaluation|fairness|explainability>
- Orchestrator: <multi-cloud|governance|release hygiene>

**Files touched**
- List exact paths (keep minimal; unrelated code untouched).

**Risks & mitigations**
- <cost|drift|api-churn> and how you mitigated (caps, seeds, cleanup).

**Rollback**
- One-liner to revert this patch or disable feature if needed.

**How to run (one line)**
\python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r env\requirements.txt; <your-one-liner-here>; pytest -q tests\test_smoke.py\`n
**Acceptance criteria**
- What should pass (artifacts created, metrics logged, screenshots saved).

**Screenshots / artifacts**
- Paste leaderboard, configs, plots; list artifact paths under artifacts/.

---

## PR Checklist (repo)
- [ ] Scope is a small, testable chunk
- [ ] Files to touch are listed and limited
- [ ] Backup/rollback path documented
- [ ] Roadmap link noted (AI Expert and/or Orchestrator)
- [ ] Minimal diff; unrelated code untouched
- [ ] New/updated tests for changed behavior
- [ ] All tests pass locally
- [ ] Smoke run performed with expected outputs
- [ ] No version drift introduced without ADR
- [ ] README/CHANGELOG updated if needed
- [ ] ADR added/updated for decisions
- [ ] Env/run/test commands provided (one-line)
- [ ] Conventional commit message; labels set (e.g., roadmap:orchestrator, risk:cost, artifact:screenshot)

## Notes
- Link the GitHub Issue this PR closes (e.g., Closes #<id>).
- Mention any follow-ups (new issues) for out-of-scope items.

