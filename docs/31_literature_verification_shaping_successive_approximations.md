# 31 Literature Verification: Shaping and Successive Approximations

This document continues Stage 2 of the five-stage refinement roadmap.

It checks shaping, successive approximations, operant reinforcement, graded action, and reward-shaping analogies against UDAM claims about gradual expansion after successful small steps.

The goal is not to present UDAM as behavior analysis or reinforcement-learning reward shaping.

The goal is to classify which UDAM components are directly supported, partially supported, analogy-only, unsupported, or in need of wording correction.

## Sources checked

Reference candidates:

- B. F. Skinner, *The Behavior of Organisms*, 1938.
- B. F. Skinner, *Science and Human Behavior*, 1953.
- G. B. Peterson, "A Day of Great Illumination: B. F. Skinner's Discovery of Shaping," Journal of the Experimental Analysis of Behavior, 2004.
- John O. Cooper, Timothy E. Heron, and William L. Heward, *Applied Behavior Analysis*, multiple editions.
- Raymond G. Miltenberger, *Behavior Modification: Principles and Procedures*, multiple editions.
- A. Y. Ng, D. Harada, and S. Russell, "Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping," ICML, 1999.
- Eric Wiewiora, "Potential-Based Shaping and Q-Value Initialization are Equivalent," 2011.

Core literature idea:

```text
complex or initially unavailable behavior can be built by reinforcing successive approximations toward a target behavior
```

This is close to a UDAM practical expansion pattern:

```text
small valid step -> favorable response -> slightly larger step -> repeat under constraints
```

But the match is limited.

Shaping is a reinforcement procedure. UDAM is a decision-theoretic re-anchoring model with state-informativeness, observation value, and boundary-risk checks.

## Minimal notation

| Symbol | Meaning in this note | Unit | Definition | Domain / assumption | Type |
|---|---|---:|---|---|---|
| `b_i` | approximation behavior | dimensionless | current behavioral approximation at step `i` | emitted or feasible behavior | behavior |
| `b*` | target behavior | dimensionless | desired final behavior | defined by trainer or task | behavior |
| `R_i` | reinforcement at step `i` | reinforcement unit | consequence that increases selected behavior | contingent on behavior | scalar / event |
| `d(b_i,b*)` | distance to target | task-specific | how far current approximation is from target behavior | non-negative | scalar |
| `s_i` | UDAM action or observation scope | domain unit | current tested scope | positive | scalar |
| `r_i` | expansion factor | dimensionless | `s_{i+1}/s_i` | usually `r_i > 1` for expansion | scalar |
| `y_i` | observed response | dimensionless | result of action or observation at step `i` | observable | observation |
| `B_expand(r_i)` | expansion benefit | utility unit | expected benefit of increasing scope | domain-specific | scalar |
| `I_expand(r_i)` | expansion information value | utility unit | expected information from larger scope | domain-specific | scalar |
| `C_obs(r_i)` | observation cost | utility unit | cost of larger probe or observation | non-negative | scalar |
| `P_boundary(i)` | boundary-crossing probability | probability | probability of adverse boundary crossing at step `i` | `[0,1]` | scalar |
| `C_boundary` | adverse boundary cost | utility unit | cost if boundary is crossed | non-negative | scalar |
| `C_correct(r_i)` | correction cost | utility unit | expected cost of rollback or correction | non-negative | scalar |

Dimension check:

```text
B_expand(r_i) + I_expand(r_i) - C_obs(r_i) - P_boundary(i) C_boundary - C_correct(r_i) = utility unit
```

Shaping literature does not by itself define this inequality. It supports gradual approximation and reinforcement-contingent progression, not UDAM's boundary-risk utility calculation.

## Literature pattern

A simplified shaping pattern is:

```text
select target behavior -> reinforce current approximation -> require closer approximation -> repeat until target behavior is reached
```

A simplified UDAM expansion pattern is:

```text
select small valid action -> observe result -> if favorable and safe, expand scope -> repeat under boundary-risk constraints
```

The overlap is:

```text
gradual progression through smaller feasible steps rather than direct jump to a distant target
```

The difference is:

```text
shaping changes behavior through reinforcement contingencies
UDAM changes action scope through observation, value, and boundary-risk checks
```

## UDAM claim 1: Small successful steps can support gradual expansion

UDAM statement:

```text
small valid observation -> favorable result -> expand scope
```

Literature fit:

```text
partial support
```

Reason:

Shaping directly supports the idea that complex or initially difficult behavior can be approached through successive approximations rather than one large jump.

This supports UDAM's practical intuition that a small successful step can be used as a basis for gradual progression.

The support is partial because UDAM expansion is not merely reinforced behavior. UDAM requires renewed checks of information value, cost, and boundary risk at each expansion step.

Recommended wording:

```text
Shaping supports UDAM's gradual-progression intuition: a distant target can sometimes be approached through successful intermediate approximations. UDAM adds decision-theoretic checks before each expansion.
```

Avoid:

```text
A small success always justifies expansion.
```

## UDAM claim 2: Expansion should be stepwise rather than global

UDAM statement:

```text
local observation does not imply global conclusion
```

Literature fit:

```text
partial support
```

Reason:

Shaping works through successive approximations. This is compatible with UDAM's warning against jumping from a local success to a global conclusion.

