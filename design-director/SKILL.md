---
name: design-director
description: "Direct the design of a new or existing app, website, or major surface: explore distinctive directions, critique current work, select an axis, and turn repeated decisions into durable product guidance and design primitives. Use when visual identity is unclear, a design is in progress, or an interface needs a deliberate redesign rather than generic polish."
---

# Design Director

Run an evidence-led direction process before implementation, or a matched critique-and-redesign process for existing work. Keep product behavior stable while visual hypotheses compete.

## Outcome

Finish with a user-approved design thesis, selected visual references, explicit risks, and an implementation contract. When work continues into implementation, leave behind only the durable product guidance, design guidance, primitives, and checks the project actually needs.

## Route the work

1. Identify the starting state:
   - `greenfield`: no meaningful design direction exists.
   - `in-progress`: hypotheses or partial screens exist, but the axis is unresolved.
   - `existing`: a real design exists and should be preserved, evolved, or overhauled.
2. Identify the surface:
   - `native-mobile`: iOS, Android, React Native, Expo, Flutter.
   - `web-product`: dashboards, tools, authenticated product UI.
   - `web-brand`: landing pages, marketing sites, portfolios, campaigns.
3. Read [references/discovery.md](references/discovery.md) for every run.
4. For `in-progress` or `existing`, read [references/evaluation-loop.md](references/evaluation-loop.md) before proposing directions.
5. Read exactly one platform reference:
   - [references/mobile.md](references/mobile.md) for `native-mobile`.
   - [references/web.md](references/web.md) for either web route.
6. Read [references/critic-loop.md](references/critic-loop.md) when visual probes or implementation captures exist and critique will affect a decision.
7. Read [references/handoff.md](references/handoff.md) and [references/design-contract.md](references/design-contract.md) only after the user selects a direction.

## Specialist routing

Use specialist skills as stages, not as one blended rulebook. Design Director owns orchestration and the decision record.

- Use Impeccable's product and platform guidance when product purpose, audience, information architecture, states, platform, or accessibility constraints are unresolved. Design Director owns this discovery conversation: avoid starting a second interview or creating project artifacts during exploration.
- Use Taste `imagegen-frontend-mobile` for native-mobile visual probes when available.
- Use Taste `imagegen-frontend-web` for web visual probes when available.
- Use Taste `brandkit` only when the project lacks a coherent identity and identity exploration would materially improve the interface direction.
- Use Taste `design-taste-frontend` or `gpt-taste` as an implementation driver only for `web-brand` surfaces after a direction is selected.
- Use native image generation as the fallback when the matching Taste image skill is unavailable. Apply the same probe brief and comparison rules.
- Use Impeccable again for structured UX critique, distillation, accessibility, hardening, and polish after implementation. Use a fresh-context critic for independent visual judgment; these are complementary reviews.

Do not load the full Taste implementation rules and the full Impeccable implementation rules as co-equal authorities. Declare one implementation driver and treat the other as a quality gate.

## Gates

### 1. Discovery gate

Establish the stable product frame before style exploration:

- user and context;
- primary job and action;
- required content and realistic states;
- platform and surface type;
- emotional intent and brand personality;
- references and anti-references, when known;
- accessibility and technical constraints.

Ask 2-3 high-leverage questions per round. At least one real user-answer round is required when the brief is sparse. Completion criterion: the same functional skeleton can be used to compare every visual direction.

For `in-progress`, first separate committed constraints from untested hypotheses and open questions. For `existing`, capture a representative baseline and ask whether the intended mode is `preserve`, `evolve`, or `overhaul`. Do not erase strengths merely to make the redesign visibly different.

### 2. Divergence gate

Generate 6-10 terse direction seeds in words before expensive visual generation. Each direction must name:

- design thesis;
- emotional effect;
- source world outside the obvious product category;
- composition, type, color, material, and motion logic;
- one memorable signature;
- main risk.

