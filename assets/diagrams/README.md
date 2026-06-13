# Diagrams

This directory contains conceptual diagrams for the Uncertainty-Diffusion Anchor Model.

The diagrams are written in Mermaid where possible so they can be edited as text.

## Files

- `timer_decomposition.mmd`: decomposition of elapsed time into known, unknown, and re-anchored intervals.
- `timer_relative_dilution.mmd`: relative uncertainty dilution in the timer model.
- `uncertainty_diffusion_cycle.mmd`: anchor loss, uncertainty diffusion, re-anchoring, and belief update.
- `action_value_flow.mmd`: decision rule for whether an action is a useful re-anchor.
- `failure_taxonomy.mmd`: cases where the model weakens or fails.

## Rendering

GitHub can render Mermaid diagrams inside Markdown, but raw `.mmd` files are kept here for editing and reuse.
