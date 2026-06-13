# Research Notes

## Related conceptual areas

UDAM connects to several existing fields.

## 1. Bayesian filtering

Agents update belief states from observations.

UDAM uses the same broad structure but focuses on anchor loss and re-anchoring.

## 2. Kalman filtering

Prediction without observation can increase uncertainty. Observation can reduce uncertainty.

UDAM's diffusion equation:

```text
P_{t+Δt} = P_t + QΔt
```

resembles the prediction-side growth of uncertainty.

## 3. POMDP

Partially observable Markov decision processes represent agents that act under hidden states.

UDAM's `P_t` can be treated as part of a belief state.

## 4. Value of information

Informative actions can improve future decisions by reducing uncertainty.

UDAM's `I(a)` is related to this idea.

## 5. Active inference

Active inference frames action as reducing uncertainty or prediction error.

UDAM is narrower: it focuses on small re-anchoring actions after anchor loss.

## 6. Behavioral activation

Behavioral activation uses action to counter withdrawal.

UDAM can reinterpret some small actions as information-producing re-anchors.

## Caution

UDAM should not overclaim mathematical novelty.

The safer novelty claim is:

> UDAM is a timer-derived cognitive and decision-theoretic formulation that integrates uncertainty diffusion, re-anchoring, and small informative action into a practical theory of recovery after anchor loss.
