# 25 Literature Verification: Multi-Armed Bandits and Exploration-Exploitation

This document continues Stage 2 of the five-stage refinement roadmap.

It checks multi-armed bandits and exploration-exploitation literature against UDAM claims about small probes, learning by acting, and adaptive switching after anchor loss.

The goal is not to prove UDAM from bandit theory.

The goal is to classify which UDAM components are directly supported, partially supported, analogy-only, unsupported, or in need of wording correction.

## Sources checked

Reference candidates:

- Herbert Robbins, "Some Aspects of the Sequential Design of Experiments," Bulletin of the American Mathematical Society, 1952.
- John C. Gittins, "Bandit Processes and Dynamic Allocation Indices," Journal of the Royal Statistical Society, Series B, 1979.
- T. L. Lai and Herbert Robbins, "Asymptotically Efficient Adaptive Allocation Rules," Advances in Applied Mathematics, 1985.
- Peter Auer, Nicolo Cesa-Bianchi, and Paul Fischer, "Finite-time Analysis of the Multiarmed Bandit Problem," Machine Learning, 2002.
- Peter Auer, Nicolo Cesa-Bianchi, Yoav Freund, and Robert E. Schapire, "The Nonstochastic Multiarmed Bandit Problem," SIAM Journal on Computing, 2002.
- Sebastien Bubeck and Nicolo Cesa-Bianchi, "Regret Analysis of Stochastic and Nonstochastic Multi-armed Bandit Problems," Foundations and Trends in Machine Learning, 2012; arXiv:1204.5721.

Core literature idea:

```text
an agent repeatedly chooses actions under uncertainty, observes feedback only from chosen actions, and must balance exploration and exploitation
```

This is close to the UDAM probe pattern:

```text
small action -> local feedback -> belief update -> continue, switch, or expand
```

But the match is limited.

Bandit theory usually formalizes repeated action selection among arms with reward feedback and regret criteria. UDAM is a broader practical model for re-anchoring after anchor loss.

## Minimal notation

| Symbol | Meaning in this note | Unit | Definition | Domain / assumption | Type |
|---|---|---:|---|---|---|
| `t` | round index | count | current bandit decision step | integer `t >= 1` | scalar |
| `k` | arm index | count | candidate action or probe option | `k in {1, ..., K}` | scalar |
| `K` | number of arms | count | number of candidate actions | positive integer | scalar |
| `A_t` | chosen arm/action | dimensionless | action selected at round `t` | `A_t in {1, ..., K}` | random variable / decision variable |
| `X_t` | observed reward or feedback | utility unit or score | result observed after choosing `A_t` | distribution depends on chosen arm | random variable |
| `mu_k` | expected reward of arm `k` | utility unit per pull | `mu_k = E[X_t | A_t = k]` | finite expectation assumed | scalar |
| `mu_star` | best expected reward | utility unit per pull | `mu_star = max_k mu_k` | finite arm set | scalar |
| `R_T` | cumulative regret | utility unit | loss versus always choosing the best arm in hindsight or expectation | horizon `T` | scalar |
| `S` | UDAM-relevant state | dimensionless | state being inferred or acted on after anchor loss | domain-specific | random variable |
| `a_probe` | UDAM small probe action | dimensionless | action selected partly to learn and partly to act | must be bounded and actionable | decision variable |
| `B(a)` | benefit of action | utility unit | expected practical benefit | domain-specific | scalar |
| `I(a)` | informational value of action | utility unit | expected information contribution of action | domain-specific | scalar |
| `C(a)` | action cost | utility unit | cost of acting | usually non-negative | scalar |

Dimension check:

```text
B(a) + I(a) - C(a) = utility unit
```

Therefore UDAM can compare probe actions only if benefit, information value, and cost are expressed on a compatible utility scale.

## Literature pattern

A simplified stochastic bandit problem is:

```text
choose A_t -> observe X_t from the chosen arm only -> update estimates -> choose A_{t+1}
```

A standard regret expression is:

