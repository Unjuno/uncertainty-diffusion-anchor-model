# Definitions

## Definition 1: State

A **state** is the latent condition the agent is trying to locate, estimate, or act upon.

Examples:

- elapsed time;
- project status;
- skill level;
- relationship state;
- health state;
- self-state after failure.

Symbol:

```text
S_t
```

## Definition 2: Belief state

A **belief state** is the agent's probability-bearing representation of the current state.

It is conditioned on observation history:

```text
p(S_t | D_t)
```

## Definition 3: Uncertainty

**Uncertainty** is the spread of the agent's belief state.

In the minimal variance formulation:

```text
P_t = Var(S_t | D_t)
```

## Definition 4: Anchor

An **anchor** is an observation, count, record, action, or feedback signal that constrains the belief state.

## Definition 5: Anchor loss

**Anchor loss** occurs when the agent loses a reference point that previously constrained the belief state.

Timer form:

```text
τ = K + U + R
```

`U` is the uncertain interval created by anchor loss.

## Definition 6: Uncertainty diffusion

**Uncertainty diffusion** is the growth of uncertainty under missing or absent anchoring observations.

Minimal form:

```text
P_{t+Δt} = P_t + QΔt
```

## Definition 7: Re-anchoring

**Re-anchoring** is the creation of a new anchor after anchor loss.

An action is a re-anchor if it returns information about the current state or improves the state in a way relevant to future decisions.

## Definition 8: Informative action

An **informative action** is an action with positive informational value:

```text
I(a) > 0
```

## Definition 9: Empty activity

**Empty activity** is an action with no informational value and no intervention value but positive cost.

```text
I(a) = 0
B(a) = 0
C(a) > 0
```

It follows that:

```text
V(a) < 0
```

## Definition 10: Positive high-frequency re-anchoring

A strategy of taking repeated small actions that return information or improve the state at low cost.

This is not the same as impulsive hyperactivity.
