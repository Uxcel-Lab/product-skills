![Product Skills banner. [image: banner]](./assets/banner.png)

# Product Skills

![License](https://img.shields.io/badge/license-MIT-blue)
![Skills](https://img.shields.io/badge/skills-59-brightgreen)
![Works with](https://img.shields.io/badge/works%20with-Claude%20%C2%B7%20Cowork%20%C2%B7%20Figma%20Make-black)

**Product Skills** is an open toolkit of UX design and product management skills for AI assistants. Each one changes how an assistant handles a design or product task, so the output follows the judgment a trained practitioner brings: gating decisions on context, leading with prevention, auditing against real standards, and refusing to over-apply best practices.

Each skill is a `SKILL.md` file: a focused set of decision rules distilled from the [Uxcel](https://uxcel.com) learning library, the platform that has spent years documenting and teaching practical UX design and product management craft to more than 500,000 designers, product managers, and teams. This material is not simply generated. It is built and reviewed by working practitioners from leading product companies, then compressed into rules an AI can actually apply.

These skills work with Claude, Cowork, Figma Make, and any tool that loads skill files.

**Who it is for:** UX designers, product managers, and builders shipping with AI who are tired of output that looks plausible but is not actually good.

---

## Examples (before/after)

The fastest way to understand a skill is to see the same prompt answered with and without it. Same model, same request. The skill supplies the framework, the discipline, and the standard.

### Pricing page (UX design)

**Prompt:** *"Design a pricing page for our SaaS product."*

![Pricing page, default vs. with the pricing skill. [image: pricing-before-after]](./assets/pricing-before-after.png)

Default output stacks every plan with equal weight and vague calls to action. With [`ux/screens/pricing`](./ux/screens/pricing/SKILL.md), plans are ordered to guide the choice, the call-to-action hierarchy is clear, and manipulative patterns are gated out.

### Usability review (UX design)

**Prompt:** *"Review this checkout screen for usability issues."*

![Usability review, default vs. with the heuristics audit. [image: heuristics-before-after]](./assets/heuristics-before-after.png)

Default gives a flat list of generic tips ("make the CTA clearer"). With [`ux/audits/heuristics`](./ux/audits/heuristics/SKILL.md), every finding names the heuristic it violates, carries a severity rating, and comes with a concrete fix.

### Product spec (product management)

**Prompt:** *"Write a PRD for this feature."*

![Product spec, default vs. with the product-spec skill. [image: product-spec-before-after]](./assets/product-spec-before-after.png)

Default produces a feature wish list. With [`pm/deliverables/product-spec`](./pm/deliverables/product-spec/SKILL.md), the spec anchors to a validated problem, states measurable requirements, and surfaces the risks and assumptions a real reviewer would ask about.

---

## What's inside

**59 skills** across two disciplines:

| Discipline | Skills | Categories |
| --- | --- | --- |
| **[UX Design](./ux)** | 38 | foundations · components · screens · flows · audits · workflows |
| **[Product Management](./pm)** | 21 | foundations · deliverables · processes · audits · workflows |

Browse the [UX design index](./ux/README.md) and [product management index](./pm/README.md) for a one-line description of every skill.

---

## The three kinds of skill

Every skill is one of three kinds, and the kind dictates how it behaves:

- **Generative** skills produce or modify work (a screen, a flow, a PRD). Instead of applying every best practice at once, they *gate*: they establish context, apply the always-true core, then surface context-dependent decisions with trade-offs so you can choose. They live in `foundations`, `components`, `screens`, `flows`, `deliverables`, and `processes`.
- **Evaluative** skills (audits) review existing work against a standard (heuristics, accessibility, spec quality) and return a severity-rated issue list with concrete fixes. They live in `audits`.
- **Orchestrators** (workflows) are the front doors that compose the other two: review an artifact holistically, or build something new from the ground up. They live in `workflows`.

---

## Get started

**Try one skill in 30 seconds.** Copy a single `SKILL.md` (for example `ux/audits/heuristics/SKILL.md`) into your tool's skills directory, or paste its contents into your prompt. Ask your assistant to review or build something, and watch the next response change.

**Install the whole set as a Claude plugin.** This repo doubles as a plugin marketplace, so you can install it straight from GitHub, no directory listing required:

```
/plugin marketplace add Uxcel-Lab/product-skills
/plugin install uxcel@product-skills
```

**Or use [`npx skills`](https://github.com/vercel-labs/skills)** to install into Claude Code, Cursor, Codex, and 60+ other agents straight from GitHub:

```
# browse without installing
npx skills add Uxcel-Lab/product-skills --list

# install everything (or a few by name)
npx skills add Uxcel-Lab/product-skills
npx skills add Uxcel-Lab/product-skills --skill ux-heuristics-audit --skill pm-product-spec
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
│   └── workflows/     design-review, design-from-scratch                      (orchestrators)
└── pm/
    ├── foundations/   problem statement, personas/JTBD, user story
    ├── deliverables/  product spec, roadmap, OKRs, vision/strategy, GTM…
    ├── processes/     discovery, prioritization, experimentation, analytics…
    ├── audits/        spec quality, prioritization rigor, metric validity…    (evaluative)
    └── workflows/     product-review, idea-to-plan                            (orchestrators)
```

Every skill is a directory containing exactly one `SKILL.md`, at `{discipline}/{category}/{skill-name}/SKILL.md`.

---

## Go deeper than the rules

Every skill compresses time-tested, learner-tested craft into decision rules an AI can apply. The [**Uxcel courses**](https://uxcel.com/courses) behind them teach the *why*: the examples, edge cases, and hands-on practice a rule can only point at. This is content created and refined by expert practitioners from top product companies and pressure-tested by hundreds of thousands of learners. Every `SKILL.md` links back to the exact lessons it came from, so the connection is earned, not bolted on.

---

## Contributing

This is a curated toolkit. Feedback and issues are always welcome, fixes to existing skills can go straight to a PR, and new skills are reviewed against a quality bar (open an issue to discuss one first). See [CONTRIBUTING.md](./CONTRIBUTING.md) for the full bar.

⭐ If these skills are useful, **star the repo**. It helps other designers and product managers find them.

## Attribution

Every skill links back to the [Uxcel lessons](https://uxcel.com/lessons) it was built from, in the **Source lessons** section at the bottom of each `SKILL.md`. Those lessons are part of broader [Uxcel courses](https://uxcel.com/courses) if you want to go deeper than a skill encodes.

## License

[MIT](./LICENSE) © Uxcel Lab
