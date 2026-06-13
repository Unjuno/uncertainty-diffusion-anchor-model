# 27 Literature Verification: Online Algorithms and Robust Decision Rules

This document continues Stage 2 of the five-stage refinement roadmap.

It checks online algorithms, competitive analysis, ski-rental-type tradeoffs, and robust decision-rule literature against UDAM claims about acting under unknown future conditions after anchor loss.

The goal is not to prove UDAM from online algorithms.

The goal is to classify which UDAM components are directly supported, partially supported, analogy-only, unsupported, or in need of wording correction.

## Sources checked

Reference candidates:

- Daniel D. Sleator and Robert E. Tarjan, "Amortized Efficiency of List Update and Paging Rules," Communications of the ACM, 1985.
- Anna R. Karlin, Mark S. Manasse, Lyle A. McGeoch, and Susan Owicki, "Competitive Randomized Algorithms for Non-Uniform Problems," Algorithmica, 1994.
- Allan Borodin and Ran El-Yaniv, *Online Computation and Competitive Analysis*, Cambridge University Press, 1998.
- Amos Fiat and Gerhard J. Woeginger, eds., *Online Algorithms: The State of the Art*, Lecture Notes in Computer Science 1442, 1998.
- Steven S. Seiden, "A Guessing Game and Randomized Online Algorithms," STOC, 2000.
- Michael Dinitz, Sungjin Im, Thomas Lavastida, Benjamin Moseley, and Sergei Vassilvitskii, "Controlling Tail Risk in Online Ski-Rental," arXiv:2308.05067, 2023.
- Nicolas Christianson, Bo Sun, Steven Low, and Adam Wierman, "Risk-Sensitive Online Algorithms," arXiv:2405.09859, 2024.

Core literature idea:

```text
an online algorithm must make decisions without knowing the future input sequence, and its performance is compared with an offline optimum that knows the future
```

This is close to a UDAM practical question:

```text
when the lost interval or future boundary is unknown, what rule is not too bad compared with an unavailable perfect rule?
```

But the match is limited.

Online algorithms usually define a precise input sequence, cost function, and offline comparator. UDAM is a broader practical synthesis for re-anchoring after anchor loss.

## Minimal notation

| Symbol | Meaning in this note | Unit | Definition | Domain / assumption | Type |
|---|---|---:|---|---|---|
| `t` | decision step | count | current online decision time | integer `t >= 1` | scalar |
| `x_t` | revealed input | problem-specific | information revealed at step `t` | not known before step `t` | random or adversarial variable |
| `a_t` | online action | dimensionless | action chosen after seeing current information, without future inputs | feasible action set | decision variable |
| `ALG(x)` | online algorithm cost | cost unit | cost incurred by the online rule on input sequence `x` | non-negative | scalar |
| `OPT(x)` | offline optimal cost | cost unit | minimum cost if the full sequence `x` were known in advance | positive when ratio is used | scalar |
| `rho` | competitive ratio | dimensionless | worst-case ratio between `ALG` and `OPT` | `rho >= 1` for cost minimization | scalar |
| `B` | buy or fixed commitment cost | cost unit | one-time cost in ski-rental-type problems | positive | scalar |
| `r` | recurring cost | cost per step | continuing cost when commitment is deferred | positive | scalar |
| `T` | unknown horizon | count | unknown duration of the process | positive integer | scalar |
| `s_i` | UDAM action or expansion scope | domain unit | scope chosen at expansion step `i` | positive | scalar |
| `P_boundary(i)` | boundary-crossing probability | probability | probability that an expansion or delay crosses adverse boundary | `[0,1]` | scalar |
| `C_boundary` | adverse boundary cost | utility unit | cost of boundary crossing | non-negative | scalar |

Dimension check:

```text
ALG(x) / OPT(x) = dimensionless
```

and:

```text
P_boundary(i) C_boundary = utility unit
```

