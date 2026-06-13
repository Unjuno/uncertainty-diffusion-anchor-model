# 00 Overview

## Name

**Uncertainty-Diffusion Anchor Model**  
Abbreviation: **UDAM**  
Japanese: **不確実性拡散アンカーモデル**

## Core claim

When an agent loses an anchor, uncertainty about the current state can diffuse over time. Small actions that return information can re-anchor the agent's belief state and may be rational when their informational and intervention value exceeds their cost.

## Japanese formulation

アンカーを失った状態では、現在地に関する不確実性は時間とともに拡散しうる。情報を返す小さな行動は、認知状態を再アンカーしうる。その情報価値と介入価値がコストを上回るなら、その小行動は合理的である。

## Minimal intuition

The simplest case is a timer:

1. You count time accurately for a while.
2. You lose track during an interruption.
3. You restart counting.

The lost interval remains uncertain, but the restarted count is still valid information.

This rejects the all-or-nothing error:

> If the measurement failed once, all later measurement is meaningless.

UDAM says instead:

> Only the lost interval becomes uncertain. Future anchors still matter.

## Timer seed scope

The timer seed model assumes:

```text
fixed target, uncertain position
```

It does not model:

```text
uncertain target, uncertain position
```

The target condition is treated as fixed inside the local model. The agent's uncertainty is about current position relative to that target.

This is not a metaphysical claim that all reality is deterministic. It is a modeling constraint that keeps the seed argument narrow and strong.

## Controllability boundary

UDAM is action-oriented.

The core model includes uncertainty that action can affect through at least one of:

- observation;
- belief update;
- decision improvement;
- state intervention.

Uncontrollable external uncertainty, such as whether an external target condition occurs, is excluded from the core model or treated as an exception layer.

## Model scope

UDAM is a cognitive and decision-theoretic model. It is not a claim that every action is good. It applies only when:

- the state is partially unknown;
- uncertainty increases without anchoring;
- an action returns information or improves the state;
- the action cost is not larger than its value;
- the relevant uncertainty is actionable or at least observable.

## Minimal equations

```text
τ = K + U + R
P_{t+Δt} = P_t + QΔt
V(a) = I(a) + B(a) - C(a)
```

## Interpretation

- `τ = K + U + R` is the timer model.
- `P_{t+Δt} = P_t + QΔt` is belief-uncertainty diffusion.
- `V(a) = I(a) + B(a) - C(a)` is action-value evaluation.

## High-stakes examples

High-stakes examples can be useful when they clarify the abstract structure:

```text
fixed target
uncertain position
lost anchor
re-anchoring action
```

However, public examples should remain neutral and non-operational. The repository preserves the structure, not vivid scenario details.

## Current status

This repository is a theory repository. Simulations are not required for the initial formulation. The priority is definitional precision.
