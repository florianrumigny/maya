---
name: maya
description: "Design direction for new, in-progress, or existing app and web interfaces. Use to establish an axis from a sparse brief, compare visual foundations or directions, critique a current design, or convert an approved direction into durable guidance and primitives."
---

# MAYA

Orchestrate product framing, inspiration research, visual divergence, foundation studies, independent critique, selection, and design-system handoff. Keep product behavior stable while visual hypotheses compete.

Use **Most Advanced Yet Acceptable** as a calibration principle, not a house style: push each direction beyond the category default while preserving product comprehension, usability, and trust.

## Route the work

Classify both dimensions before proceeding:

- Starting state: `greenfield`, `in-progress`, or `existing`.
- Surface: `native-mobile`, `web-product`, or `web-brand`.

Load references only when their branch fires:

- Product framing, exploration modes, seeds, and direction cards: [discovery.md](references/discovery.md).
- Guided research routed by discovery: [inspiration-research.md](references/inspiration-research.md).
- No approved visual system, a request to compare type and color before screens, or probes lacking personality or coherence: [visual-foundations.md](references/visual-foundations.md).
- `in-progress`, `existing`, post-implementation review, or learning from exploration feedback: [evaluation-loop.md](references/evaluation-loop.md).
- Multi-turn exploration, resuming work, or a request for current progress: [status.md](references/status.md).
- Screen probes or implementation for `native-mobile`: [mobile.md](references/mobile.md).
- Web component or page comparisons, screen probes, or implementation: [web.md](references/web.md).
- Style tiles, probes, or captures that will affect a decision: [critic-loop.md](references/critic-loop.md).
- Approved direction moving to implementation: [design-contract.md](references/design-contract.md).

## Authority model

MAYA owns orchestration, the discovery conversation, the decision record, and the temporary run status. Platform references route companion skills by stage. Selecting a direction authorizes refinement in exploration space; production integration requires an explicit user request, including when a companion normally promotes its winner automatically.

For a multi-turn run, show the compact status card from `status.md` at the start and at phase changes. Keep it temporary and separate from durable project guidance.

## Workflow

### 1. Frame

Inspect the real material and build the stable product frame in `discovery.md`. For `in-progress`, separate commitments, hypotheses, and open questions. For `existing`, establish the matched baseline in `evaluation-loop.md` and choose `preserve`, `evolve`, or `overhaul`.

Continue when the product frame and exploration mode are recorded and, when applicable, a reproducible baseline exists. For an approved direction, resume at Contract or Evaluate unless the task reopens exploration. For hesitation between existing web alternatives, go to Probe with the framed choices; reopen research only when their rationale is insufficient.

### 2. Research

Follow discovery's mode routing, then use `inspiration-research.md` for the guided branch. Complete its research gate before drafting guided directions. The seeded branch follows discovery's independent preparation instead.

Continue when the applicable branch's preparation is complete and the researched territories have been presented where required.

### 3. Diverge

Use the direction cards and anti-convergence check in `discovery.md` to turn the prepared material into distinct hypotheses.

Continue when discovery's shortlisting criterion is met.

### 4. Foundations — when triggered

Use `visual-foundations.md` to compare the shortlisted directions before screen composition. Otherwise carry the approved visual system into Probe.

Continue when the foundation study meets its exit criterion, or the existing system covers the choices being tested and no foundation trigger applies.

### 5. Probe

Use `mobile.md` or `web.md` to create matched probes from the shortlisted directions or framed alternatives and any provisional foundations.

Continue when every candidate carried forward meets the platform reference's probe criterion.

### 6. Critique

Run the review in `critic-loop.md`. Apply the baseline comparison defined in `evaluation-loop.md` for existing work.

Continue when the critic's exit criterion is met and the evidence supports selection.

### 7. Select

Ask the user to choose one direction or a compatible synthesis with one dominant thesis. Record the winner, rejected patterns, properties to preserve, open questions, and platform risks. When motion defines the thesis, optionally create one short motion study after the static direction is accepted.

This step is complete when the user explicitly confirms the direction. Before closing an exploration, use the learning section of `evaluation-loop.md`, even when implementation is deferred.

### 8. Contract

After direction confirmation, propose the durable implementation contract through the creation gate in `design-contract.md`.

This step is complete when another agent can implement the direction from the approved contract and locate its executable primitives without repeating discovery.

### 9. Evaluate the implementation

Use `evaluation-loop.md` and `critic-loop.md` on representative rendered captures.

Finish when the matched comparison is valid, blocking findings are resolved or explicitly deferred, and the learning criterion in `evaluation-loop.md` is met.
