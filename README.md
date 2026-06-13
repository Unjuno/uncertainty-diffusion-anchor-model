# Uncertainty-Diffusion Anchor Model

**Uncertainty-Diffusion Anchor Model**, or **UDAM**, is a timer-derived practical synthesis describing how uncertainty expands when an anchor is lost, and how small informative actions can re-anchor an agent's belief state.

日本語名：**不確実性拡散アンカーモデル**

UDAM is not proposed as a replacement for existing decision theory. Its value is in organizing existing ideas around a simple timer-derived structure:

```text
τ = K + U + R
```

## One-sentence summary

When uncertainty diffuses over time, low-cost informative actions can be rational because they re-anchor the agent's belief state.

不確実性は放置すると拡散する。だから、情報を返す小さな行動を細かく打ち、現在地を再アンカーし続ける戦略は合理的になりうる。

## Japanese documentation

Japanese explanations are maintained in the same repository, not in a separate repository.

Start here:

- [`docs/ja/README.md`](docs/ja/README.md)
- [`docs/ja/00_plain_explanation.md`](docs/ja/00_plain_explanation.md)

## Core intuition

The model begins with a timer example.

A person is counting toward a fixed upper time bound. They count accurately for a while, lose track during an interruption, and then start counting again.

The lost interval remains uncertain. However, the newly counted interval is not meaningless. It becomes a new anchor.

This simple structure generalizes to learning, work recovery, health tracking, relationship uncertainty, and life strategy after failure.

The distinctive framing is not:

```text
small action is always good
```

but:

```text
lost anchor does not imply future anchor invalidation
```

## If you want to use it now

For direct use, start with:

- [`docs/14_practical_reanchor_protocol.md`](docs/14_practical_reanchor_protocol.md)
- [`docs/15_application_cautions.md`](docs/15_application_cautions.md)
- [`docs/16_adaptive_observation_cadence.md`](docs/16_adaptive_observation_cadence.md)
- [`docs/18_adaptive_expansion_factor.md`](docs/18_adaptive_expansion_factor.md)
- [`examples/concrete_learning_reanchor.md`](examples/concrete_learning_reanchor.md)
- [`examples/concrete_work_reanchor.md`](examples/concrete_work_reanchor.md)
- [`examples/concrete_relationship_reanchor.md`](examples/concrete_relationship_reanchor.md)
- [`examples/concrete_budget_reanchor.md`](examples/concrete_budget_reanchor.md)

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

or:

```text
OV > 0
```

## Minimal timer model

```text
τ = K + U + R
```

where:

- `K`: known counted interval before losing the anchor
- `U`: unknown interval while the anchor was lost
- `R`: re-anchored counted interval after restarting
- `τ`: current elapsed time

The central point is:

> Losing the anchor does not invalidate all future measurements. It only creates uncertainty in the lost interval.

Timer re-anchoring should be read in three layers:

1. absolute uncertainty in `U` may remain or increase;
2. relative uncertainty can be diluted if the reference scale grows faster than the uncertainty scale;
3. a fixed upper time bound can constrain the possible range of `U`.

## Deterministic event scope

The timer seed model assumes a fixed target condition.

It asks:

```text
Given a fixed target, where is the agent relative to it?
```

It does not ask:

```text
What is the probability that the target event itself occurs?
```

This is a local modeling constraint. UDAM does not need to claim that all reality is deterministic; it only keeps event-occurrence uncertainty out of the core timer model.

## Controllability boundary

UDAM is an action-oriented model.

The core theory includes uncertainty that action can affect through at least one of:

- observation;
- belief update;
- decision improvement;
- state intervention.

Uncontrollable event-occurrence uncertainty is excluded from the core model, or treated as an external parameter, separate extension, or exception condition.

## Observability value

UDAM now treats informational value as more than uncertainty reduction.

A re-anchoring action can increase observability and enable better conditional action.

```text
OV = E_y[max_a E[V(a, S) | y]] - max_a E[V(a, S)] - C(obs)
```

Observation is favorable when:

```text
OV > 0
```

This explains both directions:

