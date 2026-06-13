# 26 Literature Verification: Exponential Search and Doubling Strategies

This document continues Stage 2 of the five-stage refinement roadmap.

It checks exponential search, doubling search, and online search literature against UDAM claims about expansion after favorable probes.

The goal is not to prove UDAM from exponential search.

The goal is to classify which UDAM components are directly supported, partially supported, analogy-only, unsupported, or in need of wording correction.

## Sources checked

Reference candidates:

- Jon Bentley and Andrew Chi-Chih Yao, "An Almost Optimal Algorithm for Unbounded Searching," Information Processing Letters, 1976.
- Anatole Beck and Donald J. Newman, "Yet More on the Linear Search Problem," Israel Journal of Mathematics, 1970.
- Shmuel Gal, *Search Games*, 1980.
- F. Thomas Bruss and James B. Robertson, "A Survey of the Linear Search Problem," The Mathematical Scientist, 1988.
- Erik D. Demaine, Sandor P. Fekete, and Shmuel Gal, "Online Searching with Turn Cost," Theoretical Computer Science, 2006; arXiv:cs/0406045.
- Spyros Angelopoulos, Christoph Duerr, and Shendan Jin, "Best-of-Two-Worlds Analysis of Online Search," arXiv:1810.08109.
- Nikhil Bansal, John Kuszmaul, and William Kuszmaul, "A Nearly Tight Lower Bound for the d-Dimensional Cow-Path Problem," arXiv:2209.08427.

Core literature idea:

```text
when a target scale or position is unknown, geometric expansion can locate a containing interval or hidden target with bounded overhead
```

This is close to the UDAM expansion pattern:

```text
small valid probe -> favorable result -> expand scope geometrically or adaptively
```

But the match is limited.

Exponential search usually assumes an ordered domain, monotonic condition, or spatial search problem. UDAM concerns practical expansion after anchor loss, where monotonicity, safety, and boundary risks may fail.

## Minimal notation

| Symbol | Meaning in this note | Unit | Definition | Domain / assumption | Type |
|---|---|---:|---|---|---|
| `i` | expansion step | count | current expansion index | integer `i >= 0` | scalar |
| `s_i` | current search or action scope | domain unit | magnitude of tested scope at step `i` | positive | scalar |
| `r_i` | expansion factor | dimensionless | `s_{i+1} / s_i` | usually `r_i > 1` for expansion | scalar |
| `d` | unknown target scale | domain unit | distance, index, or minimum sufficient scope | positive | scalar |
| `C_search` | search cost | utility or domain unit | cost accumulated by probing scopes | non-negative | scalar |
| `OPT` | offline optimal cost | utility or domain unit | cost if target location or scale were known | positive | scalar |
| `rho` | competitive ratio | dimensionless | `rho = C_search / OPT` | `rho >= 1` | scalar |
| `P_boundary(i)` | boundary-crossing probability | probability | probability expansion at step `i` crosses adverse boundary | `[0,1]` | scalar |
| `C_boundary` | boundary cost | utility unit | cost if adverse boundary is crossed | non-negative | scalar |
| `B_expand(r_i)` | benefit of expansion | utility unit | expected benefit from testing larger scope | criterion-dependent | scalar |
| `I_expand(r_i)` | information value of expansion | utility unit | information gained by larger-scope test | criterion-dependent | scalar |
| `C_obs(r_i)` | observation cost of expansion | utility unit | cost of observing/testing larger scope | non-negative | scalar |
| `C_correct(r_i)` | correction cost | utility unit | expected cost of rollback or correction | non-negative | scalar |

Dimension check:

```text
B_expand(r_i) + I_expand(r_i) - C_obs(r_i) - P_boundary(i) C_boundary - C_correct(r_i) = utility unit
```

Therefore UDAM's boundary-risk-constrained expansion inequality is dimensionally valid only if all value and cost terms are expressed on the same utility scale.

## Literature pattern

Exponential search over an unbounded ordered list usually follows this structure:

```text
test 1, 2, 4, 8, ... until the target is bracketed
then search inside the bracket
```

Cow-path or linear search problems use related geometric expansion when the target distance and direction are unknown.

The shared idea is:

```text
unknown scale -> avoid fixed large guess -> expand geometrically to control worst-case overhead
```

This supports a limited version of UDAM's expansion factor layer.

But UDAM expansion is not merely search over an ordered list. It may involve practical action, risk, irreversibility, or non-monotonic feedback.

## UDAM claim 1: Geometric expansion is useful when scale is unknown

UDAM statement:

```text
when useful scale is unknown, the agent can expand scope geometrically after successful probes
```

Related UDAM expression:

```text
s_{i+1} = r_i s_i
```

Literature fit:

```text
direct support in ordered or spatial search settings
partial support for practical UDAM expansion
```

Reason:

Exponential search directly supports geometric expansion when searching over an ordered, unbounded, or scale-unknown domain. It is useful because it avoids committing to a large fixed scale before the target range is known.

This supports UDAM's use of expansion factors as a practical scale-discovery heuristic.

However, UDAM's expansion after anchor loss may not satisfy the assumptions of ordered search. A larger action may change the system, cross a boundary, or invalidate feedback.

Recommended wording:

```text
Exponential search supports geometric expansion under unknown scale when the domain has suitable search structure. UDAM uses this as a practical analogy for bounded expansion after favorable probes.
```

Avoid:

```text
Geometric expansion is always optimal.
```

## UDAM claim 2: Doubling can be a reasonable default but not a universal optimum

UDAM statement:

```text
1 -> 2 -> 4 -> 8
```

Literature fit:

```text
partial support
```

Reason:

