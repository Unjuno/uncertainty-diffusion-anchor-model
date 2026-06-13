# 28 Literature Verification: Implementation Intentions and If-Then Planning

This document continues Stage 2 of the five-stage refinement roadmap.

It checks implementation intentions, if-then planning, and planning-prompt literature against UDAM claims about mapping observation results to concrete next actions.

The goal is not to prove UDAM from implementation-intention research.

The goal is to classify which UDAM components are directly supported, partially supported, analogy-only, unsupported, or in need of wording correction.

## Sources checked

Reference candidates:

- Peter M. Gollwitzer and Veronika Brandstaetter, "Implementation Intentions and Effective Goal Pursuit," Journal of Personality and Social Psychology, 1997.
- Peter M. Gollwitzer, "Implementation Intentions: Strong Effects of Simple Plans," American Psychologist, 1999.
- Peter M. Gollwitzer and Paschal Sheeran, "Implementation Intentions and Goal Achievement: A Meta-analysis of Effects and Processes," Advances in Experimental Social Psychology, 2006.
- Thomas L. Webb and Paschal Sheeran, "Does Changing Behavioral Intentions Engender Behavior Change? A Meta-analysis of the Experimental Evidence," Psychological Bulletin, 2006.
- Todd Rogers, Katherine L. Milkman, Leslie K. John, and Michael I. Norton, "Beyond Good Intentions: Prompting People to Make Plans Improves Follow-Through on Important Tasks," Behavioral Science & Policy, 2015.
- Keller, Gollwitzer, and Sheeran, "Changing Behavior Using the Model of Action Phases," in *The Handbook of Behavior Change*, 2020.

Core literature idea:

```text
an implementation intention links a future cue or situation to a specific response in an if-then plan
```

This is close to the UDAM practical action map:

```text
if result y occurs -> do action a(y)
```

But the match is limited.

Implementation-intention research supports action initiation and follow-through. It does not by itself verify whether the observation `y` is state-informative, whether the action is valuable, or whether boundary risk is acceptable.

## Minimal notation

| Symbol | Meaning in this note | Unit | Definition | Domain / assumption | Type |
|---|---|---:|---|---|---|
| `y` | observed result or cue | dimensionless | cue, situation, or observation result that triggers the mapped action | must be recognizable by the agent | event / observation |
| `a(y)` | mapped action | dimensionless | action planned in advance for cue `y` | feasible and specific | decision rule |
| `a_0` | default action | dimensionless | action taken without the cue-conditioned plan | may be inaction or generic response | decision variable |
| `G` | goal | dimensionless | higher-level goal being pursued | already endorsed or selected | goal state |
| `C_exec` | execution cost | utility unit | cost of performing the planned action | non-negative | scalar |
| `P_exec` | execution probability | probability | probability that the planned action is actually executed when cue appears | `[0,1]` | scalar |
| `OV` | observability value | utility unit | expected decision value of observation after cost | defined elsewhere in UDAM | scalar |
| `S` | UDAM-relevant state | dimensionless | state being inferred after anchor loss | domain-specific | random variable |

Dimension check:

```text
P_exec * expected action value - C_exec = utility unit
```

Implementation-intention research mostly concerns increasing `P_exec`, not proving that the selected action has positive expected value.

## Literature pattern

A standard implementation intention has the form:

```text
if situation X occurs, then I will perform response Y
```

The intended mechanism is practical and cognitive:

```text
specified cue -> easier cue detection -> reduced deliberation -> faster or more reliable action initiation
```

This directly supports UDAM's practical mapping:

```text
observation result -> mapped next action
```

But it does not replace UDAM's prior checks:

```text
state-informativeness
conditional action change
value versus cost
boundary risk
```

## UDAM claim 1: If-then mapping improves practical execution

UDAM statement:

```text
if result y occurs -> do action a(y)
```

Literature fit:

```text
direct support
```

Reason:

Implementation-intention research directly studies plans that specify a future cue and a concrete response. This supports UDAM's practical claim that an observation result should be paired with a concrete next action before the cue appears.

This is especially relevant after anchor loss, where vague intention can leave the agent stuck even after a valid observation.

Recommended wording:

```text
Implementation-intention research directly supports UDAM's if-result-then-action mapping as a practical execution aid.
```

Avoid:

```text
It is enough to know that some action should be taken.
```

## UDAM claim 2: If-then planning bridges belief update and action

UDAM statement:

```text
observe y -> update p(S | y) -> choose a(y)
```

Literature fit:

```text
partial support
```

Reason:

Implementation intentions support the execution side of the chain:

```text
when cue y appears -> perform response a(y)
```

They do not directly support the Bayesian update or the value-of-information component.

