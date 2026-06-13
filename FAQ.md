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

## 11. What is a false comfort miscalculation?

A false comfort miscalculation occurs when the agent assumes the state is safe, manageable, or favorable, but observation would reveal hidden downside.

The common pattern is:

```text
uncertainty feels manageable → no observation → hidden downside appears later
```

This is the negative counterpart to happy miscalculation.

It is not a reason for compulsive checking. The action is still justified only when:

```text
V(a) > 0
```

## 12. What is fixed-target disbelief?

Fixed-target disbelief is a false-comfort pattern where the agent dismisses a fixed target condition and therefore fails to re-anchor position relative to it.

The pattern is:

```text
fixed target is dismissed → no re-anchor → hidden downside remains unmanaged
```

In high-stakes examples, this is why disbelief can reverse the intended effect of UDAM.

The model should describe this abstractly and non-operationally.

## 13. Are high-stakes examples allowed?

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

## 14. Does UDAM say to keep expanding after a good result?

No.

UDAM allows expansion after favorable observations, but only when expansion value exceeds its costs.

The scope update is:

```text
s_{i+1} = r_i s_i
```

A common pattern is:

```text
1 -> 2 -> 4 -> 8
```

But expansion is favorable only when:

```text
B_expand(r_i) + I_expand(r_i) > C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
```

So expansion is constrained by boundary risk, observation cost, and correction cost.

## 15. Is doubling always optimal?

No.

Doubling can be a useful default when the useful scale is unknown and prior probes are favorable.

But it is not universally optimal.

Use a smaller factor when:

```text
boundary risk is high
correction cost is high
the state changes quickly
the action is hard to reverse
```

Use a larger factor only when:

```text
observation cost is high
boundary risk is low
correction is easy
the state is stable
```

## 16. Is UDAM original?

UDAM should not claim full mathematical originality.

It is close to existing ideas such as:

- Bayesian filtering;
- Kalman filtering;
- belief-state models;
- value of information;
- active inference;
- behavioral activation;
- exponential search;
- online decision rules.

Its contribution is the timer-derived formulation connecting uncertainty diffusion, re-anchoring, observability value, conditional action, and boundary-risk-constrained expansion into a practical model of recovery after anchor loss.

## 17. Does UDAM require simulations?

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
