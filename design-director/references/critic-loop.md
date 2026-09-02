# Fresh-context visual critic

Use a separate subagent when available. Spawn it without inherited conversation history when the agent system supports that option, and pass only the critic packet in its initial task. A full-history fork is not an independent review. The context boundary matters: the critic should judge the rendered work rather than defend its implementation history. If no independent context is available, explicitly switch roles and withhold implementation rationale from the review packet.

## Critic packet

Provide only:

- stable product frame;
- direction cards or selected thesis;
- probe or implementation screenshots;
- a baseline screenshot when improving existing work;
- named references, labeled as quality bars rather than copy targets;
- the rubric below.

Exclude source code, effort spent, implementation explanations, previous critiques, desired winner, and stopping score.

## Prompt

```text
Act as an independent visual design critic. Infer the quality bar implied by
the product frame and references. Judge the images as rendered artifacts.

First describe the immediate impression without softening it. Then assess:
1. product and audience fit;
2. distinctiveness and ownability;
3. hierarchy and composition;
4. typography and color logic;
5. interaction or platform plausibility;
6. accessibility risks visible in the artifact;
7. category reflexes and AI-generated tells;
8. elements that should be removed;
9. feasibility risks during implementation.

Return the three highest-impact changes in priority order. When comparing
directions or a redesign against its baseline, rank them and explain the
tradeoff. Propose a hybrid only when two directions share a compatible thesis.
```

## Scorecard

Score each dimension from 1-5 and attach one sentence of evidence:

- fit;
- identity;
- coherence;
- usability;
- platform literacy;
- polish.

The score is diagnostic. Do not iterate until an arbitrary total is reached.
