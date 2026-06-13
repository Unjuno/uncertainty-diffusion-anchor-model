# 36 Literature Claims Routing Audit

This document completes the first Stage 4 routing task for literature claims.

The goal is to prevent literature-related claims from drifting across README, overview, related-work notes, verification notes, visual summaries, and drafts.

## Routing principle

Literature claims should have two different homes:

```text
reader-facing support map -> docs/17_literature_support_map.md
maintenance verification checklist -> notes/literature_verification.md
```

Detailed verification notes remain in:

```text
docs/22 through docs/31
```

README and overview should only summarize literature status and route readers to the proper source.

## Source-of-truth split

| Claim type | Primary source | Supporting sources | README / overview behavior |
|---|---|---|---|
| Public claim about UDAM's relation to literature | `docs/17_literature_support_map.md` | `docs/08_related_work.md`, `docs/19_positioning_and_novelty.md` | link only; avoid details |
| Verification status for a specific literature area | `notes/literature_verification.md` | `docs/22` through `docs/31` | do not summarize beyond first-pass status |
| Full first-pass verification argument | relevant `docs/22` through `docs/31` file | `notes/literature_verification.md` | route only |
| Safe wording / avoid wording | `docs/17_literature_support_map.md` | `notes/literature_verification.md` | quote only short guardrails if needed |
| Visual support-strength summary | `assets/figures/literature_support_map.svg` | `assets/diagrams/literature_support_map.mmd`, `docs/32_visual_explanation_layer.md` | route visual readers there |
| Novelty claim | `docs/19_positioning_and_novelty.md` | `docs/17_literature_support_map.md` | keep concise |
| Draft paper or blog literature framing | `drafts/` | must cite `docs/17`, `notes/literature_verification.md`, and specific verification docs | downstream only; not source of truth |

## Current literature source roles

### `docs/17_literature_support_map.md`

Role:

```text
reader-facing graded support map
```

It should answer:

```text
which UDAM component is supported by which nearby literature area
whether support is direct, partial, analogy-only, not supported, or UDAM-specific
what wording should be avoided
```

It is the correct destination for readers asking:

```text
What parts of UDAM are supported by existing literature?
Which claims are overclaims?
Which parts remain UDAM-specific?
```

### `notes/literature_verification.md`

Role:

```text
maintenance checklist and verification ledger
```

It should answer:

```text
what has been checked
what the support level is
what caution wording is required
what future literature checks remain possible
```

It is not a polished bibliography.

### `docs/22` through `docs/31`

Role:

```text
detailed first-pass verification notes
```

These files should hold:

```text
one literature area per document
support classification
wording corrections
avoid statements
component-support versus full-synthesis caveats
```

## Allowed summary in README and overview

README and `docs/00_overview.md` may say only:

```text
literature verification: first-pass complete
component-level support exists at different strengths
component support does not prove the full UDAM synthesis
```

They should route to:

```text
docs/17_literature_support_map.md
notes/literature_verification.md
assets/figures/literature_support_map.svg
```

## Disallowed expansion in README and overview

Do not add to README or overview:

```text
full literature area summaries
citation lists
source-by-source comparisons
long support tables
new support classifications
claims that a literature proves UDAM
```

## Canonical support categories

Use these support categories consistently:

```text
direct support
partial support
analogy only
not supported
requires wording correction
UDAM-specific synthesis
```

Do not replace these with looser labels such as:

```text
proven
validated
confirmed
scientifically established
same as
```

## Canonical caution

Every literature-facing summary should preserve:

```text
component support does not prove full synthesis
```

and:

```text
UDAM is not proven by any single nearby literature
```

## Required routing for new literature claims

When adding a new literature-related claim:

```text
1. Add or update the relevant detailed verification document.
2. Update notes/literature_verification.md with status and caution wording.
3. Update docs/17_literature_support_map.md if the claim affects reader-facing support classification.
4. Update visual support map only if the support category changes in a major way.
5. Do not expand README or overview beyond a short status update and link.
```

## Current route decision

The current source-of-truth routing is acceptable.

No immediate content moves are required.

The main correction is procedural:

```text
future literature claims must route through docs/17 and notes/literature_verification.md before appearing in drafts or public summaries
```

## Stage 4 status update

Literature-claims routing audit: complete as first pass.

Next consolidation targets:

```text
route formal claims to theory/ and docs/10_formal_refinement.md
route visual claims to docs/32_visual_explanation_layer.md and assets/figures/
decide whether draft files need source-of-truth disclaimers
```
