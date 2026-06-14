# 50 Visual Rendering Audit

This document records a first-pass audit of older Mermaid diagrams and whether they need rendered static figures.

The purpose is not to add new theory.

The purpose is to prevent unnecessary visual churn while keeping reader-facing diagrams discoverable.

## Current decision

Status:

```text
older diagram rendering audit: first-pass complete
additional rendering: deferred / optional
```

Decision:

```text
Do not render every older Mermaid diagram now.
The Stage 3 SVG set already covers the current reader-facing visual path.
Render older diagrams only if they remain directly reader-facing or are needed for publication/export.
```

Reason:

```text
Visual artifacts summarize theory; they do not authorize theory.
Rendering every historical diagram may create maintenance burden and visual drift without improving the source-of-truth layer.
```

## Current rendered figure set

Rendered Stage 3 figures already exist under:

```text
assets/figures/
```

Current Stage 3 SVG set:

```text
one_page_udam_flow.svg
anchor_reanchor_timeline.svg
observation_value_decision.svg
expansion_boundary_risk.svg
literature_support_map.svg
```

These are sufficient for the main visual reading path.

## Older Mermaid source audit

| Mermaid source | Current role | Render now? | Reason |
|---|---|---:|---|
| `timer_decomposition.mmd` | early timer decomposition | no | covered by `anchor_reanchor_timeline.svg` for the reader-facing path |
| `timer_relative_dilution.mmd` | timer relative influence concept | optional | useful only if paper or tutorial needs a separate relative-dilution figure |
| `uncertainty_diffusion_cycle.mmd` | early cycle diagram | no | covered conceptually by `one_page_udam_flow.svg` |
| `action_value_flow.mmd` | action-value explanation | optional | could be rendered for a paper appendix, but not required for current public path |
| `failure_taxonomy.mmd` | early failure taxonomy | no | reader-facing failure routing now uses `failure_decision_tree.mmd` and `docs/21` |
| `failure_decision_tree.mmd` | failure diagnostic tree | optional-high | useful candidate if a static figure is needed for publication or README-free viewing |
| `observability_value_flow.mmd` | older observability diagram | no | covered by `observation_value_decision.svg` |
| `adaptive_expansion_factor.mmd` | older expansion-factor diagram | no | covered by `expansion_boundary_risk.svg` |
| `full_udam_flow.mmd` | broad flow diagram used by Japanese docs | optional | useful if Japanese visual sync becomes active |
| `positioning_map.mmd` | positioning / novelty map | optional | useful if public positioning explanation needs a static figure |

## Render candidates

If rendering is resumed, prioritize:

```text
1. failure_decision_tree.mmd
2. timer_relative_dilution.mmd
3. positioning_map.mmd
4. full_udam_flow.mmd
```

Do not prioritize:

```text
uncertainty_diffusion_cycle.mmd
action_value_flow.mmd
failure_taxonomy.mmd
observability_value_flow.mmd
adaptive_expansion_factor.mmd
```

unless a specific downstream document requires them.

## Rendering policy

Preferred workflow:

```text
1. edit Mermaid source in assets/diagrams/
2. render static output into assets/figures/
3. update assets/figures/README.md
4. update docs/32 or the relevant visual routing note only if the rendered figure becomes reader-facing
```

Avoid:

```text
editing SVG as the source of truth
letting rendered diagrams introduce new claims
adding rendered figures without maintaining Mermaid source
using figure existence as evidence of theory validity
```

## Result

Current result:

```text
No older diagram must be rendered before public repository release.
```

Recommended future action:

```text
Render only failure_decision_tree.mmd if a static failure-boundary figure becomes necessary.
Otherwise leave older diagrams as editable Mermaid sources.
```