```text
R_T = T mu_star - sum_{t=1}^T X_t
```

The key tradeoff is:

```text
exploration: choose an uncertain option to learn
exploitation: choose the option currently believed to be best
```

This directly supports the idea that some actions are valuable because they are both actions and observations.

But standard bandit feedback is narrower than UDAM feedback. UDAM's probe may affect the world, cross a boundary, change relationships, consume cognitive resources, or produce delayed consequences.

## UDAM claim 1: A small probe can be both action and observation

UDAM statement:

```text
small probes can balance learning and action
```

Related UDAM pattern:

```text
probe small -> observe response -> update belief -> continue, switch, or expand
```

Literature fit:

```text
direct support for action-with-feedback structure
partial support for UDAM's practical probe framing
```

Reason:

Bandit theory directly studies actions whose outcomes provide both reward and information about future action value. The agent learns only through selected actions.

This supports the UDAM idea that a small action can be epistemically useful, not merely practically useful.

However, UDAM's `small probe` is not necessarily a bandit arm. It may be a local practical action after anchor loss, with domain-specific constraints and boundary risks.

Recommended wording:

```text
Multi-armed bandit theory directly supports the action-with-feedback structure: selected actions can both produce payoff and reveal information for later action choice. UDAM uses this as a practical small-probe layer after anchor loss.
```

Avoid:

```text
Every small action is a bandit arm.
```

## UDAM claim 2: Exploration-exploitation supports conditional switching

UDAM statement:

```text
observe locally, update belief, then expand or switch action
```

Literature fit:

```text
direct support for adaptive action selection
partial support for UDAM expansion and switching language
```

Reason:

Bandit policies adapt later choices using prior feedback. This directly supports the idea that feedback can change future action selection.

This is aligned with UDAM's conditional action condition:

```text
a(y) != a_0
```

But bandit theory usually optimizes a sequence of arm pulls under a defined reward model. UDAM uses a broader practical action map, where the next action may change category, scope, or risk boundary.

Recommended wording:

```text
Bandit theory supports adaptive action selection from feedback. UDAM's conditional switching is aligned with this, but remains broader than arm selection in a standard bandit model.
```

Avoid:

```text
UDAM conditional switching is just UCB.
```

## UDAM claim 3: Exploration has a cost and should not be unlimited

UDAM statement:

```text
Any small action is not automatically useful.
```

Related UDAM expression:

```text
V(a) = I(a) + B(a) - C(a)
```

Literature fit:

```text
direct support
```

Reason:

Bandit theory measures the cost of exploration through regret. Pulling uncertain or suboptimal arms can be useful for learning, but it can also reduce cumulative reward.

This supports the UDAM distinction:

```text
information-producing != favorable
```

A probe must have expected value after accounting for cost, risk, and later action usefulness.

Recommended wording:

```text
Exploration can be valuable, but it is not free. Bandit theory supports treating exploratory action as a value tradeoff rather than as automatically beneficial.
```

Avoid:

```text
Try anything small; it will help.
```

## UDAM claim 4: The probe must be tied to feedback that can change later action

UDAM statement:

```text
P(y | S) != P(y)
```

and:

```text
a(y) != a_0
```

Literature fit:

```text
partial support
```

Reason:

Bandit feedback matters because it changes estimates of arm value and can alter later allocation. This is compatible with UDAM's requirement that an observation must be state-informative and action-relevant.

However, bandit feedback is usually reward feedback about arms, not necessarily a general belief update about a hidden state `S`. Contextual bandits and Bayesian bandits are closer, but standard bandits do not cover every UDAM re-anchor case.

Recommended wording:

```text
Bandit feedback supports UDAM's requirement that probes should generate action-relevant feedback. The exact state-informative condition remains UDAM-specific unless a bandit state model is explicitly defined.
```

Avoid:

```text
Bandit feedback is the same as UDAM's valid re-anchor condition.
```

## UDAM claim 5: Local probe success does not justify global expansion automatically

