# Web direction

Use for responsive web products and brand/marketing surfaces.

## Choose the register

- `web-product`: design serves a repeated task. Familiarity, density, states, keyboard use, and consistency dominate.
- `web-brand`: design communicates identity and persuasion. Composition, imagery, pacing, and memorable expression may take larger risks.

Do not use a landing-page aesthetic as the visual model for authenticated product screens.

## Probe sets

Enter with shortlisted direction cards and provisional foundations, or the framed alternatives the user is already weighing. Hold content, task, state, viewport, and functional structure constant. Use executable probes when interaction or page composition will settle the choice; image probes remain useful for visual hypotheses that do not need working behavior.

### Executable comparison — prototype

Offer Emil Kowalski's `prototype` when the user hesitates between visual choices or would benefit from trying variants. An explicit request to compare working versions authorizes the exploration; respect the host's invocation mechanism. If its user-only skill gate requires a named invocation, ask the user to invoke `prototype` rather than bypassing the gate.

Once invoked, load the installed companion and its `PICKER.md`. Keep variant construction, picker behavior, verification, and cleanup owned there. Pass the product frame, real material from discovery, candidate theses, fixed comparison scenario, and the boundaries below:

- Scope defaults to one component or section. When the user explicitly requests complete pages, pass that request as a scoped exception to the companion's narrowing rule: compare complete pages with the same real content, navigation, and required states.
- Reuse approved project primitives. When the brief reopens the visual system, identify which tokens and compositions may vary inside the isolated exploration surface.
- Reuse MAYA's shortlist rather than generating a second competing set. For existing choices without cards, name each thesis and the difference it tests before building.
- Follow MAYA's production-integration boundary in [SKILL.md](../SKILL.md#authority-model) when handing back a selection.

If the companion is unavailable, explain the limitation and offer its installation or image probes; keep the picker implementation in the companion rather than recreating it in MAYA. HTML probes establish web behavior, not native-platform validation.

Continue when the companion's verification passes and each variant can be compared at realistic size with working interactions and responsive behavior. Supply matched captures to the critic and the live comparison to the user.

### Image comparison

Pass the product frame, each direction card with its origin, and any provisional tile to the image generator. Treat generated UI as a visual hypothesis, not a product specification.

#### Web product

Use the same representative workflow, realistic data, viewport, and state across directions. One primary screen is usually sufficient; add an empty, loading, or detail state when it reveals the design system.

Use Taste image generation only as a visual probe. Impeccable remains the product UX authority.

#### Web brand

For each direction, generate:

1. the hero;
2. one section that explains or demonstrates value;
3. one proof or conversion section when needed.

Use Taste `imagegen-frontend-web` when available, with native image generation as the fallback. During Probe, override its full-page default: generate only the comparable probe sections. Generate the complete section set after selection.

Continue to critique when each candidate has a matched representative screen or section set and any tile-derived system can be judged with real content.

## Implementation routing

For authorized implementation after selection:

- `web-product`: Impeccable drives implementation and quality.
- `web-brand`: Taste `gpt-taste` or `design-taste-frontend` may drive implementation; Impeccable gates accessibility, responsive behavior, restraint, and polish.
- Record one authority for disputed aesthetic decisions. Resolve conflicts against the approved design thesis rather than blending rulebooks.

Completion criterion: the direction works at desktop and mobile widths and remains identifiable without relying on one decorative hero effect.
