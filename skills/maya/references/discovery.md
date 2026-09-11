# Discovery and seed interpretation

Use this reference to keep exploration broad without losing product relevance.

## Real material first

Before designing, read the project's canonical product, brand, and design guidance (`PRODUCT.md`, `BRAND.md`, `DESIGN.md`, or existing equivalents). Inspect the relevant rendered UI, source components, tokens, assets, content, and critical states where they exist. Use this material to frame the alternatives; preserve approved primitives unless the requested exploration explicitly reopens them.

Record the sources consulted, commitments to preserve, choices open to change, and conflicts between guidance and implementation. If rendering or source access is unavailable, identify the missing evidence and use the available material; keep affected conclusions provisional. For greenfield work, start from the supplied brief and assets.

Continue when the available material is inspected and the preserved/open boundaries are explicit. Keep this frame in the conversation or existing exploration notes; create no additional source of truth for it.

## Stable product frame

Summarize the invariant frame in one compact block:

```md
Surface:
Platform:
Audience and context:
Primary job:
Primary action:
Required content:
Critical states:
Emotional intent:
Constraints:
Anti-goals:
Approved visual system or unresolved choices:
```

Resolve missing answers within this conversation, using Impeccable's product and platform guidance when available. Keep the frame in exploration notes until [design-contract.md](design-contract.md) applies. Continue when the primary job, action, content, states, and constraints define one functional skeleton for all candidates.

## Exploration modes

Record the mode before gathering external inspiration. Inspecting the project's own material remains part of framing in every mode:

- `guided`: default when no direction is validated or previous proposals feel generic. Complete [inspiration-research.md](inspiration-research.md) before creating guided cards.
- `seeded`: use when the user requests random exploration or surprise. Follow the random seed method below; reference research is outside this branch.
- `mixed`: use when the user wants both researched and random alternatives. Prepare and freeze the seeded interpretations first, then run the guided research. Keep each card's origin explicit.

An absent reference set alone is a reason for guided research, not automatic randomization. When refining a validated direction, reuse its recorded evidence; reopen research if it no longer supports the requested changes.

## Broad verbal exploration

Create 6-10 compact cards unless the user specifies a different count. Derive guided cards from the presented research territories and seeded cards from their frozen interpretations. In mixed mode, split the total between the two branches and label each card individually. Cover the distinct territories before developing variations within one.

Use three distances:

- `grounded`: distinctive while familiar to the audience.
- `adjacent`: borrows organizing logic from a neighboring world.
- `frontier`: tests a surprising metaphor or composition while preserving usability.

Present the cards after the anti-convergence check. Continue when the user has shortlisted 2-4 cards or explicitly delegated that choice; deepen only the shortlist.

## Random seed method

Generate one seed per seeded direction before collecting research or interpreting visual references:

```bash
node <skill-directory>/scripts/generate-seeds.mjs --count 8
```

Match `--count` to the seeded portion of the exploration. The seed is an external creative stimulus, not hidden product truth. Read it through several lenses:

- segmentation and clusters;
- repetition and interruption;
- density and emptiness;
- symmetry and imbalance;
- numeric rhythm;
- contrast between character families;
- one anomalous moment.

Translate the observations into a coherent subset of decisions:

| Observation | Possible design translation |
| --- | --- |
| Strong repetition | Modular rhythm or repeated interaction motif |
| Abrupt cluster change | A single intentional material or scale shift |
| Sparse segment | Negative space or reduced control density |
| Dense segment | Compact information zone or layered detail |
| Near symmetry | Balanced frame with one controlled break |
| Numeric cadence | Spacing, timing, grid, or progression rhythm |
| One anomaly | One second-read moment or signature interaction |

Use judgment rather than encoding every character. Product requirements, accessibility, platform conventions, and the user's stated taste override the seed.

Record the exact seed, observed structure, and resulting visual hypothesis in exploration notes. Run the anti-convergence check below on the seeded hypotheses, then freeze their interpretations before guided research begins: research must not steer seed selection, rerolls, or their initial meaning. If research is already in context, use an independent context supplied only with the product frame and user constraints; if unavailable, disclose that independence cannot be guaranteed. Any later reference-informed revision becomes a guided derivative with its provenance recorded.

Continue when each seeded candidate has this record. Show the interpretation on its card; reveal the exact seed when the user requests reproducibility details.

## Direction card

```md
### [Name] — [grounded | adjacent | frontier]

Exploration mode: [seeded | guided]
Thesis: [one sentence]
Emotion: [specific response]
Source world: [non-software reference and borrowed logic]
Origin: [guided: territory ID and source IDs; seeded: interpretation and internal seed-record ID]
System: [composition, typography, palette mechanics, material/imagery, motion]
Signature: [one memorable but useful moment]
Risk: [main way this direction could fail]
```

## Anti-convergence check

Before shortlisting, compare the cards pairwise across layout topology, type voice, palette mechanics, material, imagery strategy, motion energy, and signature moment. Each pair must differ on at least two of these dimensions beyond a color or font swap.

Run two reflex checks:

1. Could the direction be guessed from the product category alone?
2. Could it be guessed from the category plus the instruction to avoid the obvious category style?

If either answer is yes or a pair fails the distinction test, revisit that branch's preparation while preserving the product frame. In mixed comparisons, resolve overlap by revising guided cards while keeping the seeded interpretations frozen. Continue when the pairwise and reflex checks pass.
