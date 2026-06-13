# 20 Five-Stage Development Roadmap

This document defines the next development phase after the core theory has become stable.

The goal is no longer to keep adding new concepts.

The goal is to improve:

```text
support
clarity
failure boundaries
reader confidence
explanatory force
```

## Current status

UDAM is currently best described as:

```text
A timer-derived practical synthesis of re-anchoring after anchor loss.
```

The core claim is:

```text
partial uncertainty does not imply total invalidation
```

or:

```text
anchor loss does not imply future anchor invalidation
```

The core timer decomposition remains:

```text
τ = K + U + R
```

## The five stages

The next work should proceed through five stages.

Japanese documentation already exists, but it should now be treated as a later synchronization layer. The English theory should stabilize first, because terminology and structure may still change.

```text
1. failure boundaries
2. literature verification
3. visual explanation
4. project-note consolidation
5. Japanese explanation sync
```

## Stage 1: Failure boundaries

Purpose:

```text
make clear where UDAM applies and where it fails
```

Current status:

```text
mostly complete, still expandable
```

Existing files:

- `docs/06_failure_cases.md`
- `docs/21_failure_decision_tree.md`
- `theory/counterexamples.md`
- `examples/failure_state_uninformative_observation.md`
- `examples/failure_checking_loop.md`
- `examples/failure_over_expansion.md`
- `examples/failure_local_to_global_judgment.md`
- `assets/diagrams/failure_decision_tree.mmd`

Japanese mirrors already exist but should not drive new changes yet:

- `docs/ja/03_failure_cases.md`
- `docs/ja/05_failure_examples.md`

Core failure conditions:

```text
P(y | S) = P(y)
a(y) = a_0
MOV_i <= 0
B_expand(r_i) + I_expand(r_i) <= C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
one local result -> total judgment
```

Next work:

- add more domain examples in English first;
- distinguish failure of UDAM from missed application of UDAM;
- connect each failure case to a proposition;
- only later sync stable changes into Japanese.

## Stage 2: Literature verification

Purpose:

```text
separate real support from loose analogy
```

Current status:

```text
verification checklist exists, actual verification mostly pending
```

Existing files:

- `notes/literature_verification.md`
- `docs/08_related_work.md`
- `docs/17_literature_support_map.md`
- `notes/evidence_hierarchy.md`

The goal is not to maximize the number of references.

The goal is to answer:

```text
which UDAM claim is supported by which existing theory, and how directly?
```

Verification categories:

```text
direct support
partial support
analogy only
not supported
requires wording correction
```

Priority topics:

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

Next work:

- verify one topic at a time;
- use primary or high-quality sources;
- add corrections when a literature link is weaker than expected;
- avoid claiming that UDAM is proven by the literature.

## Stage 3: Visual explanation

Purpose:

```text
make the model understandable without reading every formal document
```

Current status:

```text
Mermaid diagrams exist, but rendered figures are still pending
```

Existing files:

- `assets/diagrams/timer_decomposition.mmd`
- `assets/diagrams/timer_relative_dilution.mmd`
- `assets/diagrams/uncertainty_diffusion_cycle.mmd`
- `assets/diagrams/action_value_flow.mmd`
- `assets/diagrams/failure_taxonomy.mmd`
- `assets/diagrams/failure_decision_tree.mmd`
- `assets/diagrams/observability_value_flow.mmd`
- `assets/diagrams/adaptive_expansion_factor.mmd`
- `assets/diagrams/full_udam_flow.mmd`
- `assets/diagrams/positioning_map.mmd`

Next work:

- add short English Markdown pages explaining each diagram;
- make `full_udam_flow.mmd` the main orientation diagram;
- render diagrams into image files later if useful;
- add Japanese captions only after English diagram explanations stabilize.

## Stage 4: Project-note consolidation

Purpose:

```text
make the repository feel coherent as a hobby theory project, not necessarily as a formal paper
```

Current status:

```text
paper outline exists but should not dominate the project
```

Existing files:

- `drafts/paper_outline.md`
- `drafts/blog_post_jp.md`
- `drafts/short_manifesto.md`

Preferred framing:

```text
project note
concept note
theory note
```

not necessarily:

```text
academic paper
```

Next work:

- optionally add `project_note_outline.md`;
- write a short concept note version;
- keep the paper outline as optional, not central;
- prioritize readability and coherence over academic form.

## Stage 5: Japanese explanation sync

Purpose:

```text
synchronize Japanese explanations only after the English structure stabilizes
```

Current status:

```text
minimum viable Japanese layer exists, but further expansion should wait
```

Existing files:

- `docs/ja/README.md`
- `docs/ja/00_plain_explanation.md`
- `docs/ja/01_timer_model.md`
- `docs/ja/02_practical_protocol.md`
- `docs/ja/03_failure_cases.md`
- `docs/ja/04_positioning.md`
- `docs/ja/05_failure_examples.md`

Core Japanese expression:

```text
途中でわからなくなった部分があることと、これから確かめることが意味ないことは別。
```

Formal Japanese expression:

```text
過去のアンカー喪失は、未来の有効観測を無効化しない。
```

Next work later:

- sync stable English changes into Japanese;
- add Japanese examples for learning, work, relationship, and planning;
- add a Japanese glossary;
- add Japanese diagram descriptions;
- keep Japanese text as explanation, not literal translation.

## Evidence-strength ladder

Future writing should distinguish levels of support.

```text
Level 1: intuition from timer seed model
Level 2: internal formal consistency
Level 3: concrete examples
Level 4: failure cases and counterexamples
Level 5: nearby existing literature
Level 6: empirical testing or simulation, deferred
```

UDAM currently has stronger support at Levels 1-4.

Level 5 is partially mapped but not fully verified.

Level 6 is intentionally deferred.

## Practical next sequence

The immediate next sequence should be:

```text
1. continue Stage 1 only if new English failure boundaries are needed
2. begin Stage 2 literature verification one topic at a time
3. add Stage 3 diagram explanation pages
4. consolidate Stage 4 project-note materials
5. sync Japanese only after English changes stabilize
```

## Do not do now

Avoid spending effort on:

```text
heavy simulation
formal proof expansion
complex code
premature academic framing
claiming full originality
large Japanese expansion before English stabilization
```

These can wait or remain optional.

## Current guiding sentence

```text
The theory is stable enough to refine; the next work is support, clarity, and verification.
```

Japanese:

```text
理論の骨格は固まってきた。次にやるべきことは、根拠・説明・検証を強くすること。
```
