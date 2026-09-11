# Temporary design status

Use this reference when an exploration spans multiple turns, when the user asks where the work stands, or when a project needs a handoff snapshot. The status is operational context for the current design run. It is not a product, brand, or design rule.

## Show the status

Render a compact status card in the conversation at the start of the run and when a gate changes. Use a temporary `DESIGN-STATUS.md` only when the work must survive a context break or the user asks for a file. If a project already has a canonical status or planning file, use it. Otherwise use the existing scratch or exploration location; do not create a harness directory for this purpose.

```md
MAYA · [project or surface]
[starting state] · [surface] · [phase]

Exploration    [██████░░░░] 4/7 · 57%
Implementation [░░░░░░░░░░] 0/3 · 0%

Current question: [the decision this run is answering]
Confirmed: [short list]
Open: [short list]
Next: [one concrete action]
```

The bar measures completed required gates on the active route. It does not measure visual quality, confidence, effort, or time. Always show the fraction beside the percentage so a skipped or inherited phase remains legible. Round the percentage to the nearest whole number and use a ten-cell bar.

Keep exploration and implementation separate. A selected direction can show `Exploration 100%` while `Implementation 0/3 · 0%` when the user has not authorized integration. If delivery is outside the run, show `Implementation — not started` rather than treating it as an unfinished gate.

## Build the route

Include only gates required by this run. Mark inherited work as `inherited` and irrelevant work as `skipped`; do not make the user repeat it to improve the number.

The exploration gates are:

1. `Frame` — real material, product frame, and preserve/open boundaries are clear.
2. `Research` — required for guided or mixed exploration.
3. `Diverge` — distinct candidate directions exist and pass the anti-convergence check.
4. `Foundations` — required when the visual system is unresolved or the branch triggers it.
5. `Probe` — candidates are comparable with matched content, state, and viewport.
6. `Critique` — the evidence and ranked corrections are complete when critique can change selection.
7. `Select` — the user confirms one direction or compatible synthesis.

The delivery gates are `Contract`, `Implement`, and `Evaluate`. Add them only when that work is authorized. A request to compare existing alternatives may enter at `Probe` after `Frame`; a request to critique an implementation may end at `Evaluate` without reopening exploration.

## Update and close

Refresh the card only when the phase, user decision, open question, next action, or authorization changes. Keep the current snapshot short; do not turn it into an append-only session log.

If using `DESIGN-STATUS.md`, overwrite the snapshot at each gate. Delete it or move it to the project's existing archive when the run closes, unless the user asks to retain it. Before closing, state the final phase, unresolved questions, pending learning proposals, and whether implementation is authorized.

Complete the status when the user can tell the current phase, the completed and remaining gates, the confirmed decisions, the next action, and the implementation boundary without reading the whole conversation.