```text
hidden upside can be revealed
hidden downside can be revealed early
```

It also explains fixed-target disbelief. If the agent discounts a fixed target with subjective weight `pi_hat`, a favorable re-anchor can appear unfavorable:

```text
pi_hat * I_position(a) + B(a) <= C(a) < I_position(a) + B(a)
```

## High-stakes example policy

High-stakes examples can be useful because they make the fixed-target and lost-anchor structure clear.

However, the repository treats them as abstract illustrations only. Public wording should remain non-operational and neutral, using terms such as:

- fixed target condition;
- upper time bound;
- high-stakes deadline;
- safety-critical setting;
- constrained decision context.

The useful structure is preserved without vivid or harmful detail.

## FAQ

For common misunderstandings, see [`FAQ.md`](FAQ.md).

The FAQ covers:

- whether UDAM says action is always better than inaction;
- why the timer seed model uses a fixed target;
- why uncontrollable event-occurrence uncertainty is excluded;
- how high-stakes examples should be interpreted;
- why re-anchoring does not always reduce absolute uncertainty;
- how observability explains happy miscalculation, false comfort, and fixed-target disbelief;
- why doubling is a possible default, not a universal optimum.

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

where:

- `P_t`: uncertainty at time `t`
- `Q`: uncertainty diffusion rate
- `a`: action
- `I(a)`: informational value
- `B(a)`: intervention value
- `C(a)`: action cost
- `OV`: value of making the state observable enough to support better conditional action
- `s_i`: current observation or action scope
- `r_i`: expansion factor
- `V(a)`: total action value

A small action is favorable when:

```text
V(a) > 0
```

or, for observation-specific actions:

```text
OV > 0
```

A larger expansion is favorable only when its gain exceeds observation, correction, and boundary-crossing costs.

## State versus belief

UDAM is primarily about belief uncertainty.

It does not claim that the world always worsens during inaction. It claims that, without anchors, the agent's uncertainty about the current state may increase.

A later formal version can separate:

```text
state dynamics: S_t changes
belief dynamics: P_t changes
```

## Main claim

If uncertainty diffuses in the absence of anchors, then low-cost informative actions can be advantageous because they reduce or constrain uncertainty growth, reveal hidden upside, reveal hidden downside early, or enable better conditional action.

This does **not** justify arbitrary action. It supports actions that return information, improve the state, or both, at sufficiently low cost.

## Novelty position

UDAM should not be read as a wholly new mathematical theory of uncertainty.

A safer position is:

> UDAM is a timer-derived practical synthesis of belief uncertainty, re-anchoring, observability value, conditional action, and boundary-risk-constrained expansion after anchor loss.

Its distinctive contribution is the organizing metaphor and decomposition:

```text
partial uncertainty does not imply total invalidation
τ = K + U + R
```

For the detailed positioning note, see:

- [`docs/19_positioning_and_novelty.md`](docs/19_positioning_and_novelty.md)

## Repository map

| Path | Role |
|---|---|
| `docs/` | readable theory explanation |
| `docs/ja/` | Japanese explanations |
| `theory/` | definitions, assumptions, axioms, propositions, proofs, counterexamples, consistency review |
| `examples/` | structured applications |
| `notes/` | origin notes, terminology, research notes, chat synthesis |
| `assets/` | diagrams and figures |
| `drafts/` | paper, blog, and manifesto drafts |

## Reading order

