# Changelog

## 0.7.0 - Japanese documentation and visual support

Added a Japanese documentation layer inside the same repository, plus additional diagrams and a literature verification checklist.

Added:

- `docs/ja/README.md`
- `docs/ja/00_plain_explanation.md`
- `docs/ja/01_timer_model.md`
- `docs/ja/02_practical_protocol.md`
- `docs/ja/03_failure_cases.md`
- `docs/ja/04_positioning.md`
- `assets/diagrams/full_udam_flow.mmd`
- `assets/diagrams/positioning_map.mmd`
- `notes/literature_verification.md`

Removed:

- `docs/ja/00_chugaku_explanation.md`

Changed:

- README now links to Japanese documentation.
- `assets/diagrams/README.md` now lists the full flow and positioning map diagrams.
- ROADMAP now includes v0.13: Japanese documentation and visual support.

Core Japanese expression:

```text
過去のアンカー喪失は、未来の有効観測を無効化しない。
```

Plain version:

```text
途中でわからなくなった部分があることと、これから確かめることが意味ないことは別。
```

Status:

- Japanese documentation is maintained inside the same repository rather than as a separate repository.
- Literature references are tracked as verification candidates, not treated as confirmed citations yet.

## 0.6.0 - Positioning and novelty layer

Added a positioning layer to prevent overclaiming and clarify that UDAM is a practical synthesis rather than a replacement for existing decision theory.

Added:

- `docs/19_positioning_and_novelty.md`

Changed:

- README now states that UDAM is a timer-derived practical synthesis, not a wholly new mathematical theory of uncertainty.
- README now links to the positioning and novelty document.
- `notes/terminology.md` now defines practical synthesis, timer-derived formulation, and overclaim.
- ROADMAP now includes v0.12: Positioning and novelty.

Core positioning:

```text
UDAM is a timer-derived practical synthesis of re-anchoring after anchor loss.
```

Core distinctive claim:

```text
partial uncertainty does not imply total invalidation
τ = K + U + R
```

Status:

- Novelty positioning is now explicit. Future paper drafts should avoid overclaiming mathematical originality.

## 0.5.0 - Adaptive expansion factor and boundary-risk layer

Added a practical expansion layer for deciding how much to widen action or observation scope after favorable observations.

Added:

- `docs/18_adaptive_expansion_factor.md`
- `assets/diagrams/adaptive_expansion_factor.mmd`

Changed:

- README now links to the adaptive expansion factor document and includes `s_{i+1} = r_i s_i`.
- `theory/variables.md` now defines expansion variables including `s_i`, `r_i`, `P_boundary(i)`, `C_boundary`, and `C_correct(r_i)`.
- `theory/propositions.md` now includes Proposition 13: expansion factor is constrained by adverse boundary risk.
- `docs/05_propositions.md` now includes a readable version of Proposition 13.
- `theory/proofs.md` now includes a proof sketch and unit checks for the adaptive expansion condition.
- `docs/10_formal_refinement.md` now includes adaptive expansion factor as a formal refinement section.
- `docs/17_literature_support_map.md` now connects the model to exponential search, doubling search, online algorithms, and ski-rental-type tradeoffs.
- `docs/08_related_work.md` now includes adaptive expansion, exponential search, and online-rule connections.
- `docs/09_open_questions.md` now includes open questions about expansion factor, boundary-risk estimation, and fixed cadence versus geometric expansion.
- `drafts/paper_outline.md` now includes adaptive observation cadence and expansion factor as a paper section.

Core addition:

```text
s_{i+1} = r_i s_i
```

with boundary-risk constraint:

```text
B_expand(r_i) + I_expand(r_i) > C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
```

Status:

- Adaptive expansion factor is now integrated across docs, theory, proof sketches, diagrams, related work, open questions, and paper outline.

## 0.4.0 - Practical application playbooks and observation cadence

Added the practical layer for using UDAM in daily cases and for distinguishing first observation from repeated observation.

Added:

- concrete action sections to learning, work, relationship, budget, and life-strategy examples
- `examples/application_playbook_template.md`
- `docs/15_application_cautions.md`
- `docs/16_adaptive_observation_cadence.md`
- `docs/17_literature_support_map.md`

Changed:

- examples index now requires practical sections such as immediate action, observation result, next action map, and boundary.
- README now links to practical protocol, cautions, cadence, and literature support map.
- ROADMAP now includes concrete application playbooks and adaptive observation cadence.

Core addition:

```text
first valid observation -> often valuable
later observation -> useful only if it can change the next action
```

## 0.3.0 - Observability value and valid re-anchor layer

Added the observability and valid re-anchor layer.

Added:

- `theory/observability_value.md`
- `theory/observability_proofs.md`
- `theory/upside_uncertainty.md`
- `theory/downside_uncertainty.md`
- `theory/valid_reanchor_condition.md`
- `theory/conditional_action_switch.md`
- observability and conditional-switch diagrams

Changed:

- `theory/propositions.md` now includes observability value, fixed-target disbelief, valid re-anchor condition, and conditional action switch.
- `docs/05_propositions.md` now includes readable versions of those propositions.
- `docs/08_related_work.md` now connects conditional switching to the Monty Hall information structure.
- README now uses state-informative observation wording.

Core addition:

```text
P(y | S) != P(y)
a(y) != a_0
OV > 0
```

## 0.2.0 - Consistency pass and formal refinement notes

Organized the original chat content and added explicit consistency checks.

Added:

- `notes/chat_content_synthesis.md`
- `theory/consistency_review.md`
- `docs/10_formal_refinement.md`

Changed:

- README now links to chat synthesis, consistency review, and formal refinement.
- `docs/03_reanchoring.md` now distinguishes absolute uncertainty reduction from comparative containment against the no-action trajectory.
- `theory/variables.md` now clarifies the difference between `P_t` and `Q`.

Fixed:

- Corrected a timer-specific unit error: `QΔt` should have units `s²`, not `s`, when the state is elapsed time.

Open:

- Decide whether `P_t` remains variance/covariance or generalizes to an uncertainty functional `𝓤_t`.
- Formalize observation updates after re-anchoring.
- Separate belief uncertainty dynamics from physical state dynamics.

## 0.1.0 - Initial theory skeleton

Initial repository structure for the Uncertainty-Diffusion Anchor Model.

Added:

- README with core intuition and equations
- CC BY 4.0 license notice
- roadmap
- overview document
- timer model
- uncertainty diffusion document
- re-anchoring document
- action value document
- variable table
- assumptions
- axioms
- propositions
- initial proofs
- counterexamples and failure cases
- example applications
- terminology notes
- related work map

Status:

- This is a theory repository.
- Simulations are intentionally deferred.
- Priority is conceptual precision and falsifiable structure.