UDAM statement:

```text
local observation does not imply global conclusion
```

and:

```text
expansion must respect boundary risk
```

Literature fit:

```text
partial support for cautious adaptation
not supported for UDAM's boundary-risk term
```

Reason:

Bandit theory supports adapting based on observed feedback, but it does not automatically justify unbounded expansion from one successful probe. In fact, regret analysis exists because local exploration can be costly.

However, UDAM's boundary-risk term:

```text
P_boundary(i) * C_boundary
```

is not a standard bandit term. Some bandit variants include safety, constraints, or risk sensitivity, but classical MAB does not directly provide UDAM's boundary-risk-constrained expansion rule.

Recommended wording:

```text
Bandit theory supports feedback-based adaptation, but it does not imply that a successful local probe justifies global expansion. UDAM's boundary-risk constraint remains a separate practical layer.
```

Avoid:

```text
A successful probe means doubling is optimal.
```

## UDAM claim 6: Bandit theory proves UDAM

UDAM statement:

```text
not claimed
```

Literature fit:

```text
not supported
```

Reason:

Bandit theory supports a sequential action-feedback tradeoff. It does not provide UDAM's timer seed model:

```text
tau = K + U + R
```

It also does not directly prove:

```text
anchor loss does not imply future anchor invalidation
```

Correct positioning:

```text
Bandit theory supports UDAM's small-probe and exploration-exploitation layer, while the anchor-loss synthesis remains UDAM-specific.
```

Avoid:

```text
UDAM is a multi-armed bandit theory.
```

## Verification table

| UDAM claim | Bandit support level | Reason | Correction |
|---|---:|---|---|
| small probe can be both action and observation | direct / partial | direct for action-with-feedback; partial for practical post-anchor-loss probe | say aligned, not identical |
| feedback can change later action | direct support | bandit policies adapt later arm choices from feedback | keep |
| exploration is useful but costly | direct support | regret formalizes exploration cost | keep strongly |
| any small action is useful | not supported | exploration can be costly or irrelevant | reject |
| state-informative feedback enables action change | partial support | compatible with bandit feedback, but UDAM's `S` may be broader than arm reward | define state if formalizing |
| local success justifies global expansion | not supported | bandits support adaptation, not automatic expansion | reject |
| boundary-risk-constrained expansion | analogy only / not directly supported | classical MAB lacks UDAM's boundary term | keep UDAM-specific |
| timer-derived anchor-loss structure | analogy only | bandit theory does not contain `tau = K + U + R` | keep UDAM-specific |
| literature proves UDAM as a whole | not supported | only the probe/action-feedback layer is supported | reject |

## Recommended repository wording

Use:

```text
Multi-armed bandit theory supports UDAM's small-probe layer in a limited sense: an action can both produce payoff and reveal information for later action selection.
```

Use:

```text
Exploration-exploitation literature supports treating probes as value tradeoffs, not as automatically useful actions.
```

Use:

```text
Bandit theory supports feedback-based adaptation, but UDAM's anchor-loss framing and boundary-risk-constrained expansion remain UDAM-specific.
```

Avoid:

```text
Any small action is useful.
```

Avoid:

```text
UDAM is a bandit algorithm.
```

Avoid:

```text
A successful probe proves that expansion or doubling is optimal.
```

## Impact on current theory

No major correction is required.

Bandit theory strengthens the existing UDAM wording around:

```text
small probes as action-with-feedback
exploration-exploitation tradeoff
adaptive action selection
learning through bounded action
```

The main cautions are:

```text
small != useful
feedback-producing != favorable
local probe success != global expansion permission
bandit support != full synthesis proof
```

## Next literature topic

The next check should be:

```text
exponential search / doubling strategies
```

Reason:

Bandit theory supports the probe-as-action-feedback layer. Exponential search is closer to the expansion factor layer:

```text
s_{i+1} = r_i s_i
```

and to the warning:

```text
doubling is a heuristic or domain-specific strategy, not always optimal
```
