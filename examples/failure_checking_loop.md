# Failure Example: Checking Loop

## Pattern

An observation was useful at first, but later repetitions no longer change belief or action enough to justify cost.

Formal failure condition:

```text
MOV_i <= 0
```

## Situation

The agent is uncertain about a project state.

Relevant hidden state:

```text
S = current project state
```

The agent opens the task list once.

This first observation is useful.

It reveals:

```text
there are three tasks
one task is clearly first
```

At this point, the next action is already clear.

But instead of acting, the agent keeps checking the list, rereading the same items, and refreshing the same information.

## Why this fails

The first observation had value.

Later checks do not change the next action.

```text
same information -> same action -> extra cost
```

The checking loop gives a feeling of contact with the project, but does not create a new valid re-anchor.

## UDAM correction

After the first useful observation, ask:

```text
Would another observation change the next action?
```

If no:

```text
act on the current anchor
```

If yes:

```text
choose a different state-informative observation
```

## Practical rule

```text
First observation can be valuable.
Repeated observation requires marginal value.
```
