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

Japanese explanations are maintained in the same repository. The current Japanese repository-status and simulation note is:

- [`docs/ja/README.md`](docs/ja/README.md)
- [`docs/ja/06_repository_status_and_simulations.md`](docs/ja/06_repository_status_and_simulations.md)

Future work should be small repository corrections only unless the maintainer explicitly asks for a new scope.

## Visual entry points

For a quick visual reading path, start with:

- [`docs/32_visual_explanation_layer.md`](docs/32_visual_explanation_layer.md)
- [`assets/figures/README.md`](assets/figures/README.md)
- [`assets/figures/one_page_udam_flow.svg`](assets/figures/one_page_udam_flow.svg)
- [`assets/figures/anchor_reanchor_timeline.svg`](assets/figures/anchor_reanchor_timeline.svg)
- [`assets/figures/observation_value_decision.svg`](assets/figures/observation_value_decision.svg)
- [`assets/figures/expansion_boundary_risk.svg`](assets/figures/expansion_boundary_risk.svg)
- [`assets/figures/literature_support_map.svg`](assets/figures/literature_support_map.svg)

Repository-facing simulation plots live under:

- [`simulations/plots/README.md`](simulations/plots/README.md)
- [`simulations/plots/repeated_checking_mov.svg`](simulations/plots/repeated_checking_mov.svg)
- [`simulations/plots/boundary_risk_sensitivity.svg`](simulations/plots/boundary_risk_sensitivity.svg)
- [`simulations/plots/observation_cost_threshold.svg`](simulations/plots/observation_cost_threshold.svg)

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

## Support and simulation status

Current support status:

```text
Levels 1-4: strong enough for a hobby theory project
Level 5: first-pass literature verification complete enough to support component-level claims
Level 6: six toy sanity checks recorded; not empirical validation
repository-facing plots: three SVG plots available
CI plot workflow: available under .github/workflows/simulation-plots.yml
```

For simulation details, see:

- [`simulations/README.md`](simulations/README.md)
- [`docs/39_simulation_sanity_checks.md`](docs/39_simulation_sanity_checks.md)
- [`docs/49_extended_simulation_sanity_checks.md`](docs/49_extended_simulation_sanity_checks.md)
- [`docs/55_repository_simulation_plots_and_sensitivity.md`](docs/55_repository_simulation_plots_and_sensitivity.md)

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
8. [`simulations/plots/README.md`](simulations/plots/README.md)

English-first practical reading order:

1. [`docs/14_practical_reanchor_protocol.md`](docs/14_practical_reanchor_protocol.md)
2. [`docs/15_application_cautions.md`](docs/15_application_cautions.md)
3. [`docs/16_adaptive_observation_cadence.md`](docs/16_adaptive_observation_cadence.md)
4. [`docs/18_adaptive_expansion_factor.md`](docs/18_adaptive_expansion_factor.md)
5. [`docs/21_failure_decision_tree.md`](docs/21_failure_decision_tree.md)
6. [`docs/00_overview.md`](docs/00_overview.md)
7. [`FAQ.md`](FAQ.md)
8. [`docs/01_timer_model.md`](docs/01_timer_model.md)
9. [`docs/13_deterministic_event_scope.md`](docs/13_deterministic_event_scope.md)
10. [`docs/11_timer_three_layer_model.md`](docs/11_timer_three_layer_model.md)
11. [`docs/02_uncertainty_diffusion.md`](docs/02_uncertainty_diffusion.md)
12. [`docs/12_state_vs_belief.md`](docs/12_state_vs_belief.md)
13. [`docs/03_reanchoring.md`](docs/03_reanchoring.md)
14. [`docs/04_action_value.md`](docs/04_action_value.md)
15. [`docs/05_propositions.md`](docs/05_propositions.md)
16. [`docs/06_failure_cases.md`](docs/06_failure_cases.md)
17. [`docs/07_applications.md`](docs/07_applications.md)
18. [`docs/08_related_work.md`](docs/08_related_work.md)
19. [`docs/17_literature_support_map.md`](docs/17_literature_support_map.md)
20. [`docs/09_open_questions.md`](docs/09_open_questions.md)
21. [`docs/10_formal_refinement.md`](docs/10_formal_refinement.md)
22. [`docs/33_project_note_consolidation.md`](docs/33_project_note_consolidation.md)
23. [`docs/47_remaining_work_register.md`](docs/47_remaining_work_register.md)
24. [`docs/48_stabilization_pass_summary.md`](docs/48_stabilization_pass_summary.md)
25. [`docs/53_repository_completion_check.md`](docs/53_repository_completion_check.md)
26. [`docs/54_final_repository_audit.md`](docs/54_final_repository_audit.md)
27. [`docs/55_repository_simulation_plots_and_sensitivity.md`](docs/55_repository_simulation_plots_and_sensitivity.md)
28. [`simulations/README.md`](simulations/README.md)

