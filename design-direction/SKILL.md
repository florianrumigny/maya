---
name: design-direction
description: "Explore and select a distinctive visual direction for a new app, website, or major surface before implementation. Use when the product direction exists but the visual identity is unclear, when several art directions should be compared, or when a greenfield interface risks falling into generic AI patterns."
---

# Design Direction

Run an image-first divergence and selection process before implementation. Keep product behavior stable while visual hypotheses compete.

## Outcome

Finish with a user-approved design thesis, selected visual references, explicit risks, and implementation handoff. This skill chooses a direction; it does not silently turn exploration into a finished build.

## Route the work

1. Identify the surface:
   - `native-mobile`: iOS, Android, React Native, Expo, Flutter.
   - `web-product`: dashboards, tools, authenticated product UI.
   - `web-brand`: landing pages, marketing sites, portfolios, campaigns.
2. Read [references/discovery.md](references/discovery.md) for every run.
3. Read exactly one platform reference:
   - [references/mobile.md](references/mobile.md) for `native-mobile`.
   - [references/web.md](references/web.md) for either web route.
4. Read [references/critic-loop.md](references/critic-loop.md) only when visual probes exist and critique is requested or useful before selection.
5. Read [references/handoff.md](references/handoff.md) only after the user selects a direction.

## Specialist routing

Use specialist skills as stages, not as one blended rulebook.

- Use Impeccable's product and platform guidance when product purpose, audience, information architecture, states, platform, or accessibility constraints are unresolved. Design Direction owns this discovery conversation: avoid starting a second interview or creating project artifacts during exploration.
- Use Taste `imagegen-frontend-mobile` for native-mobile visual probes when available.
- Use Taste `imagegen-frontend-web` for web visual probes when available.
- Use Taste `brandkit` only when the project lacks a coherent identity and identity exploration would materially improve the interface direction.
- Use Taste `design-taste-frontend` or `gpt-taste` as an implementation driver only for `web-brand` surfaces after a direction is selected.
- Use native image generation as the fallback when the matching Taste image skill is unavailable. Apply the same probe brief and comparison rules.
- Use Impeccable again for critique, distillation, accessibility, hardening, and polish after implementation.

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

Critique informs selection; it does not replace the user's taste. Limit pre-selection critique to one pass unless the probes are invalid or indistinguishable.

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

After confirmation, follow [references/handoff.md](references/handoff.md). Declare the implementation driver, quality gates, reference images, and fidelity criteria. Preserve or create `PRODUCT.md` and `DESIGN.md` only with user approval; never overwrite existing design context silently.

## Article-derived finish

After a real implementation exists:

1. Capture the rendered result at representative sizes.
2. Run one fresh-context visual critique.
3. Fix the highest-impact gaps.
4. Remove elements that do not aid task, meaning, trust, or identity.
5. Remove category reflexes and obvious AI tells.
6. Verify native conventions or responsive behavior, accessibility, states, and performance.
7. Ask the user to approve or rewrite high-salience copy such as the hero, onboarding promise, and primary CTA.

Default to two critique-and-revision cycles. Continue only when the work is still converging and the user wants another pass.
