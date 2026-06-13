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

## Second visual artifact

The second Stage 3 diagram is:

```text
assets/diagrams/anchor_reanchor_timeline.mmd
```

It is intended to make the timer seed model visible:

```text
tau = K + U + R
```

The diagram separates:

```text
K: known interval before anchor loss
U: unknown interval after anchor loss
R: re-anchored interval after valid new observation
```

Its main visual claim is:

```text
U being unknown does not automatically invalidate R.
```

The diagram should preserve three warnings:

```text
do not erase K
do not pretend U is known
do not invalidate R merely because U is unknown
```

This diagram supports the core UDAM proposition:

```text
partial uncertainty does not imply total invalidation
```

and the practical re-anchor rule:

```text
future anchor validity must be checked locally, not globally rejected because of past anchor loss
```

## Third visual artifact

The third Stage 3 diagram is:

```text
assets/diagrams/observation_value_decision.mmd
```

It is intended to show why a valid observation is not automatically a favorable observation.

It separates four checks:

```text
1. Is result y observable?
2. Is y state-informative?
3. Does y change feasible action?
4. Is OV > 0 after observation cost?
```

The diagram centers the distinction:

```text
state-informative != favorable
```

and the conditional-action requirement:

```text
a(y) != a_0
```

The diagram also shows the observation-value expression:

```text
OV = E_y[max_a E[V(a,S) | y]] - max_a E[V(a,S)] - C(obs)
```

Its main visual claim is:

```text
an observation is useful only when it can improve action enough to justify its cost
```

## Diagram inventory for Stage 3

Planned Stage 3 visual set:

| Diagram | Purpose | Status |
|---|---|---:|
| `one_page_udam_flow.mmd` | compact full flow from anchor loss to risk-constrained expansion | added |
| `anchor_reanchor_timeline.mmd` | show `K + U + R` and why unknown `U` does not erase valid `R` | added |
| `observation_value_decision.mmd` | show `state-informative != favorable`, `a(y) != a_0`, and `OV > 0` | added |
| expansion-with-boundary-risk diagram | show why expansion is not automatic doubling | planned |
| literature-support map figure | show which components are directly supported, partial, analogy-only, unsupported | planned |

## Intended reader path

Recommended reader order after Stage 3 begins:

```text
README
-> one-page UDAM flow diagram
-> anchor-reanchor timeline
-> observation-value decision diagram
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

## Timeline diagram text

The timeline diagram should keep the timer seed model visually simple.

Preferred node labels:

```text
Known interval K
Anchor lost
Unknown interval U
Re-anchored interval R
Current position tau
tau = K + U + R
Do not invalidate R because U is unknown
```

Avoid node labels such as:

```text
U means everything is invalid
R fixes all uncertainty
Past anchor loss proves future observations are useless
```

## Observation-value diagram text

The observation-value diagram should keep the decision sequence explicit.

Preferred node labels:

```text
Candidate observation y
Observable result?
State-informative?
Does feasible action change?
a(y) != a_0?
OV > 0?
Favorable observation
State-informative but not favorable
```

Avoid node labels such as:

```text
Informative means useful
Any observation helps
Curiosity is enough
Observation guarantees action improvement
```

## Status

Stage 3 has started.

The current visual work adds:

```text
assets/diagrams/one_page_udam_flow.mmd
assets/diagrams/anchor_reanchor_timeline.mmd
assets/diagrams/observation_value_decision.mmd
```

Rendered figures can be added later under:

```text
assets/figures/
```

The English theory remains the source of truth.

Japanese visual synchronization should wait until the English visual structure stabilizes.
