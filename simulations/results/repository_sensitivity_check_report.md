# UDAM repository-facing toy sensitivity checks

These are toy demonstrations, not empirical validation.

## 1. Observation-cost threshold sensitivity

This check extends the observation-value toy model by varying signal accuracy and computing the break-even observation cost.

Interpretation boundary: a higher threshold means a more accurate observation can tolerate a higher observation cost under this toy setup. It does not mean that more observation is always better.

| signal_accuracy | break_even_observation_cost | strictly_favorable_nonnegative_cost_exists | favorable_sample_cost_count | max_favorable_sample_cost |
|---|---|---|---|---|
| 0.50 | 0.00 | false | 0 |  |
| 0.55 | 1.00 | true | 1 | 0 |
| 0.60 | 2.00 | true | 2 | 1 |
| 0.65 | 3.00 | true | 3 | 2 |
| 0.70 | 4.00 | true | 3 | 2 |
| 0.75 | 5.00 | true | 4 | 4 |
| 0.80 | 6.00 | true | 4 | 4 |
| 0.85 | 7.00 | true | 5 | 6 |
| 0.90 | 8.00 | true | 5 | 6 |
| 0.95 | 9.00 | true | 6 | 8 |

## Interpretation

- At accuracy `0.50`, the signal has no positive break-even cost.
- Higher signal accuracy raises the break-even observation cost in this toy setup.
- This reinforces the existing guardrail: state-informative still must be favorable after cost.
- This is a toy sensitivity check, not empirical validation.