1. [`docs/ja/README.md`](docs/ja/README.md)
2. [`docs/14_practical_reanchor_protocol.md`](docs/14_practical_reanchor_protocol.md)
3. [`docs/15_application_cautions.md`](docs/15_application_cautions.md)
4. [`docs/16_adaptive_observation_cadence.md`](docs/16_adaptive_observation_cadence.md)
5. [`docs/18_adaptive_expansion_factor.md`](docs/18_adaptive_expansion_factor.md)
6. [`docs/19_positioning_and_novelty.md`](docs/19_positioning_and_novelty.md)
7. [`docs/00_overview.md`](docs/00_overview.md)
8. [`FAQ.md`](FAQ.md)
9. [`docs/01_timer_model.md`](docs/01_timer_model.md)
10. [`docs/13_deterministic_event_scope.md`](docs/13_deterministic_event_scope.md)
11. [`docs/11_timer_three_layer_model.md`](docs/11_timer_three_layer_model.md)
12. [`docs/02_uncertainty_diffusion.md`](docs/02_uncertainty_diffusion.md)
13. [`docs/12_state_vs_belief.md`](docs/12_state_vs_belief.md)
14. [`docs/03_reanchoring.md`](docs/03_reanchoring.md)
15. [`docs/04_action_value.md`](docs/04_action_value.md)
16. [`docs/05_propositions.md`](docs/05_propositions.md)
17. [`docs/06_failure_cases.md`](docs/06_failure_cases.md)
18. [`docs/07_applications.md`](docs/07_applications.md)
19. [`docs/08_related_work.md`](docs/08_related_work.md)
20. [`docs/17_literature_support_map.md`](docs/17_literature_support_map.md)
21. [`docs/09_open_questions.md`](docs/09_open_questions.md)
22. [`docs/10_formal_refinement.md`](docs/10_formal_refinement.md)

## Development notes

- [`notes/chat_content_synthesis.md`](notes/chat_content_synthesis.md): organized synthesis of the original discussion.
- [`notes/high_stakes_example_policy.md`](notes/high_stakes_example_policy.md): policy for preserving high-stakes examples as safe abstract structures.
- [`notes/literature_verification.md`](notes/literature_verification.md): checklist for verifying related-work claims before treating them as citations.
- [`theory/consistency_review.md`](theory/consistency_review.md): known corrections, open issues, and consistency checks.
- [`theory/timer_three_layer_model.md`](theory/timer_three_layer_model.md): formal timer-specific refinement.
- [`theory/deterministic_event_scope.md`](theory/deterministic_event_scope.md): fixed-target scope of the timer seed model.
- [`theory/controllability_boundary.md`](theory/controllability_boundary.md): boundary between actionable uncertainty and uncontrollable external uncertainty.
- [`theory/observability_value.md`](theory/observability_value.md): formal value of observation and conditional action.
- [`theory/observability_proofs.md`](theory/observability_proofs.md): proof sketches for observability value and fixed-target discounting.
- [`theory/upside_uncertainty.md`](theory/upside_uncertainty.md): hidden upside and happy miscalculation.
- [`theory/downside_uncertainty.md`](theory/downside_uncertainty.md): hidden downside, false comfort, and fixed-target disbelief.
- [`theory/state_belief_separation.md`](theory/state_belief_separation.md): formal distinction between state dynamics and belief dynamics.

## Applications

- time perception
- learning recovery
- work interruption recovery
- health tracking
- relationship uncertainty
- life strategy after failure
- cognitive re-orientation after disruption
- happy miscalculation
- false comfort miscalculation
- fixed-target disbelief
- practical re-anchor protocol
- adaptive observation cadence
- adaptive expansion factor
- Japanese explanation layer
- literature support map

## Failure cases

UDAM does not apply cleanly when:

- the action returns no information;
- the action cost exceeds its informational and intervention value;
- feedback is systematically misleading;
- repeated checking becomes compulsive and uninformative;
- the state does not diffuse without an anchor;
- event-occurrence uncertainty is mixed into the timer seed model without adding a separate layer;
- uncontrollable external uncertainty is treated as if it were actionable;
- safety-critical action is delayed by unnecessary measurement.

## Repository status

This repository is currently a theory repository. The first goal is not simulation or implementation, but precise formulation:

1. timer model
2. variable definitions
3. assumptions and axioms
4. propositions and proofs
5. counterexamples
6. applications
7. related work
8. consistency review
9. formal refinement
10. observability value
11. practical re-anchor protocol
12. adaptive observation cadence
13. adaptive expansion factor
14. literature support map
15. positioning and novelty statement
16. Japanese explanation layer
17. literature verification checklist
18. additional diagrams

## License

Documentation and theory texts are licensed under **CC BY 4.0**.

Code, if added later, should be licensed separately, preferably under the MIT License unless otherwise stated.
