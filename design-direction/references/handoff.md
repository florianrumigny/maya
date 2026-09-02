# Selected-direction handoff

Run only after explicit user selection.

## Design thesis

Capture the decision in a compact handoff:

```md
# Selected Design Direction

## Product frame
[Stable functional and platform constraints]

## Thesis
[One sentence describing the distinctive design argument]

## Emotional target
[What the user should feel, in context]

## Visual system
- Composition:
- Typography:
- Color mechanics:
- Shape and component language:
- Imagery/material:
- Motion:
- Signature moment:

## References
[Selected probes and named quality bars]

## Preserve
[3-5 properties that must survive implementation]

## Reject
[Discarded patterns, directions, and AI tells]

## Platform expression
[Native or responsive rules that shape the visual system]

## Risks and tests
[Feasibility, accessibility, content, performance, and fidelity checks]
```

## Declare authorities

State the handoff before implementation:

```md
Implementation driver: [one skill/workflow]
Visual reference: [selected direction and probes]
UX/platform authority: [one skill/workflow]
Quality gates: [critique, accessibility, responsive/native, performance]
```

Suggested defaults:

- Native mobile: native/Expo implementation skill drives; Impeccable owns UX and quality; Taste probes are references.
- Web product: Impeccable drives; Taste probes are references.
- Web brand: Taste frontend skill may drive; Impeccable owns final quality gates.

## Persist context

If the project uses `PRODUCT.md`, preserve the product frame there. If it uses `DESIGN.md`, record the approved system there after user confirmation. Link reference images by durable project path when available.

Keep exploration notes separate from normative design rules. The random seed explains how a direction was found; it is not a production token.

Completion criterion: another agent can implement the chosen direction without seeing rejected concepts or re-running discovery.
