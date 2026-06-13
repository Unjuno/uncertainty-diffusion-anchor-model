# Failure Example: Local Observation Used as Global Judgment

## Pattern

A local observation is treated as if it justifies a global conclusion.

Failure pattern:

```text
one local result -> total self/world/project judgment
```

## Situation

The agent is uncertain about learning progress.

Relevant local state:

```text
S_local = ability to solve this kind of problem right now
```

The agent tries one problem and fails.

Observation:

```text
y = one failed problem
```

The agent concludes:

```text
I cannot learn this at all
```

## Why this fails

The observation is not meaningless.

It is a valid local observation.

But its scope is limited.

It updates:

```text
belief about this local task state
```

It does not automatically justify:

```text
global judgment about all future learning ability
```

The error is not observation itself.

The error is overextending the conclusion.

## UDAM correction

Use the observation at the correct scope.

Local conclusion:

```text
this problem type is currently difficult
```

Next useful observation:

```text
try the smallest prerequisite step
```

or:

```text
try one easier neighboring problem
```

## Practical rule

```text
Local observation updates local belief.
Global judgment requires broader evidence.
```
