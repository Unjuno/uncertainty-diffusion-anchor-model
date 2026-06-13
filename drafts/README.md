# Drafts

This directory contains public-facing and paper-facing drafts derived from UDAM.

## Source-of-truth disclaimer

Drafts are downstream presentations of UDAM.

They are not the source of formal claims, literature support claims, visual policy, simulation status, or repository policy.

If a draft conflicts with `docs/`, `theory/`, `notes/`, or `simulations/`, the source-of-truth files override the draft.

Recommended rule:

```text
drafts present the model
drafts do not define the model
```

Formal claims should route to:

```text
theory/
docs/10_formal_refinement.md
```

Literature claims should route to:

```text
docs/17_literature_support_map.md
notes/literature_verification.md
docs/22 through docs/31
```

Simulation claims should route to:

```text
docs/39_simulation_sanity_checks.md
simulations/
```

Japanese explanations should route to:

```text
docs/ja/README.md
```

Current Japanese drafts are downstream public-facing drafts, not synchronized source-of-truth Japanese documentation.

## Files

| File | Role |
|---|---|
| `paper_outline.md` | structured academic paper outline |
| `blog_post_jp.md` | Japanese public-facing blog draft |
| `short_manifesto.md` | short statement of the core idea |

## Current message hierarchy

### Short version

```text
partial uncertainty does not imply total invalidation
```

### Practical version

```text
partial uncertainty → re-anchor if the next action has positive value
```

### Formal version

```text
τ = K + U + R
P_{t+Δt} = P_t + QΔt
V(a) = I(a) + B(a) - C(a)
```

## Scope constraints

Drafts should preserve the current core boundaries:

```text
fixed target, uncertain position
```

not:

```text
uncertain target, uncertain position
```

and:

```text
actionable uncertainty only
```

not:

```text
uncontrollable external uncertainty treated as actionable
```

## Public wording rules

Public-facing drafts should avoid overclaiming.

Do not claim:

- action is always good;
- reality is deterministic;
- re-anchoring always reduces absolute uncertainty;
- the external world always worsens during inaction;
- high-stakes examples require vivid details;
- UDAM is empirically validated;
- UDAM is proven by toy simulation;
- UDAM is a replacement for existing decision theory.

Use:

- small informative action;
- belief uncertainty;
- fixed target;
- uncertain position;
- relative influence;
- controllability boundary;
- non-operational high-stakes example;
- toy demonstration rather than empirical validation.
