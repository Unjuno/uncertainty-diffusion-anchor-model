# 47 Remaining Work Register

This document records the remaining work after the first-pass agent guidance, notation audit, contraction-rule decision, publication-readiness audit, README/overview compression decision, roadmap update, changelog catch-up preparation, draft cleanup pass, minimal Japanese sync guardrail, extended toy simulation pass, visual rendering audit, release-history routing decision, repository completion check, final repository audit, Japanese sync update, repository-facing simulation plots, and additional toy sensitivity check.

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
docs/55_repository_simulation_plots_and_sensitivity.md added
docs/ja/06_repository_status_and_simulations.md added
docs/ja/README.md source-of-truth status and simulation routing refreshed
simulations/udam_extended_sanity_checks.py added
simulations/udam_repository_sensitivity_checks.py added
simulations/plot_sanity_checks.py added
simulations/results/repeated_checking_mov_summary.csv added
simulations/results/boundary_risk_sensitivity_summary.csv added
simulations/results/observation_cost_threshold_sensitivity.csv added
simulations/results/extended_sanity_check_report.md added
simulations/results/repository_sensitivity_check_report.md added
simulations/plots/README.md added
simulations/plots/repeated_checking_mov.svg added
simulations/plots/boundary_risk_sensitivity.svg added
simulations/plots/observation_cost_threshold.svg added
.github/workflows/simulation-plots.yml added
simulations/README.md updated
assets/figures/README.md updated with older-diagram rendering policy
docs/49_extended_simulation_sanity_checks.md added
docs/50_visual_rendering_audit.md added
docs/51_release_history_routing_decision.md added
```

## Remaining work by priority

### P1. Japanese sync

Status:

```text
repository-facing sync complete
```

Completed:

```text
docs/ja/06_repository_status_and_simulations.md added.
docs/ja/README.md now links the repository status and simulation note.
Japanese docs preserve English Markdown as source of truth.
```

Do not:

```text
expand Japanese docs beyond the stable English claim strength
```

### P2. Repository-facing simulation plots

Status:

```text
complete
```

Completed:

```text
simulations/plot_sanity_checks.py added
simulations/plots/README.md added
simulations/plots/repeated_checking_mov.svg added
simulations/plots/boundary_risk_sensitivity.svg added
simulations/plots/observation_cost_threshold.svg added
.github/workflows/simulation-plots.yml added
```

Do not:

```text
present plots as validation
```

### P3. Additional toy sensitivity check

Status:

```text
complete
```

Completed:

```text
observation-cost threshold sensitivity added
simulations/udam_repository_sensitivity_checks.py added
simulations/results/observation_cost_threshold_sensitivity.csv added
simulations/results/repository_sensitivity_check_report.md added
docs/55_repository_simulation_plots_and_sensitivity.md added
```

Interpretation boundary:

```text
higher signal accuracy raises the break-even observation cost in the toy setup
not: more observation is always better
```

### P4. Release history routing

Status:

```text
first-pass complete; CHANGELOG.md direct insertion deferred
```

Decision:

```text
Do not treat direct CHANGELOG.md catch-up insertion as a public-release blocker.
Use docs/42_changelog_catchup_entry.md as the catch-up ledger until CHANGELOG.md can be patched safely.
```

### P5. Empirical validation

Status:

```text
out of scope for current repository completion
```

Decision:

```text
Do not pursue empirical validation as part of this GitHub completion pass.
```

## Work no longer considered immediate blockers

These were addressed in first-pass or repository-facing form:

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
Japanese repository-status sync
repository-facing simulation plots
additional toy sensitivity check
CI simulation plot workflow
```

## Current release posture

Repository can be treated as:

```text
a completed GitHub theory repository with clear guardrails and repository-facing toy simulation plots
```

Repository should not be treated as:

```text
a validated empirical model
a replacement for existing decision theory
a completed paper package
```
