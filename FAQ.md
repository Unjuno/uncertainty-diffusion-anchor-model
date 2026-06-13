# FAQ

This FAQ is intended to prevent common misunderstandings of the Uncertainty-Diffusion Anchor Model.

## 1. Is UDAM saying that action is always better than inaction?

No.

UDAM supports action only when the action has positive value:

```text
V(a) = I(a) + B(a) - C(a) > 0
```

where:

- `I(a)` is informational value;
- `B(a)` is intervention value;
- `C(a)` is cost.

If an action returns no information, improves nothing, or costs too much, UDAM does not favor it.

## 2. What is the core idea?

The core idea is:

> Losing an anchor does not make all future anchors meaningless.

In the timer seed model:

```text
τ = K + U + R
```

where:

- `K` is the known interval before anchor loss;
- `U` is the unknown interval;
- `R` is the re-anchored known interval.

The lost interval `U` remains uncertain, but `R` can still be valid information.

## 3. Does re-anchoring always reduce absolute uncertainty?

No.

In the timer model, absolute uncertainty in `U` may remain or even increase.

The more precise claim is:

```text
absolute uncertainty may increase
relative influence may decrease
```

A representative ratio is:

```text
ρ = sqrt(Var(U)) / E[τ]
```

If the reference scale grows faster than the uncertainty scale, relative influence can decrease even when absolute uncertainty increases.

## 4. What does “fixed target” mean?

The timer seed model assumes:

```text
fixed target, uncertain position
```

It does not model:

```text
uncertain target, uncertain position
```

That means the model asks:

```text
Given a fixed target, where is the agent relative to it?
```

It does not ask:

```text
What is the probability that the target itself occurs?
```

## 5. Is this a claim that reality is deterministic?

No.

The fixed-target assumption is a local modeling constraint.

UDAM does not claim that all events are metaphysically deterministic. It only keeps event-occurrence uncertainty out of the core timer model so that the model can focus on position uncertainty and re-anchoring.

## 6. Why exclude event-occurrence uncertainty?

Because event occurrence is often not controlled by the agent.

UDAM is action-oriented. Its core variables should be variables that action can affect through:

- observation;
- belief update;
- decision improvement;
- state intervention.

If target occurrence itself is uncertain and uncontrollable, it should be treated as an external parameter, separate extension, or exception condition.

## 7. Does UDAM say the world gets worse when I do nothing?

No.

UDAM primarily concerns belief uncertainty.

It says:

```text
lack of anchors may increase uncertainty about S_t
```

not:

```text
inaction always worsens S_t
```

The model distinguishes:

```text
state dynamics: S_t changes
belief dynamics: P_t changes
```

## 8. What is a re-anchor?

A re-anchor is an action that creates or restores a reference point by returning information about the current state.

Examples:

- solving one problem;
- checking a task list;
- recording one health variable;
- sending one low-pressure message;
- restarting a count after losing track.

## 9. What is a missed re-anchor miscalculation?

It is a case where UDAM applies, but the agent fails to use it.

The common error is:

```text
partial uncertainty → total invalidation
```

UDAM's correction is:

```text
partial uncertainty → re-anchor if the next action has positive value
```

## 10. What is a happy miscalculation?

A happy miscalculation occurs when the agent expects or fears a poor state, but observation reveals that the current state is better than expected.

The common pattern is:

```text
uncertainty feels negative → observation reveals a better state than expected
```

This is not blind optimism.

It is an observability effect:

```text
uncertainty may hide upside
observation can reveal it
```

The action is still justified only when:

```text
V(a) > 0
```

## 11. Are high-stakes examples allowed?

Only as abstract, non-operational examples.

High-stakes examples can clarify the structure:

```text
fixed target
uncertain position
lost anchor
re-anchoring action
```

But the repository avoids vivid, operational, or harmful details.

Preferred wording includes:

- high-stakes fixed-deadline example;
- safety-critical fixed-target example;
- constrained decision context;
- upper time bound.

## 12. Is UDAM original?

UDAM should not claim full mathematical originality.

It is close to existing ideas such as:

- Bayesian filtering;
- Kalman filtering;
- belief-state models;
- value of information;
- active inference;
- behavioral activation.

Its contribution is the timer-derived formulation connecting uncertainty diffusion, re-anchoring, and small informative action into a practical model of recovery after anchor loss.

## 13. Does UDAM require simulations?

Not at the current stage.

The current goal is definitional precision:

- variables;
- assumptions;
- axioms;
- propositions;
- proof sketches;
- counterexamples;
- applications.

Simulations may be useful later, but they are not required for the initial theory note.
