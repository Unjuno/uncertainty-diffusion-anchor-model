# Axioms

## Axiom 1: Anchor Loss

When an agent loses an anchor, part of the state becomes uncertain.

Timer form:

```text
τ = K + U + R
```

`U` is the uncertain part created by anchor loss.

## Axiom 2: Uncertainty Diffusion

Without anchoring observations, uncertainty increases or remains unchanged over time.

```text
P_{t+Δt} = P_t + QΔt
```

with:

```text
Q >= 0
Δt >= 0
```

If `Q > 0` and `Δt > 0`, then uncertainty strictly increases.

## Axiom 3: Re-Anchoring

An action that returns information about the current state can re-anchor the agent's belief state.

A minimal condition is:

```text
I(a) > 0
```

## Axiom 4: Action Value

An action has total value:

```text
V(a) = I(a) + B(a) - C(a)
```

An action is favorable under the model if:

```text
V(a) > 0
```

## Axiom 5: No Arbitrary Activity

Activity without information value or intervention value is not re-anchoring.

If:

```text
I(a) = 0
B(a) = 0
C(a) > 0
```

then:

```text
V(a) < 0
```

The model therefore rejects empty busyness.