Doubling is a standard geometric strategy in exponential search and linear search. It often provides bounded overhead when the relevant scale is unknown.

But this does not mean that doubling is universally optimal. Different problem classes, turn costs, prior information, randomized strategies, safety constraints, and performance criteria can favor other expansion schedules.

Recommended wording:

```text
Doubling is a simple geometric expansion heuristic supported in some search settings. It should be treated as a default example, not as a universal UDAM rule.
```

Avoid:

```text
Doubling is always optimal.
```

## UDAM claim 3: Expansion must be constrained by boundary risk

UDAM statement:

```text
B_expand(r_i) + I_expand(r_i) > C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
```

Literature fit:

```text
analogy only / partial support from online search with costs
not directly supported by classical exponential search
```

Reason:

Online search literature supports comparing search strategies by incurred cost versus an offline benchmark. Some variants include turn costs or other additional costs.

This is compatible with UDAM's idea that expansion has costs beyond information gain.

However, classical exponential search does not include a UDAM-style adverse boundary term:

```text
P_boundary(i) * C_boundary
```

The boundary-risk-constrained inequality is therefore UDAM-specific.

Recommended wording:

```text
Exponential and online search literature support cost-aware expansion, but UDAM's boundary-risk term is a practical extension rather than a standard exponential-search component.
```

Avoid:

```text
Exponential search proves the boundary-risk expansion inequality.
```

## UDAM claim 4: Local success does not justify unbounded expansion

UDAM statement:

```text
local observation does not imply global conclusion
```

Literature fit:

```text
partial support
```

Reason:

Exponential search supports increasing scope after failing to bracket a target or after needing a larger range, but the expansion is still governed by a search rule and stopping condition.

It does not support the inference:

```text
one favorable local probe -> unlimited expansion is valid
```

This is consistent with UDAM's warning that local observations remain local unless the domain structure justifies extrapolation.

Recommended wording:

```text
Geometric expansion should be treated as controlled scope testing, not as global validation from a local success.
```

Avoid:

```text
A small success means the whole larger domain is safe.
```

## UDAM claim 5: Unknown scale differs from unknown state

UDAM clarification:

```text
unknown scale != unknown state
```

Literature fit:

```text
requires wording correction
```

Reason:

Exponential search is strongest when the uncertainty is about scale, index, distance, or bracketing a threshold in a structured domain.

UDAM often handles uncertainty about state, actionability, validity, cost, and boundary risk. These are not automatically reducible to a one-dimensional search scale.

Recommended wording:

```text
Use exponential search only for the scale-expansion layer. Do not use it as support for all forms of uncertainty reduction in UDAM.
```

Avoid:

```text
All uncertainty can be handled by doubling.
```

## UDAM claim 6: Exponential search proves UDAM

UDAM statement:

```text
not claimed
```

Literature fit:

```text
not supported
```

Reason:

Exponential search supports a search strategy under unknown scale. It does not provide UDAM's timer seed model:

```text
tau = K + U + R
```

It also does not directly prove:

```text
anchor loss does not imply future anchor invalidation
```

Correct positioning:

```text
Exponential search supports UDAM's scale-expansion analogy, while the anchor-loss synthesis and boundary-risk-constrained expansion remain UDAM-specific.
```

Avoid:

```text
UDAM is exponential search.
```

## Verification table

| UDAM claim | Exponential-search support level | Reason | Correction |
|---|---:|---|---|
| geometric expansion under unknown scale | direct in ordered/spatial search; partial for UDAM | exponential search and cow-path search use geometric expansion under unknown scale or distance | restrict to scale layer |
| `s_{i+1} = r_i s_i` | direct as a geometric form; partial as a UDAM decision rule | supported as expansion schedule, not as universal policy | keep as flexible factor, not fixed doubling |
| doubling `1 -> 2 -> 4 -> 8` | partial support | common default in search settings | do not claim universal optimality |
| boundary-risk-constrained expansion | analogy only / partial | cost-aware search exists, but UDAM's boundary term is not standard | keep UDAM-specific |
| local success justifies global expansion | not supported | search rules expand under structure, not arbitrary success | reject |
| unknown scale equals unknown state | not supported | search scale and belief state are different | correct wording |
| timer-derived anchor-loss structure | analogy only | exponential search does not contain `tau = K + U + R` | keep UDAM-specific |
| literature proves UDAM as a whole | not supported | only expansion analogy is supported | reject |

## Recommended repository wording

Use:

```text
Exponential search supports UDAM's use of geometric expansion as a scale-discovery heuristic when the useful scale is unknown and the domain has suitable search structure.
```

Use:

```text
Doubling is a default example of geometric expansion, not a universal optimum.
```

Use:

```text
UDAM's boundary-risk-constrained expansion remains a practical extension beyond classical exponential search.
```

Avoid:

```text
Doubling is always optimal.
```

Avoid:

```text
A favorable local probe justifies global expansion.
```

Avoid:

```text
Exponential search proves UDAM.
```

## Impact on current theory

No major correction is required.

Exponential search strengthens the existing UDAM wording around:

```text
unknown useful scale
geometric scope expansion
bounded search effort
expansion as controlled testing
```

The main cautions are:

```text
geometric expansion requires domain structure
doubling is a heuristic, not a universal optimum
unknown scale is not the same as unknown state
boundary-risk-constrained expansion is UDAM-specific
component support != full synthesis proof
```

## Next literature topic

The next check should be:

```text
online algorithms / robust decision rules
```

Reason:

Exponential search verifies the expansion schedule analogy. Online algorithms and competitive analysis are closer to the question:

```text
what rule is reasonable when the offline optimum is unavailable?
```

This should help refine UDAM's positioning around robust practical rules under incomplete information.
