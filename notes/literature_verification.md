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
| Small probes can balance learning and action | multi-armed bandits / exploration-exploitation | to verify | partial; next priority after sequential analysis |
| Action can be chosen partly to gain information | active inference / epistemic value | to verify | partial; UDAM is narrower |
| If-result-then-action mapping improves usability | implementation intentions | to verify | likely practical support |
| Small successful steps can justify gradual expansion | shaping / successive approximations | to verify | partial; be careful outside behavioral context |
| Geometric expansion can reduce search cost when scale is unknown | exponential search / doubling search | to verify | direct for ordered search, partial for UDAM applications |
| Robust rules matter when the offline optimum is unavailable | online algorithms | to verify | partial; needs careful framing |
| Repeated small cost versus one large decision | ski-rental-type tradeoffs | to verify | analogy only unless formalized |
| Small action after collapse can matter | behavioral activation | to verify | partial; avoid clinical overclaiming |

## Verified notes

Current verified notes:

- `docs/22_literature_verification_value_blackwell.md`
- `docs/23_literature_verification_bayesian_experimental_design.md`
- `docs/24_literature_verification_sequential_analysis.md`

Key result:

```text
value of information -> direct support for OV > 0 style observation value
Blackwell informativeness -> partial support for state-informative observation and conditional action, but not identical to UDAM's local condition
Bayesian experimental design -> direct support for utility-guided observation choice and prior-posterior updating, but not proof of UDAM's timer-derived synthesis
sequential analysis / stopping rules -> direct support for treating repeated observation as a continue-or-stop problem; partial support for UDAM's MOV_i notation
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

Additional caution:

```text
MOV_i <= 0 means the current observation mode should stop or change. It does not imply that all possible future observations are worthless.
```

## Priority

First priority:

```text
value of information: verified first pass
Blackwell informativeness: verified first pass
Bayesian experimental design: verified first pass
sequential analysis / stopping rules: verified first pass
```

Second priority:

```text
multi-armed bandits
exponential search
online algorithms
implementation intentions
```

Third priority:

```text
active inference
behavioral activation
shaping / successive approximations
ski-rental-type tradeoffs
```

## Status

This file is a checklist, not a bibliography.

Verified citations should later be moved into:

```text
notes/research_notes.md
docs/08_related_work.md
docs/17_literature_support_map.md
```