Therefore online competitive ratios and UDAM utility inequalities are not the same mathematical object. They can be aligned conceptually only after defining a common cost model.

## Literature pattern

A basic online decision pattern is:

```text
observe current input -> choose action without future information -> incur cost -> repeat
```

Competitive analysis compares:

```text
online rule cost / offline optimum cost
```

Ski-rental-type problems express a recurring tradeoff:

```text
continue paying small repeated cost
or
pay a larger one-time cost without knowing future duration
```

This is close to UDAM's practical expansion problem:

```text
continue small probes
or
commit to larger action under unknown future duration and boundary location
```

But UDAM's setting is not necessarily a formal ski-rental instance.

## UDAM claim 1: Offline optimum may be unavailable

UDAM statement:

```text
when future duration or boundary location is unknown, the agent needs a robust sequential rule rather than a perfect offline optimum
```

Literature fit:

```text
direct support
```

Reason:

Online algorithms directly study decision-making where the future input sequence is not known at decision time. Competitive analysis explicitly compares online performance with an offline optimum that knows the future.

This directly supports the UDAM claim that the practical question is often not:

```text
what would have been optimal with full knowledge?
```

but:

```text
what rule is defensible without full knowledge?
```

Recommended wording:

```text
Online algorithms support UDAM's distinction between unavailable offline optimality and usable rules under incomplete future information.
```

Avoid:

```text
UDAM computes the offline optimum.
```

## UDAM claim 2: Robust rule differs from optimal rule

UDAM statement:

```text
what expansion factor is not too bad under uncertainty?
```

Literature fit:

```text
direct support for the distinction
partial support for UDAM expansion rules
```

Reason:

Competitive analysis evaluates how badly an online algorithm can perform relative to an offline optimum. It is a framework for judging rules that operate without future knowledge.

This supports UDAM's safer positioning:

```text
UDAM is a practical rule family under uncertainty, not a claim to compute the best possible action in hindsight.
```

However, UDAM does not currently define a formal competitive ratio for its expansion rule. Therefore the support is conceptual unless a UDAM-specific online cost model is specified.

Recommended wording:

```text
UDAM's expansion and probing rules should be framed as robust practical rules under incomplete future information, not as offline-optimal policies.
```

Avoid:

```text
UDAM gives the optimal expansion factor.
```

## UDAM claim 3: Repeated small costs versus one larger commitment

UDAM statement:

```text
repeated small cost versus one large decision
```

Nearby example:

```text
ski rental: rent repeatedly or buy once without knowing the future horizon
```

Literature fit:

```text
direct support for the tradeoff pattern
analogy only for general UDAM applications
```

Reason:

Ski-rental-type problems directly model a recurring cost versus one-time commitment under unknown duration.

This is structurally close to UDAM decisions such as:

```text
keep probing small
or
expand/commit before knowing how long the current uncertainty regime will last
```

But ski rental is narrower. It does not include belief-state updating, valid re-anchor conditions, boundary risk, or state-informative observation.

Recommended wording:

```text
Ski-rental-type tradeoffs provide a useful analogy for repeated small costs versus larger commitment under unknown duration, but they do not by themselves model UDAM's belief update or re-anchoring conditions.
```

Avoid:

```text
UDAM is just ski rental.
```

## UDAM claim 4: Boundary and tail risk matter

UDAM statement:

```text
P_boundary(i) * C_boundary
```

Literature fit:

```text
partial support from risk-sensitive online algorithms
UDAM-specific as a concrete term
```

Reason:

Recent online-algorithm literature considers tail risk, risk-sensitive competitive ratios, and robustness beyond expected competitive ratio. This is compatible with UDAM's concern that an action can be unacceptable because of low-probability high-cost boundary outcomes.

However, UDAM's boundary term is not a standard online-algorithm expression.

Recommended wording:

```text
Risk-sensitive online algorithms support the general need to account for adverse-tail behavior. UDAM's boundary-risk term remains a model-specific practical expression.
```

