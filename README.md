# Product Skills

An open toolkit of **UX and product-management skills** for AI assistants, distilled from [Uxcel](https://uxcel.com) lessons.

Each skill is a `SKILL.md` file — a focused set of decision rules that changes how an AI assistant behaves on a design or PM task. They turn generic, plausible-sounding output into work that follows the same principles a trained designer or PM would apply: gating decisions on context, leading with prevention, auditing against real standards, and refusing to over-apply best practices.

These work with Claude, Cowork, Figma Make, and any tool that loads skill files.

---

## What's inside

**59 skills** across two disciplines:

| Discipline     | Skills | Categories                                                      |
| -------------- | ------ | --------------------------------------------------------------- |
| **[UX](./ux)** | 38     | foundations · components · screens · flows · audits · workflows |
| **[PM](./pm)** | 21     | foundations · deliverables · processes · audits · workflows     |

Browse the [UX index](./ux/README.md) and [PM index](./pm/README.md) for a one-line description of every skill.

---

## The three kinds of skill

Every skill is one of three kinds, and the kind dictates how it behaves:

- **Generative** — produces or modifies work (a screen, a flow, a PRD). These _gate_: they establish context, apply the always-true core, then surface context-dependent decisions with trade-offs instead of blindly applying every best practice. Lives in `foundations`, `components`, `screens`, `flows`, `deliverables`, `processes`.
- **Evaluative (audits)** — review existing work against a standard (heuristics, accessibility, spec quality) and return a severity-rated issue list with concrete fixes. Lives in `audits`.
- **Orchestrators (workflows)** — front doors that compose the other two: review an artifact holistically, or build something new from the ground up. Lives in `workflows`.

The single rule behind every skill: **it must change the assistant's default output.** If a skill only restates what the model already does, it's a course link, not a skill.

---

## Install

**Use any single skill directly** — copy its `SKILL.md` (e.g. `ux/audits/heuristics/SKILL.md`) into your tool's skills directory, or paste its contents into your prompt.

**Or install the whole set as a Claude plugin.** This repo doubles as a plugin marketplace, so you can install it straight from GitHub — no directory listing required:

```
/plugin marketplace add Uxcel-Lab/product-skills
/plugin install uxcel@product-skills
```

---

## Structure

```
product-skills/
├── .claude-plugin/
│   └── plugin.json
├── ux/
│   ├── foundations/   color, typography, layout/spacing/grids, iconography, microcopy
│   ├── components/    buttons, inputs & forms, cards, modals, navigation, tables…
│   ├── screens/       login/signup, pricing, dashboard, settings, empty states…
│   ├── flows/         onboarding, checkout, error recovery, offboarding
│   ├── audits/        heuristics, accessibility, aesthetics, dark patterns…   (evaluative)
│   └── workflows/     design-review, design-from-scratch                       (orchestrators)
└── pm/
    ├── foundations/   problem statement, personas/JTBD, user story
    ├── deliverables/  product spec, roadmap, OKRs, vision/strategy, GTM…
    ├── processes/     discovery, prioritization, experimentation, analytics…
    ├── audits/        spec quality, prioritization rigor, metric validity…     (evaluative)
    └── workflows/     product-review, idea-to-plan                             (orchestrators)
```

Every skill is a directory containing exactly one `SKILL.md`, at `{discipline}/{category}/{skill-name}/SKILL.md`.

---

## Contributing

This is a curated toolkit. Feedback and issues are always welcome, fixes to existing skills can go straight to a PR, and new skills are reviewed against a quality bar — open an issue to discuss one first. See [CONTRIBUTING.md](./CONTRIBUTING.md) for the full bar.

## Attribution

Every skill links back to the [Uxcel](https://uxcel.com) lessons it was built from — see the **Source lessons** section at the bottom of each `SKILL.md`.

## License

[MIT](./LICENSE) © Uxcel Lab
