# Evidence Hierarchy

This note defines how UDAM claims should be supported.

The goal is to make the theory more convincing without overclaiming.

## Evidence levels

UDAM claims can be supported at different levels.

```text
Level 1: timer intuition
Level 2: internal logical coherence
Level 3: concrete examples
Level 4: failure cases and counterexamples
Level 5: nearby literature
Level 6: empirical testing or simulation
```

The repository currently has strong support at Levels 1-4, partial support at Level 5, and little or no support at Level 6.

That is acceptable for a hobby theory project.

## Level 1: Timer intuition

A claim has Level 1 support when it follows from the timer seed model.

Core form:

```text
τ = K + U + R
```

Example claim:

```text
A lost interval does not invalidate future anchors.
```

Support status:

```text
strong
```

Reason:

`R` is still part of the elapsed-position decomposition even when `U` is uncertain.

## Level 2: Internal logical coherence

A claim has Level 2 support when it is consistent with the model's variables, propositions, and boundary conditions.

Relevant files:

- `theory/propositions.md`
- `theory/variables.md`
- `theory/logical_synthesis_review.md`
- `theory/consistency_review.md`

Example claim:

```text
Observation is useful only when it is state-informative and cost-justified.
```

Support status:

```text
strong
```

Reason:

The model distinguishes:

```text
P(y | S) != P(y)
```

from:

```text
OV > 0
```

## Level 3: Concrete examples

A claim has Level 3 support when it can be explained through readable examples.

Relevant files:

- `examples/`
- `docs/ja/05_failure_examples.md`

Example claim:

```text
Repeated observation can become a checking loop.
```

Support status:

```text
moderate to strong
```

Reason:

Examples show how first observation and repeated observation diverge.

## Level 4: Failure cases and counterexamples

A claim has Level 4 support when the repository identifies where it fails.

Relevant files:

- `docs/06_failure_cases.md`
- `theory/counterexamples.md`
- `examples/failure_*.md`

Example claim:

```text
UDAM does not justify arbitrary small action.
```

Support status:

```text
strong
```

Reason:

The theory explicitly rejects:

```text
P(y | S) = P(y)
a(y) = a_0
MOV_i <= 0
```

and excessive expansion:

```text
B_expand(r_i) + I_expand(r_i) <= C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
```

## Level 5: Nearby literature

A claim has Level 5 support when it is consistent with existing theories or literature.

Relevant files:

- `notes/literature_verification.md`
- `docs/08_related_work.md`
- `docs/17_literature_support_map.md`

Current status:

```text
partially mapped, not fully verified
```

Priority areas:

```text
value of information
Blackwell informativeness
Bayesian experimental design
sequential analysis
multi-armed bandits
active inference
implementation intentions
exponential search
online algorithms
behavioral activation
```

Important caution:

```text
nearby literature support != proof that UDAM is new
```

The proper claim is:

```text
UDAM is consistent with several existing frameworks, but each connection should be verified separately.
```

## Level 6: Empirical testing or simulation

A claim has Level 6 support when tested empirically or by simulation.

Current status:

```text
deferred
```

Possible future tests:

- interrupted timer task;
- learning restart task;
- task-state recovery task;
- checking-loop comparison;
- adaptive expansion comparison.

This level is not required for the current hobby theory stage.

## Claim support table

| UDAM claim | Current support level | Status |
|---|---:|---|
| Lost interval does not invalidate future anchor | 1, 2, 3, 4 | strong |
| Belief uncertainty can diffuse without anchors | 2, 3, 4, partial 5 | moderate to strong |
| Small informative action can be rational | 2, 3, 4, partial 5 | moderate to strong |
| Any small action is useful | rejected | false |
| Observation is useful if state-informative | 2, 4, partial 5 | incomplete wording unless cost included |
| Observation is favorable if `OV > 0` | 2, 4, partial 5 | strong internally, literature to verify |
| Repeated checking is justified | rejected | false |
| Repeated observation is justified if `MOV_i > 0` | 2, 3, 4 | strong internally |
| Doubling is always optimal | rejected | false |
| Geometric expansion can be useful | 2, 3, 4, partial 5 | moderate |
| Expansion must account for boundary risk | 2, 3, 4 | strong internally |
| Local observation proves global conclusion | rejected | false |
| UDAM is a new mathematical foundation | rejected | false |
| UDAM is a timer-derived practical synthesis | 1, 2, 3, 4, partial 5 | strong as positioning |

## How to use this hierarchy

When adding a new claim, write:

```text
Claim:
Support level:
Files supporting it:
Known failure cases:
Literature status:
```

Example:

```text
Claim: A valid re-anchor must be state-informative.
Support level: 2, 4, partial 5.
Files: propositions, counterexamples, failure examples.
Known failure: P(y | S) = P(y).
Literature status: Blackwell informativeness to verify.
```

## Recommended writing rule

Do not write:

```text
This is proven.
```

unless the proof status is explicit.

Prefer:

```text
This is internally coherent under the model assumptions.
```

or:

```text
This is supported by the timer seed model and by explicit failure boundaries.
```

or:

```text
This is consistent with nearby literature, pending verification.
```

## Current verdict

UDAM is currently strongest as:

```text
a coherent practical framework with explicit boundary conditions
```

not as:

```text
a fully verified empirical theory
```

This is enough for the current stage.
