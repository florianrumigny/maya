# Critique and evaluation loop

Use this loop for an in-progress or existing design and after implementation of a selected direction. The goal is not an abstract score; it is a fair comparison and a better project memory.

## Establish the baseline

Capture the current design before proposing changes. Record:

- representative task, content, data, state, viewport, and platform;
- intended audience and success condition;
- strengths that should survive;
- known problems and uncertainty;
- redesign mode: `preserve`, `evolve`, or `overhaul`.

Do not compare a polished redesign with richer content against a weak or incomplete baseline. Keep the scenario matched so the design variable is legible.

## Critique before divergence

Run the fresh-context critic from [critic-loop.md](critic-loop.md) on the baseline. Separate findings into:

- judgment failures: hierarchy, composition, evidence, tone, or product fit;
- reusable mechanic gaps: missing token, component, variant, or layout primitive;
- mechanical failures: overflow, contrast, tap target, broken state, responsiveness, or asset loading;
- one-off preference: subjective feedback that has not repeated.

Use the critique to write the redesign brief, not to prescribe the final look.

## Compare fairly

For each finalist and the baseline, reuse the scenario from [mobile.md](mobile.md) or [web.md](web.md); also hold the model, when relevant, and capture procedure constant. Use [critic-loop.md](critic-loop.md) for the review packet, comparison rubric, and iteration limits.

## Place feedback in the narrowest durable layer

- Put recurring judgment in `DESIGN.md`.
- Put reusable mechanics in tokens, themes, components, classes, or examples.
- Put repeated mechanical failures in deterministic tests or checks.
- Fix the evaluation scenario when the comparison itself is invalid.
- Do not encode a model-specific or personal one-off unless it recurs and generalizes.

Human judgment owns subjective hierarchy, composition, and brand fit. Deterministic checks own known mechanical failures. Neither replaces the other.

## Finish pass

After the highest-impact corrections:

1. Remove elements that contribute neither task, meaning, trust, nor identity.
2. Replace category reflexes and obvious AI-generated tells with choices supported by the thesis.
3. Verify native or responsive behavior, accessibility, critical states, and performance.
4. Ask the user to approve or rewrite high-salience copy such as the hero, onboarding promise, and primary action.

## Keep the loop lightweight

Start with one repeated representative scenario, a baseline capture, the selected comparison, and a short correction list. Add formal fixtures or automated checks only after a failure repeats or the artifact type recurs enough to justify them.