Use three creative distances: `grounded`, `adjacent`, and `frontier`. Reject variations that merely reskin the same layout.

When the user asks to be surprised, has no references, or requests random exploration, generate one seed for every initial direction before writing the direction cards. Resolve the script path relative to this skill's directory and run it with the same count:

```bash
node <skill-directory>/scripts/generate-seeds.mjs --count 8
```

Interpret each seed using [references/discovery.md](references/discovery.md), then let it influence its direction before shortlisting. Preserve exact values only for shortlisted directions in internal exploration notes. Show `Exploration mode: seeded` instead of raw values unless the user asks for them. Never display a seed in the product UI.

Completion criterion: the user shortlists 2-4 meaningfully different directions, or explicitly delegates that shortlist.

### 3. Probe gate

Generate a comparable probe set for every shortlisted direction. Keep content, viewport, task, and product structure constant so visual identity is the variable.

- Mobile: first generate one representative screen per direction; after two finalists emerge, generate 2-3 connected screens for each finalist.
- Web product: one representative workflow surface per direction, plus one important state if needed.
- Web brand: hero plus 1-2 representative sections per direction; generate the full page only after selection.

Label outputs by direction. Treat generated UI text and controls as hypotheses rather than specifications. Completion criterion: each direction is concrete enough for a user to compare composition, typography, color, imagery, component language, and motion intent.

### 4. Critique gate

When subagents are available, dispatch a fresh visual critic with no inherited conversation history using [references/critic-loop.md](references/critic-loop.md). Give it the product frame, probe images, and references, but no source code, implementation rationale, earlier critique, or target score.

Critique informs selection; it does not replace the user's taste. For existing work, critique the baseline before divergence and compare finalists against that same baseline after probing. Limit pre-selection critique to one pass unless the probes are invalid or indistinguishable.

### 5. Selection gate

Ask the user to choose one direction or a deliberately compatible synthesis. Record:

- what wins;
- what is rejected;
- what must survive implementation;
- what remains open;
- platform-specific risks.

Avoid feature-by-feature democracy across every concept. A synthesis needs one dominant thesis.

When motion is central to the selected thesis, the static direction is approved, and video generation is available, create one short motion study or state-transition study. Keep it a reference for timing, material, and continuity rather than shipping generated video by default.

Stop before implementation and request explicit confirmation of the selected direction.

### 6. Handoff gate

After confirmation, follow [references/handoff.md](references/handoff.md) and [references/design-contract.md](references/design-contract.md). Declare the implementation driver, quality gates, reference images, and fidelity criteria. Propose the smallest durable artifact set, show what will be created or changed, and obtain approval before overwriting existing design context.

Treat the system as three layers:

1. **Guidance:** product intent and design judgment that require interpretation.
2. **Primitives:** executable tokens, components, classes, or themes that bound implementation choices.
3. **Evaluation:** matched captures, human critique, and deterministic checks for recurring mechanical failures.

Do not confuse these layers. A token belongs in code, not only in prose. A compositional judgment belongs in `DESIGN.md`, not a linter. A repeated overflow or contrast failure may deserve a deterministic check.

## Article-derived finish

After a real implementation exists:

1. Capture the rendered result at representative sizes using the same content, state, data, viewport, and task as the baseline when comparing versions.
2. Run one fresh-context visual critique plus relevant deterministic checks.
3. Fix the highest-impact gaps and record feedback in the narrowest durable layer described in [references/evaluation-loop.md](references/evaluation-loop.md).
4. Remove elements that do not aid task, meaning, trust, or identity.
5. Remove category reflexes and obvious AI tells.
6. Verify native conventions or responsive behavior, accessibility, states, and performance.
7. Ask the user to approve or rewrite high-salience copy such as the hero, onboarding promise, and primary CTA.

Default to two critique-and-revision cycles. Continue only when the work is still converging and the user wants another pass.