Avoid:

```text
P_boundary(i) * C_boundary is a standard competitive-analysis term.
```

## UDAM claim 5: Competitive ratio is not the same as expected utility

UDAM clarification:

```text
competitive ratio != expected utility
```

Literature fit:

```text
requires wording correction
```

Reason:

Competitive analysis usually measures ratio to an offline optimum. UDAM often uses expected value, information value, observation cost, correction cost, and boundary-risk cost.

These are related only after specifying a formal cost model.

Recommended wording:

```text
Online algorithms can inform UDAM's robust-rule positioning, but competitive ratio should not be conflated with UDAM's expected-value inequalities.
```

Avoid:

```text
UDAM's value inequality is a competitive ratio.
```

## UDAM claim 6: Online algorithms prove UDAM

UDAM statement:

```text
not claimed
```

Literature fit:

```text
not supported
```

Reason:

Online algorithms support robust decision rules under future uncertainty. They do not provide UDAM's timer seed model:

```text
tau = K + U + R
```

They also do not directly prove:

```text
anchor loss does not imply future anchor invalidation
```

Correct positioning:

```text
Online algorithms support UDAM's robust-rule framing under incomplete future information, while the anchor-loss synthesis remains UDAM-specific.
```

Avoid:

```text
UDAM is an online algorithm.
```

## Verification table

| UDAM claim | Online-algorithm support level | Reason | Correction |
|---|---:|---|---|
| offline optimum may be unavailable | direct support | online algorithms decide without future input | keep |
| robust rule differs from offline optimum | direct support | competitive analysis explicitly compares online and offline performance | keep |
| expansion factor should be robust, not claimed optimal | partial support | compatible with competitive analysis, but no UDAM ratio currently defined | avoid optimality claims |
| repeated small cost versus one larger commitment | direct for ski rental; analogy for UDAM | ski rental models rent-or-buy under unknown horizon | keep as analogy unless formalized |
| boundary/tail risk matters | partial support | risk-sensitive online algorithms consider tail risk | keep UDAM term specific |
| competitive ratio equals UDAM value inequality | not supported | ratio and utility inequality are different objects | reject |
| timer-derived anchor-loss structure | analogy only | online algorithms do not contain `tau = K + U + R` | keep UDAM-specific |
| literature proves UDAM as a whole | not supported | only robust-rule framing is supported | reject |

## Recommended repository wording

Use:

```text
Online algorithms support UDAM's robust-rule framing: when future inputs or durations are unknown, the relevant practical question is often how to choose a rule that is not too bad without future knowledge, not how to compute an unavailable offline optimum.
```

Use:

```text
Ski-rental-type tradeoffs are useful analogies for repeated small costs versus larger commitment under unknown duration, but they do not by themselves model UDAM's belief update, valid re-anchor condition, or boundary-risk term.
```

Use:

```text
Competitive analysis and UDAM expected-value inequalities are related only after a specific cost model is defined; they should not be conflated.
```

Avoid:

```text
UDAM gives the optimal expansion factor.
```

Avoid:

```text
UDAM is an online algorithm.
```

Avoid:

```text
UDAM's expansion inequality is a competitive ratio.
```

## Impact on current theory

No major correction is required.

Online algorithms strengthen the existing UDAM wording around:

```text
future information is unavailable
offline optimum is unavailable
robust sequential rules
repeated cost versus commitment
not-too-bad practical rules
```

The main cautions are:

```text
robust != optimal
competitive ratio != expected utility
ski rental is an analogy unless formally modeled
boundary-risk terms remain UDAM-specific
component support != full synthesis proof
```

## Next literature topic

The next check should be:

```text
implementation intentions / if-then planning
```

Reason:

The decision-theoretic and algorithmic support layers now cover observation value, informative feedback, repeated observation, probes, expansion, and robust rules. Implementation intentions are the next natural support for UDAM's practical action map:

```text
if result y occurs -> do action a(y)
```