Japanese documentation:

- [`docs/ja/README.md`](docs/ja/README.md)
- [`docs/ja/06_repository_status_and_simulations.md`](docs/ja/06_repository_status_and_simulations.md)

## Repository map

| Path | Role |
|---|---|
| `docs/` | readable theory explanation |
| `docs/ja/` | Japanese explanations; English Markdown remains source of truth |
| `theory/` | definitions, variables, assumptions, axioms, propositions, proofs, counterexamples, logical review |
| `examples/` | structured applications and failure examples |
| `notes/` | origin notes, terminology, research notes, evidence hierarchy, verification notes |
| `assets/` | diagrams and figures |
| `simulations/` | toy sanity-check scripts, result files, and repository-facing plots; not empirical validation |
| `drafts/` | downstream paper, blog, manifesto, and project-note drafts; not source of truth |

## Development notes

- [`AGENTS.md`](AGENTS.md): repository editing guidance for future agents and automated assistants.
- [`docs/43_notation_consistency_audit.md`](docs/43_notation_consistency_audit.md): first-pass notation consistency audit.
- [`docs/44_contraction_rule_decision.md`](docs/44_contraction_rule_decision.md): decision note on contraction versus expansion rules.
- [`docs/45_publication_readiness_audit.md`](docs/45_publication_readiness_audit.md): first-pass publication-readiness audit.
- [`docs/46_readme_overview_compression_decision.md`](docs/46_readme_overview_compression_decision.md): decision note on README and overview compression.
- [`docs/47_remaining_work_register.md`](docs/47_remaining_work_register.md): remaining-work register after the stabilization pass.
- [`docs/48_stabilization_pass_summary.md`](docs/48_stabilization_pass_summary.md): summary of the latest stabilization pass.
- [`docs/49_extended_simulation_sanity_checks.md`](docs/49_extended_simulation_sanity_checks.md): extended toy simulation sanity-check summary.
- [`docs/50_visual_rendering_audit.md`](docs/50_visual_rendering_audit.md): older-diagram rendering audit.
- [`docs/51_release_history_routing_decision.md`](docs/51_release_history_routing_decision.md): release-history routing decision.
- [`docs/53_repository_completion_check.md`](docs/53_repository_completion_check.md): repository-completion consistency check.
- [`docs/54_final_repository_audit.md`](docs/54_final_repository_audit.md): final repository audit.
- [`docs/55_repository_simulation_plots_and_sensitivity.md`](docs/55_repository_simulation_plots_and_sensitivity.md): repository-facing simulation plots and sensitivity summary.
- [`simulations/README.md`](simulations/README.md): reproducible toy simulation scripts, result files, plots, and CI workflow.
- [`drafts/README.md`](drafts/README.md): downstream draft index and source-of-truth disclaimer.
- [`notes/literature_verification.md`](notes/literature_verification.md): checklist for verifying related-work claims before treating them as citations.
- [`notes/evidence_hierarchy.md`](notes/evidence_hierarchy.md): support levels for UDAM claims.
- [`theory/logical_synthesis_review.md`](theory/logical_synthesis_review.md): logical coherence review across model layers.
- [`theory/consistency_review.md`](theory/consistency_review.md): known corrections and open consistency issues.
- [`notes/high_stakes_example_policy.md`](notes/high_stakes_example_policy.md): policy for preserving high-stakes examples as safe abstract structures.

## Repository status

This repository is currently a completed GitHub theory repository. The current goal is small correction only, not implementation, paperization, or empirical validation.

Current status:

```text
core theory: stable enough to refine
failure boundaries: strong
literature verification: first-pass complete
visual explanation: Stage 3 SVG figures available; older rendering audited and deferred
simulation sanity checks: six toy checks recorded; not empirical validation
repository-facing plots: three SVG plots available
CI plot workflow: added
project-note consolidation: first-pass complete
Japanese layer: repository-facing sync complete; English Markdown remains source of truth
repository completion check: complete
final repository audit: pass
```

## License

Documentation and theory texts are licensed under **CC BY 4.0**.