Therefore implementation intentions help turn a selected conditional action into an executable plan, but they do not prove that the observation or action is valid.

Recommended wording:

```text
Implementation intentions support the execution layer of UDAM's conditional action map, not the full observation-update-value chain.
```

Avoid:

```text
If-then planning makes any observation valid.
```

## UDAM claim 3: The cue must be concrete and recognizable

UDAM statement:

```text
observation result must be usable as a decision cue
```

Literature fit:

```text
direct support
```

Reason:

Implementation-intention research emphasizes specific future situations or cues. This supports the UDAM requirement that `y` should be concrete enough to trigger an action rather than remain an ambiguous feeling.

A vague cue such as:

```text
if I feel better somehow
```

is weaker than:

```text
if the timer reaches 10 minutes and the task is still moving
```

Recommended wording:

```text
The if-part of a UDAM action map should be a concrete, observable cue, not a vague mood or global judgment.
```

Avoid:

```text
If I feel ready, then I will act.
```

## UDAM claim 4: The response must be specific and feasible

UDAM statement:

```text
a(y) must be actionable
```

Literature fit:

```text
direct support
```

Reason:

If-then planning works by linking a specified situation to a specified response. This supports UDAM's failure boundary that an action map fails when the response is too abstract, too large, or not executable.

Recommended wording:

```text
The then-part of a UDAM action map should specify a concrete feasible action, not merely a goal or aspiration.
```

Avoid:

```text
Then I will improve the situation.
```

## UDAM claim 5: If-then plans do not determine whether the action is valuable

UDAM statement:

```text
state-informative != favorable
```

and:

```text
V(a) = I(a) + B(a) - C(a)
```

Literature fit:

```text
requires wording correction
```

Reason:

Implementation intentions can make a chosen action easier to execute. They do not establish that the action has positive expected value.

This is a critical boundary for UDAM.

An if-then plan can reliably execute a bad action.

Recommended wording:

```text
Implementation intentions improve execution of a selected response; they do not by themselves establish that the response is decision-theoretically favorable.
```

Avoid:

```text
If-then planning makes the action correct.
```

## UDAM claim 6: If-then planning proves UDAM

UDAM statement:

```text
not claimed
```

Literature fit:

```text
not supported
```

Reason:

Implementation-intention research supports the action-execution layer. It does not provide UDAM's timer seed model:

```text
tau = K + U + R
```

It also does not directly prove:

```text
anchor loss does not imply future anchor invalidation
```

Correct positioning:

```text
Implementation intentions support UDAM's practical if-result-then-action mapping, while the anchor-loss synthesis remains UDAM-specific.
```

Avoid:

```text
UDAM is an implementation-intention theory.
```

## Verification table

| UDAM claim | Implementation-intention support level | Reason | Correction |
|---|---:|---|---|
| if-result-then-action mapping improves usability | direct support | if-then planning directly links cue and response | keep |
| cue should be concrete and recognizable | direct support | implementation intentions rely on identifiable future situations | keep |
| response should be specific and feasible | direct support | implementation intentions specify concrete behavior | keep |
| conditional action can be executed more reliably | direct support | implementation intentions support follow-through | keep |
| belief update from observation | not supported | implementation intentions do not provide Bayesian update | keep in BED / VOI layer |
| action value is positive | not supported | execution support does not imply value support | reject |
| valid re-anchor condition | analogy only | cue-response planning is not state-informativeness | keep UDAM-specific |
| timer-derived anchor-loss structure | analogy only | implementation intentions do not contain `tau = K + U + R` | keep UDAM-specific |
| literature proves UDAM as a whole | not supported | only execution mapping is supported | reject |

## Recommended repository wording

Use:

```text
Implementation-intention research directly supports UDAM's if-result-then-action mapping as a practical execution device: a recognized cue should be linked to a concrete feasible response.
```

Use:

```text
If-then planning supports execution, not validity. UDAM must still check state-informativeness, action value, cost, and boundary risk.
```

Use:

```text
The if-part should be observable and the then-part should be actionable.
```

Avoid:

```text
If-then planning makes the observation valid.
```

Avoid:

```text
If-then planning makes the action correct.
```

Avoid:

```text
UDAM is implementation intentions.
```

## Impact on current theory

No major correction is required.

Implementation intentions strengthen the existing UDAM wording around:

```text
conditional action maps
concrete cue-action pairs
execution after observation
playbook usability
```

The main cautions are:

```text
execution support != value support
cue-response mapping != state-informativeness
if-then plan != proof of UDAM
component support != full synthesis proof
```

## Next literature topic

The next check should be:

```text
active inference / epistemic value
```

Reason:

Implementation intentions verify the execution side of conditional action. Active inference and epistemic value are the next natural area for checking action chosen partly to gain information.
