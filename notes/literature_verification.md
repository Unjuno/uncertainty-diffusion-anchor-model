# Literature Verification Checklist

This note tracks literature links that should be verified before being treated as citations.

The goal is not to collect many references.

The goal is to check whether each UDAM claim is actually supported by nearby literature.

## Method

For each item, check:

```text
1. What UDAM claim is being supported?
2. What existing theory is nearby?
3. Does the source actually support the claim?
4. Is the connection direct, partial, or weak?
5. Should UDAM wording be corrected?
```

## Verification table

| UDAM claim | Nearby area | Status | Notes |
|---|---|---|---|
| Observation has value when it can improve action choice | value of information | verified: direct support | See `docs/22_literature_verification_value_blackwell.md`; keep cost and expected-decision-value wording |
| More informative observations can improve decisions | Blackwell informativeness | verified: partial support | See `docs/22_literature_verification_value_blackwell.md`; compatible but not identical to `P(y | S) != P(y)` |
| Choose observations by expected usefulness | Bayesian experimental design | verified: direct support | See `docs/23_literature_verification_bayesian_experimental_design.md`; supports utility-guided observation choice |
| Prior -> observation -> posterior -> action | Bayesian experimental design | verified: partial to direct support | Direct for prior-posterior updating; action mapping is supported when utility is decision-relevant but remains UDAM-specific in concrete form |
| Continue observing only while marginal value is positive | sequential analysis / stopping rules | verified: partial support | See `docs/24_literature_verification_sequential_analysis.md`; stopping-rule discipline is directly supported, but `MOV_i` is UDAM-specific notation |
| Repeated observation requires a stopping rule | sequential analysis / stopping rules | verified: direct support | Later checks are continue-or-stop decisions, not automatic extensions of the first observation |
| Small probes can balance learning and action | multi-armed bandits / exploration-exploitation | verified: direct / partial support | See `docs/25_literature_verification_multi_armed_bandits.md`; direct for action-with-feedback, partial for UDAM's practical post-anchor-loss probe framing |
| Exploration is useful but costly | multi-armed bandits / exploration-exploitation | verified: direct support | Regret formalizes that exploratory action can have opportunity cost |
| Geometric expansion can reduce search cost when scale is unknown | exponential search / doubling search | verified: direct / partial support | See `docs/26_literature_verification_exponential_search.md`; direct for ordered or spatial search, partial for UDAM practical expansion |
| Doubling is always optimal | exponential search / doubling search | not supported | Doubling is a useful default example in some search settings, not a universal rule |
| Robust rules matter when the offline optimum is unavailable | online algorithms | verified: direct / partial support | See `docs/27_literature_verification_online_algorithms.md`; direct for offline optimum unavailable, partial for UDAM-specific expansion rules |
| Repeated small cost versus one large decision | ski-rental-type tradeoffs | verified: direct / analogy support | Direct for rent-or-buy under unknown horizon; analogy for broader UDAM applications |
| If-result-then-action mapping improves usability | implementation intentions | verified: direct support | See `docs/28_literature_verification_implementation_intentions.md`; direct support for cue-response execution mapping |
| Concrete cue and feasible response improve execution | implementation intentions | verified: direct support | Supports observable if-part and actionable then-part; does not prove observation validity or action value |
| Action can be chosen partly to gain information | active inference / epistemic value | verified: direct / partial support | See `docs/29_literature_verification_active_inference.md`; direct support for epistemic action, partial support for UDAM's `I(a)` term |
| Epistemic value makes action automatically favorable | active inference / epistemic value | not supported | Information-seeking still needs UDAM's value, cost, and boundary-risk checks |
| Small action after collapse can matter | behavioral activation | verified: partial support | See `docs/30_literature_verification_behavioral_activation.md`; partial support for structured small action after avoidance-like collapse; not a clinical claim |
| Avoidance can maintain collapse-like states | behavioral activation | verified: direct / partial support | Direct in BA context; partial for UDAM because not all inaction is avoidance |
| Small successful steps can justify gradual expansion | shaping / successive approximations | to verify | next priority; be careful outside behavioral context |

## Verified notes

Current verified notes:

- `docs/22_literature_verification_value_blackwell.md`
- `docs/23_literature_verification_bayesian_experimental_design.md`
- `docs/24_literature_verification_sequential_analysis.md`
- `docs/25_literature_verification_multi_armed_bandits.md`
- `docs/26_literature_verification_exponential_search.md`
- `docs/27_literature_verification_online_algorithms.md`
- `docs/28_literature_verification_implementation_intentions.md`
- `docs/29_literature_verification_active_inference.md`
- `docs/30_literature_verification_behavioral_activation.md`

Key result:

```text
value of information -> direct support for OV > 0 style observation value
Blackwell informativeness -> partial support for state-informative observation and conditional action, but not identical to UDAM's local condition
Bayesian experimental design -> direct support for utility-guided observation choice and prior-posterior updating, but not proof of UDAM's timer-derived synthesis
sequential analysis / stopping rules -> direct support for treating repeated observation as a continue-or-stop problem; partial support for UDAM's MOV_i notation
multi-armed bandits -> direct support for action-with-feedback and exploration-exploitation tradeoff; partial support for UDAM's practical small-probe framing
exponential search -> direct support for geometric expansion under unknown scale in structured search domains; partial support for UDAM expansion; no support for universal doubling
online algorithms -> direct support for unavailable offline optimum and robust-rule framing; partial support for UDAM-specific expansion rules unless a formal cost model is defined
implementation intentions -> direct support for if-result-then-action execution mapping; not support for observation validity or positive action value
active inference -> direct support for epistemic action and information-seeking policy selection; partial support for UDAM's practical I(a) term
behavioral activation -> partial support for structured small action after collapse-like avoidance; not support for UDAM as therapy or arbitrary small action
```

## Current caution

Do not write:

```text
UDAM is proven by these literatures.
```

Prefer:

```text
UDAM is consistent with several existing decision-theoretic and cognitive frameworks, but each connection should be verified separately.
```

Additional cautions:

```text
MOV_i <= 0 means the current observation mode should stop or change. It does not imply that all possible future observations are worthless.
small != useful
feedback-producing != favorable
local probe success != global expansion permission
unknown scale != unknown state
doubling is not always optimal
robust != optimal
competitive ratio != expected utility
execution support != value support
if-then planning does not make an observation valid
I(a) != expected free energy unless formally mapped
epistemic value != automatic favorability
UDAM is not behavioral activation therapy
avoidance != all inaction
```

## Priority

First priority:

```text
value of information: verified first pass
Blackwell informativeness: verified first pass
Bayesian experimental design: verified first pass
sequential analysis / stopping rules: verified first pass
multi-armed bandits / exploration-exploitation: verified first pass
exponential search / doubling strategies: verified first pass
online algorithms / robust decision rules: verified first pass
implementation intentions / if-then planning: verified first pass
active inference / epistemic value: verified first pass
behavioral activation: verified first pass
```

Second priority:

```text
shaping / successive approximations
```

Third priority:

```text
ski-rental-type tradeoffs: verified as direct/analogy under online algorithms
```

## Status

This file is a checklist, not a bibliography.

Verified citations should later be moved into:

```text
notes/research_notes.md
docs/08_related_work.md
docs/17_literature_support_map.md
```
