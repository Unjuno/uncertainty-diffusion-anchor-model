# 32 Visual Explanation Layer

This document begins Stage 3 of the five-stage refinement roadmap.

Stage 3 is not intended to add new theory.

Its purpose is to make the existing theory readable at a glance.

## Stage 3 goal

The current repository has enough theory and first-pass literature verification to support the core UDAM structure.

The next bottleneck is reader comprehension.

A reader should be able to see the basic UDAM logic before reading the full formal notes.

The visual layer should therefore explain:

```text
anchor loss -> uncertainty diffusion -> valid local observation -> conditional action -> repeated observation boundary -> risk-constrained expansion
```

## Visual principles

Use diagrams to reduce cognitive load, not to hide assumptions.

Each diagram should:

```text
show one decision layer only
make failure points visible
avoid implying automatic expansion
avoid implying that any observation is useful
avoid implying that small action is always valid
```

The visual layer should preserve the core corrections from the literature verification stage:

```text
state-informative != favorable
small != useful
feedback-producing != favorable
local success != global expansion permission
robust != optimal
execution support != value support
epistemic value != automatic favorability
successive approximation != boundary-risk permission
```

## First visual artifact

The first Stage 3 diagram is:

```text
assets/diagrams/one_page_udam_flow.mmd
```

It is intended as a compact entry-point diagram.

It does not replace the detailed diagrams already present in `assets/diagrams/`.

It summarizes the full flow as one page:

```text
1. Start from anchor loss.
2. Avoid global invalidation.
3. Name the target state.
4. Take one valid local observation or small bounded action.
5. Check whether the result is state-informative.
6. Check whether it changes feasible action.
7. Check value versus cost.
8. Decide: stop, switch, observe again, or expand.
9. If expanding, re-check boundary risk.
10. Never infer global safety from local success alone.
```

## Diagram inventory for Stage 3

Planned Stage 3 visual set:

| Diagram | Purpose | Status |
|---|---|---:|
| `one_page_udam_flow.mmd` | compact full flow from anchor loss to risk-constrained expansion | added |
| anchor-loss-to-reanchor timeline | show `K + U + R` visually | planned |
| observation-value decision diagram | show `OV > 0` and action change | planned |
| expansion-with-boundary-risk diagram | show why expansion is not automatic doubling | planned |
| literature-support map figure | show which components are directly supported, partial, analogy-only, unsupported | planned |

## Intended reader path

Recommended reader order after Stage 3 begins:

```text
README
-> one-page UDAM flow diagram
-> failure decision tree
-> logical synthesis review
-> literature support map
-> detailed formal notes
```

## One-page diagram text

The one-page diagram should keep labels short.

Preferred node labels:

```text
Anchor lost
Do not globally invalidate
Name target state S
Valid local observation y?
State-informative?
Action changes?
Value > cost?
Stop / switch / observe again / expand
Boundary risk acceptable?
Expand scope
No global conclusion from local success
```

Avoid node labels such as:

```text
Any small action works
Double after success
More information is always better
UDAM proves optimal action
```

## Status

Stage 3 has started.

The current visual work adds the first one-page flow source.

Rendered figures can be added later under:

```text
assets/figures/
```

The English theory remains the source of truth.

Japanese visual synchronization should wait until the English visual structure stabilizes.
