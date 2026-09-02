# Durable design contract

Create the smallest non-duplicative artifact set that lets future agents understand the product, exercise design judgment, and implement consistently. Inspect existing project conventions before proposing filenames.

## Default artifact split

| Layer | Default artifact | Contains | Must not become |
|---|---|---|---|
| Product intent | `PRODUCT.md` | audience, jobs, product promise, platform, constraints, anti-goals, success criteria | a visual style guide |
| Design judgment | `DESIGN.md` | selected thesis, reader/user framing, hierarchy, composition, content evidence, type/color/material/motion logic, signature patterns, anti-patterns, accessibility intent | a dump of every exploration or raw token values |
| Brand identity | `BRAND.md`, only when warranted | voice, identity assets, logo rules, imagery world, brand-specific color/type governance | a duplicate of `DESIGN.md` |
| Executable primitives | project-native source | tokens, themes, reusable components, variants, states, motion constants | prose that drifts away from the implementation |
| Evaluation | lightweight fixtures and checks | comparison scenarios, captures, recurring feedback, deterministic checks | a permanent log of one-off taste reactions |

`PRODUCT.md` and `DESIGN.md` are recommended outputs once a direction is approved, but adapt to an existing repository's canonical files. Do not create aliases that duplicate current sources of truth.

## Platform expression

- Web product: prefer existing CSS variables, theme configuration, component variants, and documented primitives. A bounded stylesheet/class vocabulary is useful when agents repeatedly compose pages directly from HTML/CSS.
- Web brand: a documented stylesheet may be the right public vocabulary when many pages share a controlled set of compositions. Pair it with examples or components; prose alone is insufficient.
- Expo or React Native: use typed tokens or a theme module plus reusable native components. Do not invent a CSS stylesheet merely to imitate a web workflow.
- Native iOS or Android: use the project's resource, theme, and component conventions.

The executable layer is the implementation source of truth for exact values. `DESIGN.md` explains why and when to use those values.

## Minimum `DESIGN.md` shape

```md
# Design Direction

## Product and user frame
## Design thesis
## Experience principles
## Content and evidence hierarchy
## Composition and responsive/native behavior
## Typography, color, shape, imagery, and motion
## Signature patterns
## States and accessibility
## Avoid
## References and implementation pointers
```

Include only sections that carry decisions. Favor concrete rules with examples and honest caveats over adjectives such as “clean,” “premium,” or “modern.”

## Creation gate

Before writing files, present:

1. files to create or update;
2. the canonical source for exact tokens and components;
3. overlaps that will be removed;
4. which decisions remain provisional.

Obtain user approval before replacing existing normative files.
