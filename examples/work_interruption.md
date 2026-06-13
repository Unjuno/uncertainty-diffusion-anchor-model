# Example: Work Interruption Recovery

## Situation

A project is interrupted. After time passes, the agent no longer knows exactly what is done, what is broken, or what should happen next.

## Lost anchor

The lost anchor is project state.

## Uncertainty diffusion

Without inspection, uncertainty grows about:

- completed tasks;
- blocked tasks;
- external dependencies;
- outdated assumptions;
- next action.

```text
P_{project,t+Δt} = P_{project,t} + Q_project Δt
```

## Re-anchoring action

Inspect the task list, commit log, notes, or current working tree for 10 minutes.

## Informational value

The action maps the current project state.

```text
I(a) > 0
```

## Intervention value

If the agent closes one tiny task, the action also improves the state.

```text
B(a) > 0
```

## Failure case

Rewriting the entire plan before inspecting the actual state may be noise-producing activity.

The first re-anchor should contact the real project state.
