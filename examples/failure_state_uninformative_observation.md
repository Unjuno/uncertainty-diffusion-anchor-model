# Failure Example: State-Uninformative Observation

## Pattern

An action feels like a check, but it does not return information about the relevant hidden state.

Formal failure condition:

```text
P(y | S) = P(y)
```

Therefore:

```text
P(S | y) = P(S)
```

## Situation

The agent wants to know whether they can currently solve a set of problems.

Relevant hidden state:

```text
S = current problem-solving ability
```

Instead of solving one problem, the agent reorganizes notes, changes folders, rewrites headings, and reviews the plan layout.

Observation returned:

```text
y = notes look more organized
```

## Why this fails

The observation may say something about organization, but it does not directly test the relevant state.

```text
organized notes != demonstrated problem-solving ability
```

The action may feel productive, but it is not a valid re-anchor for the target state.

## UDAM correction

Choose a state-informative observation.

```text
solve one representative problem
```

Possible results:

```text
solved correctly -> proceed to a slightly larger set
partially solved -> identify missing step
not solved -> review the smallest prerequisite
```

## Practical rule

```text
Do not ask whether the action feels productive.
Ask whether the observation changes belief about the relevant state.
```
