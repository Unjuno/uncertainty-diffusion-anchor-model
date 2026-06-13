# State-Belief Separation

This file separates state dynamics from belief uncertainty dynamics.

## State dynamics

Let `S_t` be the latent state.

A general state transition can be written as:

```text
S_{t+Δt} = f(S_t, Δt, w_t)
```

where `w_t` is process noise or unmodeled change.

This describes how the state itself changes.

## Belief dynamics

Let `D_t` be the observation history available to the agent.

The agent's belief is:

```text
p(S_t | D_t)
```

The uncertainty of this belief, in the variance formulation, is:

```text
P_t = Var(S_t | D_t)
```

This describes what the agent knows or does not know.

## Minimal UDAM equation

UDAM's core uncertainty equation:

```text
P_{t+Δt} = P_t + QΔt
```

is a belief-uncertainty equation.

It should not automatically be read as a physical state deterioration equation.

## Observation update

A re-anchoring action `a` may return an observation `y_a`.

The updated belief is:

```text
p(S_t | D_t, y_a)
```

In variance form:

```text
P_t^+ = Var(S_t | D_t, y_a)
```

## Action value decomposition

The action-value equation:

```text
V(a) = I(a) + B(a) - C(a)
```

separates two roles:

- `I(a)`: belief-update value;
- `B(a)`: state-intervention value.

An action can have high `I(a)` without high `B(a)`, or high `B(a)` without high `I(a)`.

## Examples

| Action | Belief update `I(a)` | State intervention `B(a)` |
|---|---:|---:|
| inspect project state | high | low to medium |
| solve one problem | high | medium |
| record one health metric | medium | low |
| repair one broken task | medium | high |
| compulsive checking | low | low or negative |

## Formal caution

A future fully formal version should use two equations:

```text
S_{t+Δt} = f(S_t, Δt, w_t)
P_{t+Δt} = g(P_t, Δt, Q, D_t)
```

The current minimal model uses only the second equation because it focuses on uncertainty and re-anchoring.
