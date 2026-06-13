# 37 Formal Claims Routing Audit

This document completes the first Stage 4 routing task for formal claims.

The goal is to prevent formal claims, equations, variables, propositions, proofs, and counterexamples from drifting across README, overview, docs, theory notes, and drafts.

## Routing principle

Formal claims should have two layers:

```text
formal source layer -> theory/
reader-facing formal explanation -> docs/10_formal_refinement.md
```

README and overview should only summarize core formulas and route readers to the proper source.

## Source-of-truth split

| Claim type | Primary source | Supporting sources | README / overview behavior |
|---|---|---|---|
| Variable definitions and notation | `theory/variables.md` | `docs/10_formal_refinement.md` | show only minimal formulas |
| Assumptions | `theory/assumptions.md` | `docs/10_formal_refinement.md` | route only |
| Axioms | `theory/axioms.md` | `docs/05_propositions.md` | route only |
| Propositions | `theory/propositions.md` | `docs/05_propositions.md` | route only or cite short proposition names |
| Proof sketches / derivations | `theory/proofs.md` | `docs/10_formal_refinement.md` | do not include in README or overview |
| Counterexamples | `theory/counterexamples.md` | `docs/06_failure_cases.md`, `docs/21_failure_decision_tree.md` | route through failure docs |
| Logical synthesis and consistency | `theory/logical_synthesis_review.md` | `theory/consistency_review.md` | keep only short status in README |
| Formal refinement for readers | `docs/10_formal_refinement.md` | `theory/` | route readers here for compact formal explanation |
| Visual formula summaries | `docs/32_visual_explanation_layer.md`, `assets/figures/` | `theory/variables.md`, `theory/propositions.md` | visual summary only; not source of formal claims |
| Draft paper or blog formulas | `drafts/` | must route to `theory/` and `docs/10` | downstream only; not source of truth |

## Current formal source roles

### `theory/variables.md`

Role:

```text
notation and variable source of truth
```

It should answer:

```text
what each symbol means
what assumptions or domains each variable has
which notation should be avoided because of collision risk
```

This file is the primary source for symbols such as:

```text
K, U, R, tau
P_t, Q, Q_total
V(a), I(a), B(a), C(a)
OV, MOV_i
s_i, r_i, P_boundary(i), C_boundary, C_correct(r_i)
```

### `theory/propositions.md`

Role:

```text
proposition source of truth
```

It should answer:

```text
what UDAM formally claims
what conditions each proposition requires
what each proposition means in plain language
```

New proposition-like claims should not first appear in README, overview, examples, or drafts.

They should be added here or explicitly marked as informal.

### `theory/proofs.md`

Role:

```text
proof and derivation source of truth
```

It should answer:

```text
why the propositions follow under stated assumptions
where a proposition is only a proof sketch
which claims are not fully formalized
```

README and overview should not contain proof sketches.

### `theory/counterexamples.md`

Role:

```text
formal counterexample and boundary source
```

It should answer:

```text
when the model fails
which claims are not universally true
which assumptions are necessary
```

Practical failure documents may explain the same boundaries, but formal counterexamples belong here.

### `docs/10_formal_refinement.md`

Role:

```text
reader-facing formal refinement map
```

It should answer:

```text
how the formal layers fit together
which representation is currently core
which extensions are deferred
which equations are central enough for readers to know
```

This document is not the final formal source for every variable or proposition.

It is the compact reader-facing bridge into `theory/`.

## Allowed summary in README and overview

README and `docs/00_overview.md` may show only the minimal formula set:

```text
tau = K + U + R
P_{t+Delta t} = P_t + Q Delta t
V(a) = I(a) + B(a) - C(a)
OV = E_y[max_a E[V(a,S) | y]] - max_a E[V(a,S)] - C(obs)
s_{i+1} = r_i s_i
B_expand(r_i) + I_expand(r_i) > C_obs(r_i) + P_boundary(i) C_boundary + C_correct(r_i)
```

They should route detailed formal interpretation to:

```text
docs/10_formal_refinement.md
theory/variables.md
theory/propositions.md
theory/proofs.md
theory/counterexamples.md
theory/logical_synthesis_review.md
```

## Disallowed expansion in README and overview

Do not add to README or overview:

```text
new variables
new propositions
proof sketches
full derivations
formal extensions not yet represented in theory/
long notation discussions
simulation claims
empirical validation claims
```

## Canonical formal cautions

Every formal-facing summary should preserve:

```text
state-informative != favorable
OV > 0 is required for favorable observation
MOV_i > 0 is required for repeated observation
local success does not imply global expansion permission
r_i is selected, not automatically 2
component support does not prove full synthesis
```

## Required routing for new formal claims

When adding a new formal claim:

```text
1. Add or update notation in theory/variables.md if new symbols are introduced.
2. Add or update assumptions in theory/assumptions.md if the claim depends on new conditions.
3. Add or update theory/propositions.md if the claim is proposition-like.
4. Add or update theory/proofs.md if the claim has a derivation.
5. Add or update theory/counterexamples.md if the claim has clear failure conditions.
6. Update docs/10_formal_refinement.md only after the formal source layer is stable.
7. Keep README and overview limited to short formulas and links.
```

## Current route decision

The current source-of-truth routing is acceptable.

No immediate content moves are required.

The main correction is procedural:

```text
future formal claims must enter through theory/ before appearing as stable claims in docs, drafts, README, or overview
```

`docs/10_formal_refinement.md` remains the best reader-facing map of the formal layer, but it should not replace `theory/` as the formal source.

## Stage 4 status update

Formal-claims routing audit: complete as first pass.

Next consolidation targets:

```text
route visual claims to docs/32_visual_explanation_layer.md and assets/figures/
decide whether draft files need source-of-truth disclaimers
```
