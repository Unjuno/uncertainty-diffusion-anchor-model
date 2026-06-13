# Example: Work Interruption Recovery

## Situation

A project is interrupted. After time passes, the agent no longer knows exactly what is done, what is broken, or what should happen next.

## Lost anchor

The lost anchor is project state.

## State variable

The latent state is the actual project condition:

```text
S_t = current project state
```

This may include files, tasks, dependencies, blockers, and external requirements.

## Belief uncertainty

The agent is uncertain about the current project state.

```text
P_{project,t} = Var(S_t | D_t)
```

## Possible state dynamics

The project itself may change during the interruption:

- dependencies update;
- requirements shift;
- collaborators make changes;
- previous assumptions become stale.

## Belief dynamics

Even if the project has not changed, the agent's uncertainty can increase because memory and context decay.

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
