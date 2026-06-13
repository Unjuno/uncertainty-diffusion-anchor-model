# 35 Overview Consolidation Audit

This document completes the first `docs/00_overview.md` audit task in Stage 4.

The goal is to decide whether the overview duplicates README or serves a distinct role as a slightly fuller conceptual introduction.

## Audit principle

`docs/00_overview.md` should not be a second README.

README should route.

Overview should explain.

The overview may repeat core slogans, but it should add conceptual boundaries that README does not need to carry.

Recommended rule:

```text
README = landing page
Overview = compact conceptual introduction
Detailed docs = source-of-truth explanations
```

## Current role of overview

The current overview provides:

```text
name
core claim
Japanese formulation
minimal timer intuition
visual entry point
timer seed scope
controllability boundary
model scope
minimal equations
high-stakes example policy
current status
```

This is broader than README's public routing role.

It is still short enough to serve as a compact conceptual overview.

## Section audit

| Overview section | Current role | Audit decision | Source-of-truth route |
|---|---|---|---|
| Name | identification | keep | `README.md` also repeats this intentionally |
| Core claim | conceptual thesis | keep | `README.md`, `docs/01_timer_model.md` |
| Japanese formulation | minimal bilingual bridge | keep short | `docs/ja/README.md` for full Japanese sync |
| Minimal intuition | timer seed explanation | keep | `docs/01_timer_model.md`, `docs/11_timer_three_layer_model.md` |
| Visual entry point | reader route | keep | `docs/32_visual_explanation_layer.md`, `assets/figures/README.md` |
| Timer seed scope | conceptual boundary | keep | `docs/13_deterministic_event_scope.md` |
| Controllability boundary | conceptual boundary | keep | `docs/10_formal_refinement.md`, `docs/15_application_cautions.md` |
| Model scope | applicability boundary | keep | `docs/15_application_cautions.md`, `docs/21_failure_decision_tree.md` |
| Minimal equations | compact formula index | keep short | `docs/10_formal_refinement.md`, `theory/variables.md` |
| Interpretation | formula explanation | keep short | `docs/01` through `docs/04` |
| High-stakes examples | safety boundary | keep | `notes/high_stakes_example_policy.md` |
| Current status | project snapshot | keep short | `README.md`, `ROADMAP.md` |

## Findings

The overview duplicates README in a few necessary entry points:

```text
name
core claim
visual entry route
current status
```

This duplication is acceptable because the overview is a conceptual entry document.

The overview's distinct value is in these sections:

```text
Timer seed scope
Controllability boundary
Model scope
High-stakes examples
```

These boundaries are more detailed than README but still short enough for an overview.

## Highest-risk sections for future bloat

The sections most likely to become too long are:

```text
Minimal intuition
Timer seed scope
Controllability boundary
Model scope
High-stakes examples
```

These should not accumulate full arguments.

They should route to deeper files once they need more detail.

## Keep as-is for now

The overview should remain as a compact conceptual introduction.

No sections need immediate removal.

No detailed derivations were found that must be moved immediately.

## Route, do not expand

Future edits should route as follows:

```text
Timer seed scope -> docs/13_deterministic_event_scope.md
Controllability boundary -> docs/10_formal_refinement.md and docs/15_application_cautions.md
Model scope -> docs/15_application_cautions.md and docs/21_failure_decision_tree.md
Minimal equations -> docs/10_formal_refinement.md and theory/variables.md
High-stakes examples -> notes/high_stakes_example_policy.md
Visual entry point -> docs/32_visual_explanation_layer.md and assets/figures/README.md
```

## Overview should avoid adding

Do not add the following to `docs/00_overview.md`:

```text
full proof sketches
full application examples
full literature grading
long diagrams or rendered figure embeds
new notation beyond the minimal equations
long Japanese explanations
complete failure taxonomy
complete high-stakes examples
```

## Overview may repeat

The overview may repeat short orientation claims:

```text
partial uncertainty does not imply total invalidation
future anchors still matter
UDAM is not a claim that every action is good
visual layer is a reader aid, not new theory
```

These repetitions are acceptable because overview is an entry document.

## README versus overview split

The intended split is:

```text
README: what is this repository and where should I start?
Overview: what is the model and what are its boundaries?
Detailed docs: what are the definitions, proofs, examples, and support claims?
```

## Current decision

`docs/00_overview.md` is acceptable for now.

It is not merely a README duplicate.

Its conceptual-boundary sections justify its existence.

Maintenance rule:

```text
future overview additions should usually be boundary clarifications or links, not new explanations
```

## Stage 4 status update

Overview duplication audit: complete as first pass.

Next consolidation targets:

```text
route literature claims to docs/17_literature_support_map.md and notes/literature_verification.md
route formal claims to theory/ and docs/10_formal_refinement.md
route visual claims to docs/32_visual_explanation_layer.md and assets/figures/
```
