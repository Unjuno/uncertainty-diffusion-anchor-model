# 08 Related Work

UDAM is not presented as a completely new mathematical structure.

Its novelty, if any, lies in how several existing ideas are integrated around the timer-to-life-strategy generalization.

## State-space models and Kalman filtering

UDAM resembles the prediction-update structure of state-space models.

- Prediction without observation can increase uncertainty.
- Observation can reduce uncertainty.

Related concept:

```text
P_{t+Δt} = P_t + QΔt
```

Relevant reference:

- Kalman, R. E. (1960). A New Approach to Linear Filtering and Prediction Problems. DOI: 10.1115/1.3662552

## Bayesian filtering

UDAM treats the agent as holding a belief state over a partially observed current state.

Related concepts:

- prior belief;
- posterior update;
- observation likelihood;
- uncertainty reduction.

## POMDP and belief states

In partially observable decision processes, agents act under uncertainty about the true state.

UDAM's `P_t` can be understood as part of a belief state.

## Value of information

UDAM's `I(a)` term is related to the value of information.

Actions can be useful not only because they directly improve the state, but because they improve future decisions by reducing uncertainty.

## Active inference

Active inference also frames action as a way to reduce uncertainty and prediction error.

UDAM is narrower and more practical: it focuses on re-anchoring after anchor loss.

## Behavioral activation

Behavioral activation emphasizes action after withdrawal or low mood.

UDAM does not claim to be a clinical model. However, it gives an information-theoretic interpretation of why small actions after collapse can matter.

## Cognitive anchoring

The model also connects to anchoring and reference-point mechanisms in cognition.

UDAM uses the word anchor in a broad sense: any observation or action that constrains current-state uncertainty.

## Novelty statement

UDAM should not claim full mathematical originality.

A safer claim is:

> UDAM is a timer-derived cognitive and decision-theoretic formulation that integrates uncertainty diffusion, re-anchoring, and small informative actions into a practical theory of recovery after anchor loss.
