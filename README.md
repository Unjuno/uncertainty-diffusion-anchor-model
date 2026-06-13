# Uncertainty-Diffusion Anchor Model

**Uncertainty-Diffusion Anchor Model**, or **UDAM**, is a timer-derived practical synthesis describing how uncertainty expands when an anchor is lost, and how small informative actions can re-anchor an agent's belief state.

日本語名：**不確実性拡散アンカーモデル**

UDAM is not proposed as a replacement for existing decision theory. Its value is in organizing existing ideas around a simple timer-derived structure:

```text
τ = K + U + R
```

## One-sentence summary

When uncertainty diffuses over time, low-cost informative actions can be rational because they re-anchor the agent's belief state.

The distinctive framing is not:

```text
small action is always good
```

but:

```text
lost anchor does not imply future anchor invalidation
```

## Current development policy

The English theory is the source of truth for now.

Japanese explanations are maintained in the same repository, but further Japanese expansion is deferred until the English structure stabilizes.

Current Japanese entry point:

- [`docs/ja/README.md`](docs/ja/README.md)

## Visual entry points

For a quick visual reading path, start with:

- [`docs/32_visual_explanation_layer.md`](docs/32_visual_explanation_layer.md)
- [`assets/figures/README.md`](assets/figures/README.md)
- [`assets/figures/one_page_udam_flow.svg`](assets/figures/one_page_udam_flow.svg)
- [`assets/figures/anchor_reanchor_timeline.svg`](assets/figures/anchor_reanchor_timeline.svg)
- [`assets/figures/observation_value_decision.svg`](assets/figures/observation_value_decision.svg)
- [`assets/figures/expansion_boundary_risk.svg`](assets/figures/expansion_boundary_risk.svg)
- [`assets/figures/literature_support_map.svg`](assets/figures/literature_support_map.svg)

Editable Mermaid sources are kept under:

- [`assets/diagrams/one_page_udam_flow.mmd`](assets/diagrams/one_page_udam_flow.mmd)
- [`assets/diagrams/anchor_reanchor_timeline.mmd`](assets/diagrams/anchor_reanchor_timeline.mmd)
- [`assets/diagrams/observation_value_decision.mmd`](assets/diagrams/observation_value_decision.mmd)
- [`assets/diagrams/expansion_boundary_risk.mmd`](assets/diagrams/expansion_boundary_risk.mmd)
- [`assets/diagrams/literature_support_map.mmd`](assets/diagrams/literature_support_map.mmd)

The visual sequence is:

```text
anchor loss
-> K + U + R
-> valid observation
-> favorable observation
-> boundary-risk-constrained expansion
-> literature support strength
```

The visual layer is meant to improve comprehension, not to introduce new theory.

## Core model

The model begins with a timer example.

A person is counting toward a fixed upper time bound. They count accurately for a while, lose track during an interruption, and then start counting again.

The lost interval remains uncertain. However, the newly counted interval is not meaningless. It becomes a new anchor.

Minimal timer decomposition:

```text
τ = K + U + R
```

where:

- `K`: known counted interval before losing the anchor;
- `U`: unknown interval while the anchor was lost;
- `R`: re-anchored counted interval after restarting;
- `τ`: current elapsed time.

The central claim is:

```text
partial uncertainty does not imply total invalidation
```

## General model

Uncertainty diffusion without an anchor:

```text
P_{t+Δt} = P_t + QΔt
```

Action value:

```text
V(a) = I(a) + B(a) - C(a)
```

Observability value:

```text
OV = E_y[max_a E[V(a, S) | y]] - max_a E[V(a, S)] - C(obs)
```

Adaptive expansion factor:

```text
s_{i+1} = r_i s_i
```

Boundary-risk-constrained expansion:

```text
B_expand(r_i) + I_expand(r_i) > C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
```

## If you want to use it now

For direct use, start with:

- [`docs/14_practical_reanchor_protocol.md`](docs/14_practical_reanchor_protocol.md)
- [`docs/15_application_cautions.md`](docs/15_application_cautions.md)
- [`docs/16_adaptive_observation_cadence.md`](docs/16_adaptive_observation_cadence.md)
- [`docs/18_adaptive_expansion_factor.md`](docs/18_adaptive_expansion_factor.md)
- [`docs/21_failure_decision_tree.md`](docs/21_failure_decision_tree.md)

The practical pattern is:

```text
unclear state -> state-informative observation -> conditional next action
```

Ask:

```text
What small observation would reveal the current state?
```

Then act only if:

```text
V(a) > 0
```

or, for observation-specific actions:

```text
OV > 0
```

## Failure diagnostic

UDAM does not support activity, checking, observation, or expansion as such.

Use the failure decision tree:

- [`docs/21_failure_decision_tree.md`](docs/21_failure_decision_tree.md)

Core failure conditions include:

```text
P(y | S) = P(y)
a(y) = a_0
MOV_i <= 0
B_expand(r_i) + I_expand(r_i) <= C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
one local result -> total judgment
```

## Five-stage refinement roadmap

After the core theory stabilized, development moved to a five-stage refinement process:

```text
1. failure boundaries
2. literature verification
3. visual explanation
4. project-note consolidation
5. Japanese explanation sync
```

See:

- [`docs/20_five_stage_development_roadmap.md`](docs/20_five_stage_development_roadmap.md)
- [`notes/evidence_hierarchy.md`](notes/evidence_hierarchy.md)

Current support status:

```text
Levels 1-4: strong enough for a hobby theory project
Level 5: first-pass literature verification complete enough to support component-level claims
Level 6: empirical testing or simulation deferred
```

## Logical synthesis status

A cross-layer logical review found no major internal contradiction.

See:

- [`theory/logical_synthesis_review.md`](theory/logical_synthesis_review.md)

Main watch items:

```text
I(a) versus OV
state-informative versus favorable
first observation versus repeated observation
expansion versus automatic doubling
local observation versus global conclusion
```

## Novelty position

UDAM should not be read as a wholly new mathematical theory of uncertainty.

A safer position is:

> UDAM is a timer-derived practical synthesis of belief uncertainty, re-anchoring, observability value, conditional action, and boundary-risk-constrained expansion after anchor loss.

For details, see:

- [`docs/19_positioning_and_novelty.md`](docs/19_positioning_and_novelty.md)

## Reading order

Visual-first reading order:

1. [`docs/32_visual_explanation_layer.md`](docs/32_visual_explanation_layer.md)
2. [`assets/figures/README.md`](assets/figures/README.md)
3. [`assets/figures/one_page_udam_flow.svg`](assets/figures/one_page_udam_flow.svg)
4. [`assets/figures/anchor_reanchor_timeline.svg`](assets/figures/anchor_reanchor_timeline.svg)
5. [`assets/figures/observation_value_decision.svg`](assets/figures/observation_value_decision.svg)
6. [`assets/figures/expansion_boundary_risk.svg`](assets/figures/expansion_boundary_risk.svg)
7. [`assets/figures/literature_support_map.svg`](assets/figures/literature_support_map.svg)

English-first practical reading order:

1. [`docs/14_practical_reanchor_protocol.md`](docs/14_practical_reanchor_protocol.md)
2. [`docs/15_application_cautions.md`](docs/15_application_cautions.md)
3. [`docs/16_adaptive_observation_cadence.md`](docs/16_adaptive_observation_cadence.md)
4. [`docs/18_adaptive_expansion_factor.md`](docs/18_adaptive_expansion_factor.md)
5. [`docs/21_failure_decision_tree.md`](docs/21_failure_decision_tree.md)
6. [`docs/20_five_stage_development_roadmap.md`](docs/20_five_stage_development_roadmap.md)
7. [`docs/32_visual_explanation_layer.md`](docs/32_visual_explanation_layer.md)
8. [`docs/19_positioning_and_novelty.md`](docs/19_positioning_and_novelty.md)
9. [`docs/00_overview.md`](docs/00_overview.md)
10. [`FAQ.md`](FAQ.md)
11. [`docs/01_timer_model.md`](docs/01_timer_model.md)
12. [`docs/13_deterministic_event_scope.md`](docs/13_deterministic_event_scope.md)
13. [`docs/11_timer_three_layer_model.md`](docs/11_timer_three_layer_model.md)
14. [`docs/02_uncertainty_diffusion.md`](docs/02_uncertainty_diffusion.md)
15. [`docs/12_state_vs_belief.md`](docs/12_state_vs_belief.md)
16. [`docs/03_reanchoring.md`](docs/03_reanchoring.md)
17. [`docs/04_action_value.md`](docs/04_action_value.md)
18. [`docs/05_propositions.md`](docs/05_propositions.md)
19. [`docs/06_failure_cases.md`](docs/06_failure_cases.md)
20. [`docs/07_applications.md`](docs/07_applications.md)
21. [`docs/08_related_work.md`](docs/08_related_work.md)
22. [`docs/17_literature_support_map.md`](docs/17_literature_support_map.md)
23. [`docs/09_open_questions.md`](docs/09_open_questions.md)
24. [`docs/10_formal_refinement.md`](docs/10_formal_refinement.md)
25. [`docs/33_project_note_consolidation.md`](docs/33_project_note_consolidation.md)
26. [`docs/34_readme_consolidation_audit.md`](docs/34_readme_consolidation_audit.md)

Japanese documentation, to be synchronized after English stabilization:

- [`docs/ja/README.md`](docs/ja/README.md)

## Repository map

| Path | Role |
|---|---|
| `docs/` | readable theory explanation |
| `docs/ja/` | Japanese explanations; currently a later synchronization layer |
| `theory/` | definitions, variables, assumptions, axioms, propositions, proofs, counterexamples, logical review |
| `examples/` | structured applications and failure examples |
| `notes/` | origin notes, terminology, research notes, evidence hierarchy, verification notes |
| `assets/` | diagrams and figures |
| `drafts/` | optional paper, blog, manifesto, and project-note drafts |

For source-of-truth assignments and consolidation rules, see:

- [`docs/33_project_note_consolidation.md`](docs/33_project_note_consolidation.md)

For the README-specific consolidation audit, see:

- [`docs/34_readme_consolidation_audit.md`](docs/34_readme_consolidation_audit.md)

## Development notes

- [`docs/33_project_note_consolidation.md`](docs/33_project_note_consolidation.md): source-of-truth map for repository consolidation.
- [`docs/34_readme_consolidation_audit.md`](docs/34_readme_consolidation_audit.md): first-pass audit of README duplication and routing risk.
- [`notes/literature_verification.md`](notes/literature_verification.md): checklist for verifying related-work claims before treating them as citations.
- [`notes/evidence_hierarchy.md`](notes/evidence_hierarchy.md): support levels for UDAM claims.
- [`theory/logical_synthesis_review.md`](theory/logical_synthesis_review.md): logical coherence review across model layers.
- [`theory/consistency_review.md`](theory/consistency_review.md): known corrections and open consistency issues.
- [`notes/high_stakes_example_policy.md`](notes/high_stakes_example_policy.md): policy for preserving high-stakes examples as safe abstract structures.

## Repository status

This repository is currently a theory repository. The first goal is not simulation or implementation, but precise formulation and readable refinement.

Current status:

```text
core theory: stable enough to refine
failure boundaries: strong
literature verification: first-pass complete
visual explanation: first-pass Mermaid source set complete; Stage 3 SVG figures available
project-note consolidation: README audit complete as first pass
Japanese layer: minimal, deferred for later sync
```

## License

Documentation and theory texts are licensed under **CC BY 4.0**.

Code, if added later, should be licensed separately, preferably under the MIT License unless otherwise stated.
