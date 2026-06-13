# Roadmap

## v0.1: Theory skeleton

Goal: Fix the minimal theory structure.

- [x] README
- [x] license notice
- [x] timer model
- [x] variables
- [x] assumptions
- [x] axioms
- [x] propositions
- [x] proofs
- [x] counterexamples

Status: complete as initial skeleton.

## v0.2: Applications

Goal: Add structured application examples.

- [x] learning recovery
- [x] work interruption recovery
- [x] health tracking
- [x] relationship uncertainty
- [x] life strategy after failure

Status: initial examples added. Further examples can be added later.

## v0.3: Related work

Goal: Map the model to existing fields without overclaiming novelty.

- [x] Bayesian filtering
- [x] Kalman filtering
- [x] POMDP / belief state
- [x] active inference
- [x] value of information
- [x] behavioral activation
- [x] cognitive anchoring

Status: initial related-work map added. Needs expansion and citations if developed into a paper.

## v0.4: Diagrams

Goal: Add conceptual diagrams.

- [x] uncertainty diffusion without anchors
- [x] lost interval and re-anchored interval
- [x] action value flow
- [x] failure case taxonomy

Status: Mermaid source diagrams added under `assets/diagrams/`. Rendered figures can be added later under `assets/figures/`.

## v0.5: Formal refinement

Goal: sharpen the mathematical status of the model.

- [ ] decide whether `P_t` is variance, covariance, entropy, or a general uncertainty functional
- [ ] define conditions under which `Q > 0`
- [ ] formalize diminishing information value for repeated checking
- [ ] add notation for observation update after re-anchoring
- [ ] separate cognitive uncertainty from physical state change

## v1.0: Stable theory note

Goal: Publish a coherent theory note with definitions, propositions, proofs, examples, and limitations.

Remaining work:

- refine definitions;
- strengthen proofs;
- add rendered figures;
- add a formal novelty statement;
- expand related work;
- add Japanese and English paper-style drafts.
