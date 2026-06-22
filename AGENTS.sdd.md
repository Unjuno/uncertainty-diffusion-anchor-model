# AGENTS.sdd.md

This file gives implementation guidance for agents working on the SDD prototype under `docs/sdd/`.

The root `AGENTS.md` remains the guidance for the existing UDAM theory repository. This file is the maintainer-requested implementation scope for the interactive prototype.

## Scope

Implement only the v0.1 prototype defined in:

- `docs/sdd/spec.md`
- `docs/sdd/tasks.md`
- `docs/sdd/acceptance.md`
- `docs/sdd/glossary.md`
- `docs/sdd/decisions.md`
- `docs/sdd/grill.md`

## Product target

Build an interactive prototype where a user can:

```text
enter a Prompt
→ draw on Human Layer
→ generate or loop Generated Image updates
→ paint Noise Brush regions
→ save intermediate Snapshots
→ restore a Snapshot
→ Finish from a selected Snapshot
```

This is not a one-shot prompt-to-final-image app.

## Implementation order

Follow `docs/sdd/tasks.md` in order.

Do not skip directly to model quality work.

Required order:

1. Project scaffold
2. Static UI
3. App state model
4. Human Layer canvas
5. Mock generation backend
6. Basic generation flow
7. Noise Brush mask
8. Step / Auto / Pause loop
9. Snapshot save / restore
10. Finish from Snapshot
11. TinySD backend hook
12. Documentation and demo path

## Hard rules

1. Do not implement features not listed in `docs/sdd/spec.md`.
2. Start with Mock backend before TinySD or any real model backend.
3. Keep Human Layer separate from Generated Image.
4. Generation updates must not modify Human Layer.
5. Noise Brush applies only to Generated Image.
6. Noise Brush creates a mask for re-generation; it is not a normal eraser.
7. Auto Mode must always be stoppable with Pause.
8. Protect against stale generation responses overwriting newer state.
9. Snapshot restore must not delete the original Snapshot.
10. Finish from Snapshot must use the selected Snapshot as the base image.

## v0.1 exclusions

Do not implement the following in v0.1:

- Diagram structure recognition
- Mermaid / UML / SVG conversion
- ControlNet
- Complex semantic layers
- Collaborative editing
- Authentication
- Cloud deployment
- Persistent server storage
- Full latent-state snapshot restart
- Production-quality model optimization

## Completion rule

A task is complete only when the matching conditions in `docs/sdd/acceptance.md` pass.

If the spec is unclear, do not decide silently in code. Propose a spec update using `docs/sdd/grill.md` first.
