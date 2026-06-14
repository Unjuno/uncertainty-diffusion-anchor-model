# 47 Remaining Work Register

This document records the remaining work after the first-pass agent guidance, notation audit, contraction-rule decision, publication-readiness audit, README/overview compression decision, roadmap update, changelog catch-up preparation, draft cleanup pass, minimal Japanese sync guardrail, extended toy simulation pass, visual rendering audit, release-history routing decision, repository completion check, and final repository audit.

The purpose is to keep the project in stabilization mode.

This document does not add new UDAM theory.

The current task is GitHub repository completion only.

## Current state

Completed in the latest stabilization pass:

```text
AGENTS.md added
README linked to AGENTS.md
README linked stabilization-pass documents from Development notes
README repository status refreshed for repository-completion scope
ROADMAP.md recorded v0.20 through v0.25 stabilization milestones
docs/42_changelog_catchup_entry.md extended with 0.8.0 through 0.11.0 compact entries
docs/43_notation_consistency_audit.md added
docs/44_contraction_rule_decision.md added
docs/45_publication_readiness_audit.md added
docs/46_readme_overview_compression_decision.md added
docs/48_stabilization_pass_summary.md added
docs/53_repository_completion_check.md added
docs/54_final_repository_audit.md added
drafts/paper_outline.md source-of-truth disclaimer added and abstract wording softened
drafts/blog_post_jp.md source-of-truth disclaimer added
drafts/short_manifesto.md source-of-truth disclaimer added
docs/ja/README.md source-of-truth status clarified
simulations/udam_extended_sanity_checks.py added
simulations/results/repeated_checking_mov_summary.csv added
simulations/results/boundary_risk_sensitivity_summary.csv added
simulations/results/extended_sanity_check_report.md added
docs/49_extended_simulation_sanity_checks.md added
simulations/README.md updated
docs/50_visual_rendering_audit.md added
assets/figures/README.md updated with older-diagram rendering policy
docs/51_release_history_routing_decision.md added
```

## Remaining work by priority

### P1. Final repository audit

Status:

```text
complete; pass with minor non-blocking notes
```

Completed:

```text
docs/54_final_repository_audit.md added.
No blocking repository-completion issue remains.
```

Do not:

```text
add external-publication drafts
add Quora-specific files
expand toward paperization
claim empirical validation
```

### P2. Repository completion check

Status:

```text
first-pass complete
```

Completed:

```text
docs/53_repository_completion_check.md added.
README.md repository status refreshed.
AGENTS.md and docs/48 now narrow scope to GitHub repository completion and stabilization.
```

### P3. Release history routing

Status:

```text
first-pass complete; CHANGELOG.md direct insertion deferred
```

Current source:

```text
docs/42_changelog_catchup_entry.md
```

Decision:

```text
Do not treat direct CHANGELOG.md catch-up insertion as a public-release blocker.
Use docs/42_changelog_catchup_entry.md as the catch-up ledger until CHANGELOG.md can be patched safely.
```

Do not:

```text
rewrite the whole changelog casually
backfill many micro-entries
turn CHANGELOG into ROADMAP or Git history
```

### P4. Draft cleanup

Status:

```text
first-pass complete
```

Current decision:

```text
Do not continue paperization unless explicitly requested.
Drafts remain downstream presentations, not source-of-truth files.
```

Do not:

```text
let drafts introduce stronger claims than theory/ or docs/17 support
```

### P5. Older diagram rendering

Status:

```text
first-pass audit complete; additional rendering deferred
```

Decision:

```text
Do not render every older Mermaid diagram now.
Render older diagrams only when a repository-facing route needs them.
```

Do not:

```text
turn visual work into theory authorization
```

### P6. Japanese sync

Status:

```text
minimal guardrail sync complete; full sync deferred
```

Remaining optional work:

```text
full Japanese synchronization only if needed for repository readability
Japanese examples only when they do not exceed English claim strength
```

Do not:

```text
expand Japanese docs beyond the stable English claim strength
```

### P7. Simulation extension

Status:

```text
first extended toy pass complete
```

Remaining optional work:

```text
only repository-facing plots or further toy sensitivity checks if they improve readability
```

Do not:

```text
present simulations as empirical validation
```

### P8. Empirical validation

Status:

```text
out of scope for current repository completion
```

Decision:

```text
Do not pursue empirical validation as part of this GitHub completion pass.
```

Do not:

```text
claim external validity from toy simulations
```

## Work no longer considered immediate blockers

These were addressed in first-pass form:

```text
agent editing guidance
notation consistency audit
contraction rule decision
README / overview compression decision
publication-readiness audit
roadmap stabilization recording
changelog catch-up preparation
release-history routing decision
remaining-work register
draft source-of-truth disclaimer insertion
minimal Japanese source-of-truth guardrail
extended toy simulation pass
older diagram rendering audit
repository completion check
final repository audit
```

## Current release posture

Repository can be treated as:

```text
a mostly completed GitHub theory repository with clear guardrails
```

Repository should not be treated as:

```text
a validated empirical model
a replacement for existing decision theory
a completed paper package
```
