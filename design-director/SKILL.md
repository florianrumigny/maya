---
name: design-director
description: "Design direction for new, in-progress, or existing app and web interfaces. Use to establish an axis from a sparse brief, compare visual directions, critique a current design, or convert an approved direction into durable guidance and primitives."
---

# Design Director

Orchestrate product framing, visual divergence, independent critique, selection, and design-system handoff. Keep product behavior stable while visual hypotheses compete.

## Route the work

Classify both dimensions before proceeding:

- Starting state: `greenfield`, `in-progress`, or `existing`.
- Surface: `native-mobile`, `web-product`, or `web-brand`.

Load references only when their branch fires:

- Every run: [discovery.md](references/discovery.md).
- `in-progress`, `existing`, or post-implementation review: [evaluation-loop.md](references/evaluation-loop.md).
- `native-mobile`: [mobile.md](references/mobile.md).
- Either web surface: [web.md](references/web.md).
- Probes or captures that will affect a decision: [critic-loop.md](references/critic-loop.md).
- Approved direction moving to implementation: [design-contract.md](references/design-contract.md).

## Authority model

Design Director owns orchestration, the discovery conversation, and the decision record. Use the platform references to route Impeccable, Taste, image generation, and native/Expo expertise by stage.

## Workflow

### 1. Frame

Build the stable product frame in `discovery.md`. For `in-progress`, separate commitments, hypotheses, and open questions. For `existing`, establish the matched baseline in `evaluation-loop.md` and choose `preserve`, `evolve`, or `overhaul`.

Continue when every direction can use the same functional skeleton and, when applicable, a reproducible baseline exists.

### 2. Diverge

Follow the verbal exploration and optional seed method in `discovery.md`. Keep directions meaningfully different rather than varying decoration on one layout.

Continue when the user has shortlisted 2-4 directions, or explicitly delegated that shortlist.

### 3. Probe

Follow the applicable platform reference. Hold task, content, state, viewport, and product structure constant across candidates. Treat generated UI as a visual hypothesis, not a product specification.

Continue when every shortlisted direction can be compared on composition, typography, color, imagery, component language, and motion intent.

### 4. Critique

When critique can change the decision, run the fresh-context review in `critic-loop.md`. Apply the baseline comparison defined in `evaluation-loop.md` for existing work. Use one pre-selection pass unless the probes are invalid or indistinguishable.

Continue when the review yields a ranked, finite correction set and enough evidence to choose.

### 5. Select

Ask the user to choose one direction or a compatible synthesis with one dominant thesis. Record the winner, rejected patterns, properties to preserve, open questions, and platform risks. When motion defines the thesis, optionally create one short motion study after the static direction is accepted.

Stop before implementation. This step is complete only when the user explicitly confirms the direction.

### 6. Contract and implement

After confirmation, create the durable implementation contract in `design-contract.md`.

This step is complete when another agent can implement the direction from the approved contract and locate its executable primitives without repeating discovery.

### 7. Evaluate the implementation

Use `evaluation-loop.md` and `critic-loop.md` on representative rendered captures. Default to at most two critique-and-revision passes; continue only while the work is converging and the user wants another pass.

Finish when the matched comparison is valid, blocking findings are resolved or explicitly deferred, and reusable feedback lives in its narrowest source of truth.
