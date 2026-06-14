# 47 Remaining Work Register

This document records the remaining work after the first-pass agent guidance, notation audit, contraction-rule decision, publication-readiness audit, README/overview compression decision, roadmap update, changelog catch-up preparation, draft cleanup pass, minimal Japanese sync guardrail, extended toy simulation pass, and visual rendering audit.

The purpose is to keep the project in stabilization mode.

This document does not add new UDAM theory.

## Current state

Completed in the latest stabilization pass:

```text
AGENTS.md added
README linked to AGENTS.md
README linked stabilization-pass documents from Development notes
ROADMAP.md recorded v0.20 through v0.25 stabilization milestones
docs/42_changelog_catchup_entry.md extended with 0.9.0 and 0.10.0 compact entries
docs/43_notation_consistency_audit.md added
docs/44_contraction_rule_decision.md added
docs/45_publication_readiness_audit.md added
docs/46_readme_overview_compression_decision.md added
docs/48_stabilization_pass_summary.md added
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
```

## Remaining work by priority

### P1. Safe CHANGELOG catch-up insertion

Status:

```text
prepared, not inserted
```

Source:

```text
docs/42_changelog_catchup_entry.md
```

Action:

```text
Insert the compact catch-up entries near the top of CHANGELOG.md only if the file can be patched safely.
```

Do not:

```text
rewrite the whole changelog casually
backfill many micro-entries
turn CHANGELOG into ROADMAP or Git history
```

### P2. Paper draft cleanup

Status:

```text
first-pass complete
```

Completed:

```text
drafts/paper_outline.md now states draft/source-of-truth status directly.
drafts/paper_outline.md now uses safer conditional title and abstract wording.
drafts/blog_post_jp.md now states draft/source-of-truth status directly.
drafts/short_manifesto.md now states draft/source-of-truth status directly.
```

Remaining optional work:

```text
full prose-level paper rewrite
citation insertion after literature sources are finalized
journal-style formatting
```

Do not:

```text
let drafts introduce stronger claims than theory/ or docs/17 support
```

### P3. Older diagram rendering

Status:

```text
first-pass audit complete; additional rendering deferred
```

Completed:

```text
docs/50_visual_rendering_audit.md classifies older Mermaid diagrams.
assets/figures/README.md now points to the rendering audit.
```

Decision:

```text
Do not render every older Mermaid diagram now.
Render older diagrams only when a publication, export, or reader-facing route needs them.
```

Priority candidate if rendering is later needed:

```text
failure_decision_tree.mmd
```

Do not:

```text
turn visual work into theory authorization
```

### P4. Japanese sync

Status:

```text
minimal guardrail sync complete; full sync deferred
```

Completed:

```text
docs/ja/README.md now states that English Markdown is the source of truth.
docs/ja/README.md now lists avoided overclaims in Japanese.
```

Remaining optional work:

```text
full Japanese synchronization after English wording stabilizes
Japanese examples only when they do not exceed English claim strength
```

Do not:

```text
expand Japanese docs beyond the stable English claim strength
```

### P5. Simulation extension

Status:

```text
first extended toy pass complete
```

Completed:

```text
repeated-checking MOV_i simulation
boundary-risk sensitivity simulation
extended toy simulation report
simulation README routing update
```

Remaining optional work:

```text
stochastic diffusion-and-reanchor time series
sensitivity analysis over observation-value parameters
public-facing plots if useful
```

Do not:

```text
present simulations as empirical validation
```

### P6. Empirical validation

Status:

```text
not started in a serious sense
```

Action:

```text
Only begin if there is a concrete empirical domain, operationalized variables, data plan, and falsifiable evaluation criterion.
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
remaining-work register
draft source-of-truth disclaimer insertion
minimal Japanese source-of-truth guardrail
extended toy simulation pass
older diagram rendering audit
```

## Current release posture

Repository can be treated as:

```text
a mostly stabilized English theory repository with clear guardrails
```

Repository should not be treated as:

```text
a validated empirical model
a clinical or financial decision protocol
a replacement for existing decision theory
a completed paper package
```
