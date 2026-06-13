# 33 Project Note Consolidation

This document starts Stage 4 of the five-stage refinement roadmap.

Stage 4 is not a theory-expansion stage.

Its purpose is to reduce navigation cost, clarify document ownership, and prevent the same claim from drifting across multiple files.

## Stage 4 goal

The repository now contains:

```text
core theory documents
formal notes
application playbooks
failure diagnostics
literature verification notes
visual explanation sources and figures
Japanese explanation files
paper/blog/project-note drafts
```

The next risk is not lack of content.

The next risk is fragmentation.

Stage 4 should therefore answer:

```text
Which document is the source of truth for each kind of claim?
Which documents are entry points?
Which documents are supporting notes?
Which documents are drafts or downstream presentations?
```

## Consolidation principle

Do not delete or rewrite large sections before assigning document roles.

First classify documents.

Then update links.

Then remove or compress duplication only when a clear source of truth exists.

## Source-of-truth map

| Claim type | Primary source | Supporting sources | Notes |
|---|---|---|---|
| Public entry point | `README.md` | `docs/00_overview.md` | README should stay short and route readers. |
| Conceptual overview | `docs/00_overview.md` | `FAQ.md` | Overview should explain the model without full proof burden. |
| Timer seed model | `docs/01_timer_model.md` | `docs/11_timer_three_layer_model.md`, `docs/13_deterministic_event_scope.md` | Keep `tau = K + U + R` stable. |
| Uncertainty diffusion | `docs/02_uncertainty_diffusion.md` | `docs/10_formal_refinement.md`, `theory/variables.md` | Avoid mixing cognitive uncertainty with physical state change. |
| Re-anchoring | `docs/03_reanchoring.md` | `docs/14_practical_reanchor_protocol.md`, `theory/propositions.md` | Preserve valid local re-anchor conditions. |
| Action value | `docs/04_action_value.md` | `theory/variables.md`, `theory/propositions.md` | Keep `V(a) = I(a) + B(a) - C(a)` consistent. |
| Propositions | `docs/05_propositions.md` | `theory/propositions.md`, `theory/proofs.md` | `theory/` remains the formal source. |
| Failure boundaries | `docs/06_failure_cases.md` | `docs/21_failure_decision_tree.md`, `theory/counterexamples.md` | Failure tree is the practical diagnostic. |
| Applications | `docs/07_applications.md` | `examples/`, `docs/15_application_cautions.md` | Examples should not expand theory silently. |
| Related work | `docs/08_related_work.md` | `docs/17_literature_support_map.md`, `notes/literature_verification.md` | Literature claims must remain graded. |
| Open questions | `docs/09_open_questions.md` | `ROADMAP.md` | Open questions should not imply unresolved core contradiction. |
| Formal refinement | `docs/10_formal_refinement.md` | `theory/` | Keep notation consistency here. |
| Practical protocol | `docs/14_practical_reanchor_protocol.md` | `docs/15_application_cautions.md`, `docs/16_adaptive_observation_cadence.md`, `docs/18_adaptive_expansion_factor.md` | Practical usage should route through cautions. |
| Literature verification | `notes/literature_verification.md` | `docs/22` through `docs/31`, `docs/17_literature_support_map.md` | Keep component support separate from full synthesis proof. |
| Visual explanation | `docs/32_visual_explanation_layer.md` | `assets/diagrams/`, `assets/figures/` | SVG is reader-facing; Mermaid is editable source. |
| Logical coherence | `theory/logical_synthesis_review.md` | `theory/consistency_review.md` | Logical review is the current coherence checkpoint. |
| Japanese explanation | `docs/ja/README.md` | `docs/ja/*` | Japanese expansion remains deferred until English stabilization. |
| Project drafts | `drafts/` | `README.md`, `docs/00_overview.md` | Drafts are downstream presentations, not source of truth. |

## Directory roles

### `docs/`

Readable explanation layer.

This is the main reader-facing theory layer.

It should answer:

```text
what the model says
how to use it
where it fails
how it relates to existing literature
```

### `theory/`

Formal source layer.

This directory should hold definitions, assumptions, variables, axioms, propositions, proofs, counterexamples, and logical consistency checks.

It should answer:

```text
what is formally claimed
what is assumed
what follows from what
what does not follow
```

### `notes/`

Research and maintenance layer.

This directory should hold origin notes, terminology, evidence hierarchy, verification notes, and maintenance policies.

It should answer:

```text
why claims are worded this way
how support levels are graded
what still needs checking
```

### `examples/`

Application layer.

Examples should illustrate the model, not silently change it.

Each example should preserve:

```text
state-informative != favorable
small != useful
local success != global expansion permission
```

### `assets/`

Visual asset layer.

Mermaid files in `assets/diagrams/` are source files.

SVG files in `assets/figures/` are rendered reader-facing outputs.

### `drafts/`

Presentation layer.

Drafts can translate the model into paper, blog, manifesto, or project-note form.

They should not become the source of formal claims.

## Duplication policy

Some repetition is useful.

The following claims may appear in multiple entry points:

```text
partial uncertainty does not imply total invalidation
lost anchor does not imply future anchor invalidation
state-informative != favorable
small != useful
local success != global expansion permission
component support does not prove full synthesis
```

But detailed derivations should have one primary home.

Recommended rule:

```text
repeat slogans, not derivations
repeat navigation, not full arguments
repeat warnings, not whole sections
```

## Documents that should remain short

These should route readers rather than carry all details:

```text
README.md
FAQ.md
docs/00_overview.md
docs/20_five_stage_development_roadmap.md
```

## Documents that may be long

These can hold detailed reasoning:

```text
docs/10_formal_refinement.md
theory/proofs.md
theory/logical_synthesis_review.md
docs/17_literature_support_map.md
notes/literature_verification.md
docs/22 through docs/31 literature verification files
```

## Stage 4 task list

Recommended first-pass consolidation tasks:

```text
1. Add this consolidation map.
2. Link it from README and ROADMAP.
3. Audit README for duplicated long explanations.
4. Audit docs/00_overview.md for duplicated long explanations.
5. Check that literature claims route to docs/17 and notes/literature_verification.md.
6. Check that formal claims route to theory/ and docs/10.
7. Check that visual claims route to docs/32 and assets/figures.
8. Leave Japanese synchronization for Stage 5.
```

## Non-goals for Stage 4

Stage 4 should not:

```text
add new UDAM concepts
expand Japanese documentation
turn drafts into source-of-truth documents
rewrite the whole repository in one pass
delete old notes before their replacement role is clear
```

## Current status

Stage 4 has started.

This document establishes the first consolidation map.

No documents are deprecated yet.

No Japanese synchronization is performed at this stage.
