# 47 Remaining Work Register

This document records the remaining work after the first-pass agent guidance, notation audit, contraction-rule decision, publication-readiness audit, README/overview compression decision, roadmap update, and changelog catch-up preparation.

The purpose is to keep the project in stabilization mode.

This document does not add new UDAM theory.

## Current state

Completed in the latest stabilization pass:

```text
AGENTS.md added
README linked to AGENTS.md
README linked stabilization-pass documents from Development notes
ROADMAP.md recorded v0.20 through v0.23 stabilization milestones
docs/42_changelog_catchup_entry.md extended with a 0.9.0 compact entry
docs/43_notation_consistency_audit.md added
docs/44_contraction_rule_decision.md added
docs/45_publication_readiness_audit.md added
docs/46_readme_overview_compression_decision.md added
docs/48_stabilization_pass_summary.md added
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
not complete
```

Action:

```text
Use AGENTS.md and docs/43_notation_consistency_audit.md as constraints.
Make drafts present the model without defining it.
```

Do not:

```text
let drafts introduce stronger claims than theory/ or docs/17 support
```

### P3. Optional older diagram rendering

Status:

```text
optional
```

Action:

```text
Render older non-Stage-3 Mermaid diagrams only if they are still reader-facing.
```

Do not:

```text
turn visual work into theory authorization
```

### P4. Japanese sync

Status:

```text
deferred
```

Action:

```text
Translate stable English claims conservatively after English source routing and notation remain stable.
```

Do not:

```text
expand Japanese docs beyond the stable English claim strength
```

### P5. Simulation extension

Status:

```text
optional / future
```

Possible work:

```text
repeated-checking MOV_i simulation
stochastic diffusion-and-reanchor time series
boundary-risk parameter sensitivity analysis
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
