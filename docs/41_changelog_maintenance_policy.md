# 41 Changelog Maintenance Policy

This document defines how `CHANGELOG.md` should be maintained after Stage 4 consolidation.

The goal is to prevent the changelog from becoming a duplicate of ROADMAP, Git history, audit notes, and detailed development logs.

## Current problem

`CHANGELOG.md` contains useful historical detail, but it is already too detailed to keep scaling linearly.

The project now has dedicated homes for most change types:

```text
ROADMAP.md -> staged development status
Git history -> exact commit-level history
docs/33 through docs/40 -> consolidation audits and source-of-truth routing
simulations/ -> reproducible toy sanity checks
notes/ -> evidence, literature, and maintenance notes
theory/ -> formal claims and coherence checks
```

Therefore, `CHANGELOG.md` should no longer try to record every document edit.

## New role of CHANGELOG

`CHANGELOG.md` should record milestone-level changes only.

It should answer:

```text
what changed at the project level
which major layer was added or completed
whether the change affects readers or source-of-truth structure
where details live
```

It should not answer:

```text
every file touched
every small wording change
every audit sub-step
every intermediate commit
```

## What belongs in CHANGELOG

Add a changelog entry for:

```text
new major theory layer
new formal claim or major correction
new practical protocol layer
new failure boundary system
new literature verification milestone
new visual explanation milestone
new simulation sanity-check milestone
new source-of-truth or repository policy milestone
Japanese sync milestone
public-facing release or version snapshot
```

## What does not belong in CHANGELOG

Do not add a changelog entry for:

```text
minor README link updates
single-line wording fixes
small routing edits
individual audit checklist items
CSV result corrections that do not change interpretation
small visual styling changes
internal file reordering
```

These should be left to Git history unless they affect project-level interpretation.

## Recommended entry format

Use compact milestone entries.

Template:

```markdown
## 0.x.y - Short milestone title

Summary:

- one or two sentences describing the project-level change.

Added:

- major new documents or directories only.

Changed:

- major source-of-truth or reader-facing changes only.

Interpretation:

- what this does and does not imply.

Details:

- links to ROADMAP, docs, notes, theory, simulations, or assets.
```

## Versioning policy

The existing changelog uses `0.7.x` style entries.

Going forward, either of these is acceptable:

```text
continue 0.8.x, 0.9.x, etc. for milestone entries
or use dated milestone headings when version precision is not useful
```

Recommended for this repository:

```text
use 0.x milestone numbers only when the change maps to ROADMAP stages
use dated headings for maintenance-only summaries
```

## Consolidation catch-up policy

Do not backfill every missed entry since `0.7.22`.

Instead, add one compact catch-up entry covering:

```text
Stage 3 rendered figures
Stage 4 project-note consolidation
v0.18 simulation sanity checks
```

This avoids turning the changelog into a duplicate of the full commit history.

## Source-of-truth routing

Detailed status should route as follows:

| Change type | Detail source |
|---|---|
| stage status | `ROADMAP.md` |
| source-of-truth routing | `docs/33` through `docs/40` |
| literature verification | `docs/17`, `notes/literature_verification.md`, `docs/22` through `docs/31` |
| visual explanation | `docs/32_visual_explanation_layer.md`, `assets/diagrams/`, `assets/figures/` |
| simulations | `docs/39_simulation_sanity_checks.md`, `simulations/` |
| formal theory | `theory/`, `docs/10_formal_refinement.md` |
| Japanese docs | `docs/ja/README.md` |

## Changelog wording rules

Avoid:

```text
proved
validated
confirmed
complete theory
empirical support
```

Use:

```text
recorded
first-pass complete
sanity-check demonstration
source-of-truth routing
reader-facing layer
maintenance policy
```

## Current decision

`CHANGELOG.md` should be kept.

It should not be deleted or fully rewritten.

But future updates should be milestone-level only.

The next safe changelog update is a single compact catch-up entry, not a long sequence of missed micro-entries.