However, shaping does not directly address epistemic generalization, boundary risk, or state-informativeness. It is not a proof that stepwise expansion is always safer.

Recommended wording:

```text
Shaping is compatible with UDAM's preference for stepwise progression over global leaps, but safety and validity still require separate checks.
```

Avoid:

```text
Stepwise expansion is always safe.
```

## UDAM claim 3: Reinforcement is not the same as evidence of state validity

UDAM clarification:

```text
reinforced response != valid re-anchor
```

Literature fit:

```text
requires wording correction
```

Reason:

In shaping, a behavior is strengthened because it is reinforced. In UDAM, an observation is valid because it is state-informative or action-relevant.

These are different criteria.

A reinforced behavior may be useful for skill acquisition without being evidence about the hidden state `S`.

Recommended wording:

```text
Shaping supports behavioral progression, not UDAM's state-informative observation condition.
```

Avoid:

```text
If a step was reinforced, it was a valid re-anchor.
```

## UDAM claim 4: Reward shaping is only an analogy for UDAM expansion

UDAM statement:

```text
not a reinforcement-learning reward-shaping algorithm
```

Literature fit:

```text
analogy only
```

Reason:

Reward shaping in reinforcement learning can speed learning by modifying rewards, and potential-based reward shaping is designed to preserve optimal policies under specific conditions.

This is conceptually nearby because it changes the learning landscape without changing the target objective.

However, UDAM does not currently define a Markov decision process, reward function, potential function, or policy-invariance theorem.

Recommended wording:

```text
Reward shaping is a useful analogy for guided progression, but UDAM is not a reward-shaping algorithm unless a formal reinforcement-learning model is specified.
```

Avoid:

```text
UDAM is potential-based reward shaping.
```

## UDAM claim 5: Every expansion should be reinforced or repeated

UDAM statement:

```text
not claimed
```

Literature fit:

```text
not supported
```

Reason:

Shaping involves repeated reinforcement of approximations. UDAM involves repeated decision points under uncertainty.

A UDAM expansion may stop, switch, contract, or change observation mode even after a local success if boundary risk, cost, or diminishing marginal observation value becomes unfavorable.

Recommended wording:

```text
UDAM can use successful steps as evidence for possible progression, but each new scope remains a separate decision.
```

Avoid:

```text
Once a step works, keep reinforcing and expanding.
```

## UDAM claim 6: Shaping proves UDAM

UDAM statement:

```text
not claimed
```

Literature fit:

```text
not supported
```

Reason:

Shaping supports a gradual behavior-building procedure. It does not provide UDAM's timer seed model:

```text
tau = K + U + R
```

It also does not directly prove:

```text
anchor loss does not imply future anchor invalidation
```

Correct positioning:

```text
Shaping supports UDAM's gradual-progression analogy, while the anchor-loss, observability-value, and boundary-risk layers remain UDAM-specific.
```

Avoid:

```text
UDAM is shaping.
```

## Verification table

| UDAM claim | Shaping support level | Reason | Correction |
|---|---:|---|---|
| small successful steps can support gradual expansion | partial support | shaping uses successive approximations toward target behavior | keep as practical analogy |
| stepwise progression can avoid one large jump | partial support | shaping progresses through intermediate approximations | still needs safety and value checks |
| reinforced response equals valid re-anchor | not supported | reinforcement and state-informativeness are different | reject |
| reward shaping equals UDAM expansion | analogy only | RL reward shaping requires formal MDP and reward model | keep separate |
| local success justifies global expansion | not supported | shaping is stepwise and contingent; not global validation | reject |
| repeated reinforcement means keep expanding | not supported | UDAM may stop, switch, or contract | reject |
| timer-derived anchor-loss structure | analogy only | shaping does not contain `tau = K + U + R` | keep UDAM-specific |
| literature proves UDAM as a whole | not supported | only gradual-progression analogy is supported | reject |

## Recommended repository wording

Use:

```text
Shaping and successive approximations partially support UDAM's gradual-expansion intuition: progress can sometimes be built through successful intermediate steps rather than a single global leap.
```

Use:

```text
UDAM differs from shaping because each expansion still requires observation value, cost, actionability, and boundary-risk checks.
```

Use:

```text
A reinforced or successful intermediate step is not automatically a valid re-anchor or permission for global expansion.
```

Avoid:

```text
UDAM is shaping.
```

Avoid:

```text
Reward shaping proves UDAM's expansion rule.
```

Avoid:

```text
Every successful small step should be expanded.
```

## Impact on current theory

No major correction is required.

Shaping strengthens the existing UDAM wording around:

```text
gradual progression
intermediate approximations
small-to-larger practical movement
avoiding direct jumps to global action
```

The main cautions are:

```text
reinforcement != state-informativeness
successive approximation != boundary-risk permission
reward shaping != UDAM expansion
local success != global validation
component support != full synthesis proof
```

## Stage 2 status after this check

This completes the planned first-pass literature verification set in the current roadmap sequence.

Remaining future literature work may still be added, but the core nearby literatures now have first-pass support classification.

The next project stage should likely move from Stage 2 to Stage 3:

```text
visual explanation
```

Reason:

The theory now has a substantial support map. The next bottleneck is reader comprehension, not additional concepts.
