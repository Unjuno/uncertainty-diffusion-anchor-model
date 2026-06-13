# Paper Outline

## Working title

Uncertainty-Diffusion Anchor Model: Why Small Informative Actions Are Rational After Anchor Loss

## Abstract draft

This paper introduces the Uncertainty-Diffusion Anchor Model (UDAM), a cognitive and decision-theoretic model of how agents recover after losing a reference point for their current state. The model begins from a timer example: after losing track of elapsed time, restarting the count does not recover the lost interval but does create a new anchor. This structure is generalized to partially observed states where uncertainty diffuses over time without anchoring observations. The model proposes that low-cost informative actions can be rational because they re-anchor the agent's belief state. The paper distinguishes re-anchoring from arbitrary activity and identifies failure cases such as compulsive checking, misleading feedback, and high-cost action.

## Sections

1. Introduction
2. Timer model
3. Uncertainty diffusion
4. Re-anchoring actions
5. Action value
6. Propositions and proof sketches
7. Failure cases
8. Applications
9. Related work
10. Limitations
11. Conclusion

## Core equations

```text
τ = K + U + R
P_{t+Δt} = P_t + QΔt
V(a) = I(a) + B(a) - C(a)
```

## Main contribution

UDAM reframes small actions after disruption as information-producing re-anchors rather than mere effort or optimism.
