# 40 Draft Source-of-Truth Disclaimer Audit

This document completes the first Stage 4 audit for draft files.

The goal is to prevent paper, blog, manifesto, and project-note drafts from being mistaken for the source of UDAM's formal, literature, visual, or practical claims.

## Audit principle

Drafts are downstream presentations.

They may translate, compress, dramatize, or reorder UDAM for a specific audience.

They should not become source-of-truth documents.

Recommended rule:

```text
drafts present the model
drafts do not define the model
```

## Current draft inventory

| Draft file | Current role | Source-of-truth risk | Decision |
|---|---|---:|---|
| `drafts/paper_outline.md` | academic paper outline | medium | keep; route formal/literature claims to docs and theory |
| `drafts/blog_post_jp.md` | Japanese public-facing blog draft | medium | keep; mark Japanese draft as downstream and not synced source |
| `drafts/short_manifesto.md` | concise public statement | low-to-medium | keep; useful rhetorical summary, not formal source |
| `drafts/README.md` | draft directory index | high leverage | update with explicit source-of-truth disclaimer |

## Required disclaimer

The draft directory should state:

```text
Drafts are downstream presentations of UDAM.
They are not the source of formal claims, literature support claims, or repository policy.
If a draft conflicts with docs/, theory/, or notes/, the source-of-truth files override the draft.
```

## Source-of-truth routing from drafts

| Draft claim type | Source of truth |
|---|---|
| formal variables, equations, propositions, proofs | `theory/`, `docs/10_formal_refinement.md` |
| literature support and related work claims | `docs/17_literature_support_map.md`, `notes/literature_verification.md`, `docs/22` through `docs/31` |
| visual summaries | `docs/32_visual_explanation_layer.md`, `assets/diagrams/`, `assets/figures/` |
| simulation results | `docs/39_simulation_sanity_checks.md`, `simulations/` |
| practical protocol | `docs/14_practical_reanchor_protocol.md`, `docs/15_application_cautions.md` |
| failure boundaries | `docs/21_failure_decision_tree.md`, `docs/06_failure_cases.md`, `theory/counterexamples.md` |
| novelty and positioning | `docs/19_positioning_and_novelty.md` |
| Japanese explanations | `docs/ja/README.md` after later sync; current Japanese drafts remain downstream |

## Current decision

Do not edit every draft file individually in this pass.

Reason:

```text
A directory-level disclaimer is less intrusive.
The existing drafts are short enough to preserve.
The main risk is reader interpretation, not currently broken content.
```

Add or strengthen the disclaimer in:

```text
drafts/README.md
```

Individual draft disclaimers may be added later if drafts are published externally or expanded substantially.

## Drafts should avoid adding

Do not add the following to drafts unless the relevant source-of-truth files are updated first:

```text
new variables
new propositions
new empirical claims
new clinical or therapeutic claims
new literature support classifications
new simulation validation claims
claims that UDAM is proven
claims that UDAM is a complete replacement for decision theory
```

## Drafts may do

Drafts may:

```text
compress the core idea
adapt tone for a target audience
translate stable claims into public-facing language
outline a future paper
state memorable slogans
```

provided they preserve the current guardrails:

```text
partial uncertainty does not imply total invalidation
state-informative != favorable
small != useful
local success != global expansion permission
component support does not prove full synthesis
toy simulations are not empirical validation
```

## Stage 4 status update

Draft source-of-truth disclaimer audit: complete as first pass.

With this audit, the Stage 4 project-note consolidation checklist is first-pass complete.

Remaining future work is optional compression, not required source-of-truth routing.
