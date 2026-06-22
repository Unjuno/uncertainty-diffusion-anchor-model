# SDD AGENTS.md

This file is the local agent guide for the SDD prototype under `docs/sdd/`.

For the general repository rules, also read the root `AGENTS.md`. For the implementation scope of this prototype, this file and `AGENTS.sdd.md` are authoritative.

## Read first

1. `docs/sdd/README.md`
2. `docs/sdd/spec.md`
3. `docs/sdd/tasks.md`
4. `docs/sdd/acceptance.md`
5. `docs/sdd/glossary.md`
6. `docs/sdd/decisions.md`
7. `docs/sdd/grill.md`

## Implementation rule

Implement only the v0.1 prototype described in `docs/sdd/spec.md`.

If a feature is not in the spec, do not implement it.

## MVP priority

```text
1. UI is usable
2. Generation loop runs
3. Noise Brush affects the next generation request
4. Snapshots can be saved and restored
5. Finish from Snapshot works
6. Model quality can be improved later
```

## Required implementation order

Use `docs/sdd/tasks.md` as the task order.

Start with the Mock backend. Do not start with TinySD model integration.

## Non-negotiable behavior

- Human Layer is independent from Generated Image.
- Generation updates must not change Human Layer.
- Noise Brush applies to Generated Image only.
- Auto Mode must be stoppable.
- Snapshot restore must preserve the original Snapshot.
- Finish from Snapshot must use the selected Snapshot as the base image.
- Generation errors must be visible in the UI.
- Generation errors must not make the app unusable.

## When the spec is unclear

Stop implementation and propose a spec update.

Use `docs/sdd/grill.md` to check whether the change belongs in v0.1.
