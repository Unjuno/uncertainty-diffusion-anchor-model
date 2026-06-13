# Uncertainty-Diffusion Anchor Model

**Uncertainty-Diffusion Anchor Model**, or **UDAM**, is a theoretical model describing how uncertainty expands when an anchor is lost, and how small informative actions can re-anchor an agent's belief state.

日本語名：**不確実性拡散アンカーモデル**

## One-sentence summary

When uncertainty diffuses over time, low-cost informative actions can be rational because they re-anchor the agent's belief state.

不確実性は放置すると拡散する。だから、情報を返す小さな行動を細かく打ち、現在地を再アンカーし続ける戦略は合理的になりうる。

## Core intuition

The model begins with a timer example.

A person is counting toward a fixed deadline. They count accurately for a while, lose track during an interruption, and then start counting again.

The lost interval remains uncertain. However, the newly counted interval is not meaningless. It becomes a new anchor.

This simple structure generalizes to learning, work recovery, health tracking, relationship uncertainty, and life strategy after failure.

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

## General model

Uncertainty diffusion without an anchor:

```text
P_{t+Δt} = P_t + QΔt
```

Action value:

```text
V(a) = I(a) + B(a) - C(a)
```

where:

- `P_t`: uncertainty at time `t`
- `Q`: uncertainty diffusion rate
- `a`: action
- `I(a)`: informational value
- `B(a)`: intervention value
- `C(a)`: action cost
- `V(a)`: total action value

A small action is favorable when:

```text
V(a) > 0
```

## Main claim

If uncertainty diffuses in the absence of anchors, then low-cost informative actions can be advantageous because they reduce or constrain uncertainty growth.

This does **not** justify arbitrary action. It supports actions that return information, improve the state, or both, at sufficiently low cost.

## Applications

- time perception
- learning recovery
- work interruption recovery
- health tracking
- relationship uncertainty
- life strategy after failure
- cognitive re-orientation after disruption

## Failure cases

UDAM does not apply cleanly when:

- the action returns no information;
- the action cost exceeds its informational and intervention value;
- feedback is systematically misleading;
- repeated checking becomes compulsive and uninformative;
- the state does not diffuse without an anchor;
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

## License

Documentation and theory texts are licensed under **CC BY 4.0**.

Code, if added later, should be licensed separately, preferably under the MIT License unless otherwise stated.
