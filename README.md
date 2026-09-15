# MAYA

<p align="center">
  <img src="skills/maya/assets/brand/maya-logo-primary-512.png" width="320" alt="MAYA — a relic becoming a design system">
</p>

**Most Advanced Yet Acceptable.**

MAYA is a design-direction skill for AI coding agents. It helps teams explore distinctive visual directions, critique existing interfaces, select a coherent design thesis, and turn that decision into durable product guidance and implementation primitives.

MAYA is one orchestrator skill with focused references for discovery, inspiration research, visual foundations, mobile, web, critique, evaluation, and design-system handoff. It can coordinate other design skills without merging their instructions into one oversized prompt.

## What MAYA does

- Frames the product, audience, task, constraints, and emotional intent before styling.
- Inspects existing project guidance, rendered UI, components, tokens, and content before exploring.
- Researches real references across multiple disciplines and presents distinct territories before visual proposals.
- Can use the optional [Inspo MCP](https://inspomcp.dev/mcp) source to retrieve and compare real web references during inspiration research.
- Generates meaningfully different design directions at grounded, adjacent, and frontier distances.
- Supports independent random-seed exploration and mixed guided/seeded comparisons.
- Compares applied style tiles when identity is unresolved, when requested before screens, or when probes lack personality or coherence.
- Produces comparable image probes for native mobile, web products, and brand websites.
- Routes working web comparisons to Emil Kowalski's `prototype`, including complete pages when requested.
- Uses a fresh-context critic to review probes and rendered implementations.
- Shows a temporary, route-aware status card so the current phase, decisions, and next action stay visible.
- Handles greenfield projects, unresolved work in progress, and existing redesigns.
- Converts an approved direction into `PRODUCT.md`, `DESIGN.md`, optional `BRAND.md`, and project-native tokens or components.
- Separates local corrections from durable learning proposals for user approval.

## Workflow

1. **Frame** the stable product and platform constraints from real project material.
2. **Research** references and group them into territories for guided exploration; prepare the random branch independently in seeded or mixed mode.
3. **Diverge** into distinct verbal directions with traceable origins.
4. **Foundations**, when needed: compare typography, color roles, form, imagery, material, motion, and signature through matched style tiles.
5. **Probe** shortlisted directions with matched content, state, task, and viewport.
6. **Critique** the rendered artifacts from a fresh context.
7. **Select** one dominant thesis with explicit preserve and reject decisions.
8. **Contract** the direction through a proposed set of canonical guidance and executable primitives.
9. **Evaluate** the implementation against matched captures and recurring checks.

Foundations remain provisional until tested on a representative screen. Selecting a direction allows exploration refinement; production integration requires an explicit request. Normative document changes require approval of the proposed edits.

For hesitation between existing alternatives, MAYA can move from framing to probes. Exploration and evaluation close with the selective learning process in [evaluation-loop.md](skills/maya/references/evaluation-loop.md#learn-from-corrections).

## Installation

### Agent Skills CLI

Install MAYA directly from the public repository:

```bash
npx skills add https://github.com/florianrumigny/maya --skill maya
```

Reload your agent or start a new session after installation.

### Update an installed copy

After pushing changes to the repository, update a global MAYA installation with:

```bash
npx skills update maya -g -y
```

Use `-p` instead of `-g` for a project-scoped installation. Start a new agent turn after the update so it reloads the skill. This command applies to installations managed by the Agent Skills CLI; the source repository must be recorded in the installed skill metadata.

### Codex installer

You can also ask Codex:

```text
Install the maya skill from
https://github.com/florianrumigny/maya/tree/main/skills/maya
```

Or use Codex's bundled installer directly:

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo florianrumigny/maya \
  --path skills/maya
```

## Compatibility

MAYA follows the open Agent Skills format and is not limited to Codex. It can be installed in any compatible agent through the [Agent Skills CLI](https://github.com/vercel-labs/skills#supported-agents), including:

- Codex
- Claude Code
- Cursor
- GitHub Copilot
- Gemini CLI
- OpenCode
- Cline
- Windsurf

The installation command above automatically detects compatible agents and lets you select where MAYA should be installed.

You can also target a specific agent:

```bash
# Codex
npx skills add florianrumigny/maya --skill maya -a codex

# Claude Code
npx skills add florianrumigny/maya --skill maya -a claude-code

# Cursor
npx skills add florianrumigny/maya --skill maya -a cursor

# GitHub Copilot
npx skills add florianrumigny/maya --skill maya -a github-copilot

# Gemini CLI
npx skills add florianrumigny/maya --skill maya -a gemini-cli
```

The core workflow and references are agent-independent. The `agents/openai.yaml` file only provides additional metadata for OpenAI environments and can be ignored by other agents.

When independent sub-agents are supported, MAYA can use one for fresh-context critique. Otherwise, it performs the review through an explicit critic-role switch.

## Recommended companion skills

MAYA works on its own. The following optional skills unlock its full orchestration workflow.

### Impeccable

[Impeccable](https://impeccable.style/) provides product UX guidance, accessibility review, interface critique, hardening, and final polish.

```bash
npx impeccable install
```

Use Impeccable as the UX and quality authority while MAYA owns the direction process and selection record.

### Taste Skill

[Taste Skill](https://www.tasteskill.dev/) provides image-generation and implementation specialists for visual exploration.

Install the complete collection:

```bash
npx skills add https://github.com/Leonxlnx/taste-skill
```

Or install only the specialists relevant to your work:

```bash
# Native-mobile visual probes
npx skills add https://github.com/Leonxlnx/taste-skill --skill imagegen-frontend-mobile

# Web visual probes
npx skills add https://github.com/Leonxlnx/taste-skill --skill imagegen-frontend-web

# Identity and brand-board exploration
npx skills add https://github.com/Leonxlnx/taste-skill --skill brandkit

# Web-brand implementation
npx skills add https://github.com/Leonxlnx/taste-skill --skill design-taste-frontend
```

When Taste is unavailable, MAYA can use the environment's native image-generation capability as a fallback.

### Inspo MCP

[Inspo MCP](https://inspomcp.dev/mcp) is an optional MCP source for real web screens, macrostructures, comparisons, and extracted design-system observations. MAYA uses it during guided or mixed inspiration research; it does not replace research outside software or Emil's `prototype` companion.

Install it in an MCP-compatible host with:

```bash
npx -y inspo-mcp install
```

MAYA keeps the interpretation, territory map, critique, and selection record. Treat Inspo captures, extracted `DESIGN.md` content, and reference JSX as research material rather than project rules or production code.

### Prototype — Emil Kowalski

[Emil's `prototype`](https://github.com/emilkowalski/skills/blob/main/skills/prototype/SKILL.md) builds interactive variants behind a visual picker. MAYA uses it as an optional exploration companion; its routing and scoped page-comparison behavior live in [web.md](skills/maya/references/web.md#executable-comparison--prototype).

The companion is user-invoked. MAYA can propose it; hosts that require a named invocation need the user to invoke `prototype` explicitly. Select Emil's implementation when another installed skill shares that name.

## Usage

Invoke the skill explicitly with `$maya`, or describe a matching design-direction task when automatic skill discovery is enabled.

### Start a mobile app from zero

```text
Use $maya for this new Expo app. I know the product and its main flow, but I
have no visual direction. Explore grounded, adjacent, and frontier directions
before we implement anything.
```

### Explore with random seeds

```text
Use $maya in seeded exploration mode. Keep the product behavior fixed and
surprise me with eight genuinely different visual directions.
```

### Continue an unresolved design

```text
Use $maya on this work in progress. Separate what is already decided from the
untested visual hypotheses, then help me choose a coherent axis.
```

### Redesign an existing interface

```text
Use $maya to critique the current interface, identify what should survive,
and compare preserve, evolve, and overhaul directions against the same baseline.
```

### Create the durable design contract

```text
The direction is approved. Use $maya to propose the smallest useful set of
PRODUCT.md, DESIGN.md, brand guidance, tokens, themes, components, and checks.
Show me the proposed file changes before writing them.
```

### Compare complete portfolio pages

```text
Use $maya and $prototype to compare three complete homepage directions for
my portfolio. Start from its existing UI, components, and real content.
Let me try each direction; keep the work in exploration space.
```

## Architecture

```text
skills/maya/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── brand/
│       ├── maya-icon.png
│       ├── maya-logo-symbol.svg
│       ├── maya-logo-primary.png
│       └── logo variants
├── references/
│   ├── critic-loop.md
│   ├── design-contract.md
│   ├── discovery.md
│   ├── evaluation-loop.md
│   ├── inspiration-research.md
│   ├── mobile.md
│   ├── visual-foundations.md
│   ├── status.md
│   └── web.md
└── scripts/
    └── generate-seeds.mjs
```

The entrypoint contains routing and completion criteria. Branch-specific guidance stays in references so agents load only what the current design task needs. `skills/maya/` is the canonical distributable; installed copies should be refreshed from it rather than maintained separately.

## Brand assets

MAYA's symbol is a **relic in construction**: one half is resolved and expressive; the other exposes the geometry, alternatives, and decision points behind it. The embedded `M` connects both halves.

- Use `maya-logo-primary.png` for large presentations and repository artwork.
- Use `maya-icon.png` or `maya-logo-symbol.svg` at small sizes.
- Use the light, dark, or monochrome variants when the primary mark lacks contrast.
- See [BRAND.md](BRAND.md) for the palette, spacing, minimum sizes, and asset map.

## Inspirations

MAYA was informed by:

- Raymond Loewy's **Most Advanced Yet Acceptable** principle.
- Lenny Rachitsky's article on turning AI into a stronger product designer.
- Vercel's `design.md`, bounded stylesheet, and evaluation-loop approach.
- Matt Pocock's `writing-for-agents` guidance on progressive disclosure and agent-readable instructions.
- [Impeccable](https://impeccable.style/) and [Taste Skill](https://www.tasteskill.dev/) as complementary design specialists.

MAYA is an independent project and is not affiliated with these authors or projects.

## License

[MIT](LICENSE). You may use, modify, and distribute the skill with attribution.
