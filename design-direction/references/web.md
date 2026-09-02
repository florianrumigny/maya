# Web direction

Use for responsive web products and brand/marketing surfaces.

## Choose the register

- `web-product`: design serves a repeated task. Familiarity, density, states, keyboard use, and consistency dominate.
- `web-brand`: design communicates identity and persuasion. Composition, imagery, pacing, and memorable expression may take larger risks.

Do not use a landing-page aesthetic as the visual model for authenticated product screens.

## Probe sets

### Web product

Use the same representative workflow, realistic data, viewport, and state across directions. One primary screen is usually sufficient; add an empty, loading, or detail state when it reveals the design system.

Use Taste image generation only as a visual probe. Impeccable remains the product UX authority.

### Web brand

For each direction, generate:

1. the hero;
2. one section that explains or demonstrates value;
3. one proof or conversion section when needed.

Use Taste `imagegen-frontend-web` when available. During divergence, override its full-page default: generate only the comparable probe sections. Generate the complete section set after selection.

When the product has no identity, Taste `brandkit` may generate a compact board for each final contender. Use it after the verbal shortlist so logo and mockup generation do not prematurely lock the exploration.

## Implementation routing

After selection:

- `web-product`: Impeccable drives implementation and quality.
- `web-brand`: Taste `gpt-taste` or `design-taste-frontend` may drive implementation; Impeccable gates accessibility, responsive behavior, restraint, and polish.
- Record one authority for disputed aesthetic decisions. Resolve conflicts against the approved design thesis rather than blending rulebooks.

Completion criterion: the direction works at desktop and mobile widths and remains identifiable without relying on one decorative hero effect.
