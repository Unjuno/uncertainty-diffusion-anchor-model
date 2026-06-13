# 44 Contraction Rule Decision

This document records a first-pass decision about whether UDAM needs a separate contraction rule in addition to the existing expansion rule.

The purpose is not to add a new theory layer.

The purpose is to prevent the expansion rule from being misread as one-way growth.

## Decision status

Status:

```text
first-pass decision recorded
```

Decision:

```text
Do not add a full new contraction theory layer now.
Add a reader-facing clarification: failed or unfavorable expansion should reduce scope, stop expansion, or change observation mode according to the existing value and boundary-risk conditions.
```

Reason:

```text
The current model already contains enough machinery to reject expansion:
V(a) <= 0
OV <= 0
MOV_i <= 0
B_expand(r_i) + I_expand(r_i) <= C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
```

A separate contraction theory may be useful later, but adding it now would risk unnecessary theory expansion.

## Existing expansion rule

UDAM's expansion layer uses:

```text
s_{i+1} = r_i s_i
```

with the boundary-risk-constrained condition:

```text
B_expand(r_i) + I_expand(r_i) > C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
```

This already implies a negative decision boundary:

```text
B_expand(r_i) + I_expand(r_i) <= C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
```

Interpretation:

```text
Do not expand at that factor.
```

It does not yet require a new formal contraction equation.

## Clarification to preserve

Use this wording when needed:

```text
Expansion is permitted only when the selected expansion factor remains favorable after observation cost, boundary risk, and correction cost.
If the inequality fails, UDAM supports reducing scope, observing sooner, stopping expansion, or switching observation mode rather than expanding automatically.
```

This is a clarification of the existing rule, not a new formal claim.

## What contraction means here

In the current repository phase, contraction means one of four practical responses:

| Response | Meaning | Existing source layer |
|---|---|---|
| reduce `r_i` | choose a smaller expansion factor | `docs/18_adaptive_expansion_factor.md`, `docs/21_failure_decision_tree.md` |
| reduce `s_i` | return to a smaller action or observation scope | practical layer |
| observe sooner | shorten the interval before rechecking boundary risk | observation cadence / expansion layer |
| stop or switch | stop current checking or expansion mode | `MOV_i <= 0`, failure decision tree |

This is enough for the current public repository.

## What not to add yet

Do not introduce a new canonical equation such as:

```text
s_{i+1} = c_i s_i
```

or:

```text
c_i < 1
```

unless the maintainer explicitly requests a formal contraction layer.

Reason:

```text
A new contraction symbol would create another notation burden without solving a current contradiction.
```

## Guardrails

Preserve:

```text
local success != global expansion permission
small != useful
state-informative != favorable
```

Add this practical clarification where relevant:

```text
failed expansion test means reduce, pause, or re-observe; it does not mean the model failed.
```

Avoid:

```text
Expansion is the natural next step after any success.
Contraction requires a separate new UDAM axiom.
Every failed expansion proves the original local action was invalid.
```

## Recommended routing

If future edits mention contraction:

| Claim type | Route to |
|---|---|
| Practical contraction after failed expansion | `docs/18_adaptive_expansion_factor.md`, `docs/21_failure_decision_tree.md` |
| Formal contraction rule | `theory/` first |
| Visual contraction explanation | `assets/diagrams/` first, then `assets/figures/` |
| Changelog entry | only if a formal contraction layer is added |

## Result

Current result:

```text
No separate contraction rule is required for v1.0 stabilization.
```

Recommended future action:

```text
Add a short clarification to expansion-facing documents only if readers misread expansion as one-way growth.
Do not add a new contraction equation during stabilization.
```
