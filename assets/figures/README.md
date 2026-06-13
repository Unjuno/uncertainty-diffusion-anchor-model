# Figures

This directory contains rendered or static reader-facing figures derived from the Mermaid diagrams in `assets/diagrams/`.

Mermaid source files remain the primary editable source.

Rendered figures are secondary outputs for easier reading, embedding, and presentation.

## Stage 3 visual figures

| Figure | Source diagram | Purpose |
|---|---|---|
| `one_page_udam_flow.svg` | `../diagrams/one_page_udam_flow.mmd` | compact full flow from anchor loss to risk-constrained expansion |
| `anchor_reanchor_timeline.svg` | `../diagrams/anchor_reanchor_timeline.mmd` | timer seed timeline showing `K + U + R` |
| `observation_value_decision.svg` | `../diagrams/observation_value_decision.mmd` | distinction between state-informative and favorable observation |
| `expansion_boundary_risk.svg` | `../diagrams/expansion_boundary_risk.mmd` | expansion factor selection under boundary-risk constraints |
| `literature_support_map.svg` | `../diagrams/literature_support_map.mmd` | direct, partial, analogy-only, avoid, and UDAM-specific support categories |

## Source policy

Do not edit rendered figures as the primary source.

Preferred workflow:

```text
edit Mermaid source in assets/diagrams/
then regenerate or manually update rendered figure in assets/figures/
```

## Current status

The Stage 3 figure set is available as SVG first-pass static figures.

Future work may add PNG exports if needed for platforms that do not display SVG well.
