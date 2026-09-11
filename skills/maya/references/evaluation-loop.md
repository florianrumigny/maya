# Critique and evaluation loop

Use the baseline and comparison sections for an in-progress or existing design and after implementation. Use the learning section when closing an exploration or evaluation with user feedback. The goal is not an abstract score; it is a fair comparison and a better project memory.

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

## Learn from corrections

Separate feedback by scope:

- **Local decision:** applies to this variant, screen, or task. Keep it in the conversation or existing exploration notes and apply it within the authorized scope.
- **Durable candidate:** could guide future work in this project. State its scope and supporting evidence; repeated feedback or an explicitly general user preference can justify a proposal, but repetition alone does not make a rule.

For each durable candidate, consult the canonical destinations in [design-contract.md](design-contract.md). Present the exact proposed wording, rationale, destination, and whether it adds, merges, replaces, or removes an existing rule. Surface contradictions and stale guidance rather than appending another layer. Project preferences stay in the project; they do not become general MAYA rules.

Obtain explicit user approval before promoting a learning into any durable source. Apply only the approved change; leave pending or rejected candidates in exploration context without a separate learning backlog. Reuse the existing wording when it already covers the feedback. If no candidate generalizes, close without a document update.

For authorized implementation, reusable mechanics belong in project-native primitives; repeated mechanical failures may justify deterministic checks. Human judgment still owns composition and brand fit. Correct invalid comparison scenarios before drawing lessons from them.

Complete when local decisions are separated from durable candidates, every proposed promotion has wording and a destination, and only explicitly approved promotions have been written. Pending proposals do not block delivery of the exploration.

## Finish pass

After the highest-impact corrections:

1. Remove elements that contribute neither task, meaning, trust, nor identity.
2. Replace category reflexes and obvious AI-generated tells with choices supported by the thesis.
3. Verify native or responsive behavior, accessibility, critical states, and performance.
4. Ask the user to approve or rewrite high-salience copy such as the hero, onboarding promise, and primary action.

## Keep the loop lightweight

Start with one repeated representative scenario, a baseline capture, the selected comparison, and a short correction list. Add formal fixtures or automated checks only after a failure repeats or the artifact type recurs enough to justify them.
