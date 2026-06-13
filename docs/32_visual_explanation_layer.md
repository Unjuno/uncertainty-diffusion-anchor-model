# 32 Visual Explanation Layer

This document tracks Stage 3 of the five-stage refinement roadmap.

Stage 3 does not add new theory.

Its purpose is to make the existing theory readable at a glance.

## Stage 3 goal

The visual layer explains the core UDAM flow:

```text
anchor loss -> uncertainty diffusion -> valid local observation -> conditional action -> repeated observation boundary -> risk-constrained expansion
```

The visual layer should reduce cognitive load without hiding assumptions.

It should preserve these corrections:

```text
state-informative != favorable
small != useful
feedback-producing != favorable
local success != global expansion permission
robust != optimal
execution support != value support
epistemic value != automatic favorability
successive approximation != boundary-risk permission
component support != full synthesis proof
```

## Source and rendered figure policy

Editable source diagrams are stored in:

```text
assets/diagrams/
```

Reader-facing static SVG figures are stored in:

```text
assets/figures/
```

Do not treat SVG files as the primary source.

Preferred workflow:

```text
edit Mermaid source -> regenerate or update SVG figure -> update figure index if needed
```

## Stage 3 visual set

| Visual artifact | Mermaid source | Rendered SVG | Purpose | Status |
|---|---|---|---|---:|
| One-page UDAM flow | `assets/diagrams/one_page_udam_flow.mmd` | `assets/figures/one_page_udam_flow.svg` | compact flow from anchor loss to risk-constrained expansion | rendered |
| Anchor-reanchor timeline | `assets/diagrams/anchor_reanchor_timeline.mmd` | `assets/figures/anchor_reanchor_timeline.svg` | show `tau = K + U + R` and why unknown `U` does not erase valid `R` | rendered |
| Observation-value decision | `assets/diagrams/observation_value_decision.mmd` | `assets/figures/observation_value_decision.svg` | show `state-informative != favorable`, `a(y) != a_0`, and `OV > 0` | rendered |
| Expansion boundary risk | `assets/diagrams/expansion_boundary_risk.mmd` | `assets/figures/expansion_boundary_risk.svg` | show why expansion is not automatic doubling and must pass boundary-risk checks | rendered |
| Literature support map | `assets/diagrams/literature_support_map.mmd` | `assets/figures/literature_support_map.svg` | show direct, partial, analogy-only, avoid, and UDAM-specific support categories | rendered |

## Intended reader path

Recommended reader order:

```text
README
-> visual explanation layer
-> rendered figure index
-> one-page UDAM flow
-> anchor-reanchor timeline
-> observation-value decision
-> expansion-with-boundary-risk diagram
-> literature-support map
-> failure decision tree
-> logical synthesis review
-> detailed formal notes
```

## Visual artifact summaries

### 1. One-page UDAM flow

Main purpose:

```text
show the whole practical UDAM sequence on one page
```

Key warning:

```text
local success does not imply global safety
```

### 2. Anchor-reanchor timeline

Main purpose:

```text
show tau = K + U + R
```

Key warning:

```text
U being unknown does not automatically invalidate R
```

### 3. Observation-value decision

Main purpose:

```text
show why a valid observation is not automatically favorable
```

Key checks:

```text
observable result
state-informative result
action change
OV > 0 after observation cost
```

### 4. Expansion boundary risk

Main purpose:

```text
show why a favorable local result does not automatically permit expansion
```

Key inequality:

```text
B_expand(r_i) + I_expand(r_i) > C_obs(r_i) + P_boundary(i) C_boundary + C_correct(r_i)
```

Key warning:

```text
r_i is selected, not automatically 2
```

### 5. Literature support map

Main purpose:

```text
show support strength, not prestige
```

Support categories:

```text
direct support
partial support
analogy only
not supported / avoid
UDAM-specific synthesis
```

Key warning:

```text
component support does not prove full synthesis
```

## Avoided visual claims

Do not make diagrams imply:

```text
Any small action works
More information is always better
Double after success
Local success proves global safety
UDAM is proven by one literature
UDAM is therapy
UDAM is active inference
Literature proves the whole model
```

## Status

Stage 3 is first-pass complete as a visual explanation layer.

The five planned Mermaid sources and their first-pass SVG figures are now present.

Future visual work may include:

```text
render older non-Stage-3 diagrams
add PNG exports for platforms that do not display SVG well
improve visual styling after content stabilizes
```

The English theory remains the source of truth.

Japanese visual synchronization should wait until the English visual structure stabilizes.
