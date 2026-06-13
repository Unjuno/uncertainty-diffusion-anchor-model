# Changelog

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
