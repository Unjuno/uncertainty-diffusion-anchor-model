# Example: Learning Re-Anchor

## Situation

A learner stops studying for a period of time. After the interruption, they no longer know their actual skill level.

## Lost anchor

The lost anchor is the learner's calibrated sense of ability.

## State variable

The latent state is current skill level:

```text
S_t = current skill state
```

## Belief uncertainty

The learner is uncertain about what they still remember and what they can currently solve.

```text
P_{skill,t} = Var(S_t | D_t)
```

## Possible state dynamics

The actual skill state may change through forgetting, consolidation, or background learning.

```text
S_{t+Δt} may differ from S_t
```

## Belief dynamics

Even if the skill state has not changed much, the learner's uncertainty about it may increase without practice or testing.

```text
P_{skill,t+Δt} = P_{skill,t} + Q_skill Δt
```

## Re-anchoring action

Solve one problem.

## Informational value

The result reveals current ability more directly than thinking about ability.

```text
I(a) > 0
```

## Intervention value

Solving the problem may also train the skill slightly.

```text
B(a) >= 0
```

## Failure case

If the problem is too easy, it may not reveal the relevant uncertainty.

If the problem is too hard, it may create discouragement without useful calibration.

A good re-anchor should be small, concrete, and diagnostic.
