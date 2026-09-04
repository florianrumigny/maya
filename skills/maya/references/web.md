# Web direction

Use for responsive web products and brand/marketing surfaces.

## Choose the register

- `web-product`: design serves a repeated task. Familiarity, density, states, keyboard use, and consistency dominate.
- `web-brand`: design communicates identity and persuasion. Composition, imagery, pacing, and memorable expression may take larger risks.

Do not use a landing-page aesthetic as the visual model for authenticated product screens.

## Probe sets

Enter with shortlisted direction cards and any provisional style tiles from the Foundations stage in [SKILL.md](../SKILL.md). Pass the stable product frame, each card with its origin, and any tile to the image generator. Treat generated UI as a visual hypothesis, not a product specification.

### Web product

Use the same representative workflow, realistic data, viewport, and state across directions. One primary screen is usually sufficient; add an empty, loading, or detail state when it reveals the design system.

Use Taste image generation only as a visual probe. Impeccable remains the product UX authority.

### Web brand

Keep content, task, state, viewport, and functional structure matched across directions. For each direction, generate:

1. the hero;
2. one section that explains or demonstrates value;
3. one proof or conversion section when needed.

Use Taste `imagegen-frontend-web` when available, with native image generation as the fallback. During Probe, override its full-page default: generate only the comparable probe sections. Generate the complete section set after selection.

Continue to critique when each candidate has a matched representative screen or section set and any tile-derived system can be judged with real content.

## Implementation routing

After selection:

- `web-product`: Impeccable drives implementation and quality.
- `web-brand`: Taste `gpt-taste` or `design-taste-frontend` may drive implementation; Impeccable gates accessibility, responsive behavior, restraint, and polish.
- Record one authority for disputed aesthetic decisions. Resolve conflicts against the approved design thesis rather than blending rulebooks.

Completion criterion: the direction works at desktop and mobile widths and remains identifiable without relying on one decorative hero effect.
