# Native mobile direction

Use for iOS, Android, Expo, React Native, Flutter, and other native-mobile surfaces.

## Probe set

Enter with shortlisted direction cards and any provisional style tiles from the Foundations stage in [SKILL.md](../SKILL.md). Keep one device family, viewport, content fixture, state, and functional flow across directions. Treat generated UI as a visual hypothesis, not a product specification.

Use a staged probe:

1. Generate one representative primary screen for every direction carried forward from Diverge or Foundations.
2. If more than two candidates remain, ask the user to choose up to two finalists or use an explicitly delegated choice.
3. Generate 2-3 connected screens for each finalist:

   - the primary or home state;
   - the screen where the main action occurs;
   - one state that exposes the system, such as empty, progress, completion, error, or detail.

Show the interface itself rather than decorative device mockups unless physical presentation is the explicit deliverable. Text must be large enough to judge hierarchy. Keep navigation and controls believable.

When available, use Taste `imagegen-frontend-mobile` to generate the probes. Pass the stable product frame, direction card with its origin, any provisional tile, fixed screen list, platform, and comparison constraints. Native image generation is the fallback.

Continue to critique when each candidate has a matched representative screen and any tile-derived system can be judged with real content.

## Platform guardrails

The direction may vary brand expression, composition within a screen, imagery, type emphasis, color roles, shape language, motion character, and moments of delight. It must preserve platform literacy:

- safe areas and system bars;
- expected back behavior;
- reachable and sufficiently large touch targets;
- scalable text and localization tolerance;
- keyboard and input behavior;
- light/dark and contrast needs;
- reduced-motion behavior;
- familiar semantics for navigation, sheets, dialogs, toggles, and destructive actions.

For an adaptive app, state which details follow iOS and which follow Android. A single brand language may sit above two platform expressions.

## Implementation routing

For authorized implementation after selection:

- Use Impeccable as the UX and quality authority.
- Use the relevant native/Expo skill as implementation authority.
- Treat Taste-generated images as visual references, not pixel contracts.
- Compare simulator captures with references while allowing corrections for platform behavior, accessibility, and real content.

Completion criterion: the chosen direction can survive on both the ideal mockup and a real small device with dynamic content.
