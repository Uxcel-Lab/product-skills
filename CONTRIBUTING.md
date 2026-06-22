# Contributing

Thanks for your interest in improving this toolkit. It's a curated set of UX and PM skills distilled from [Uxcel lessons](https://uxcel.com/lessons), and we care more about a small set of skills that genuinely change an assistant's output than a large pile of mediocre ones. Contributions are welcome within that bar.

There are three ways to contribute, in order of friction.

## 1. Feedback & issues — always open

The most valuable contribution is telling us where a skill falls short. Open an issue for:

- A skill that produces wrong, generic, or low-quality output on a real task (include the prompt and what you got).
- Missing nuance — a case the skill should handle but doesn't.
- A new skill you'd find useful (see lane 3 before writing one).

## 2. Fixes to existing skills — PRs welcome

Small, reviewable improvements are easy to accept:

- Sharper or clearer decision rules.
- Better good/bad examples.
- Corrected or updated source-lesson links.
- Typos and formatting.

Keep each PR focused on one skill where possible.

## 3. New skills — open an issue first

New skills are reviewed against a quality bar, not merged just for existing. Please open an issue to discuss before writing one, so we can confirm it clears the bar and isn't already covered.

A skill is accepted only if it meets all of the following:

- **It changes the assistant's default output.** It must be corrective (the model is subtly wrong by default), structuring (the model knows it but doesn't apply it systematically), or enriching (it adds nuance the model lacks). A skill that only restates what the model already does is a course link, not a skill — pure facts, definitions, and glossaries don't qualify.
- **It's written as decision rules, not a knowledge dump.** If-then triggers, gating logic, and concrete good/bad examples — not an essay.
- **It behaves correctly for its kind.** Generative skills (foundations, components, screens, flows, deliverables, processes) must *gate*: establish context, apply the always-true core, then surface context-dependent decisions with trade-offs instead of applying every best practice blindly. Evaluative skills (`audits`) return a prioritized, severity-rated issue list with concrete fixes.
- **It cites its sources.** Content should trace to citable source lessons rather than invented claims. End the skill with a **Source lessons** section linking each one.
- **It follows the repo structure.** One `SKILL.md` per directory at `{discipline}/{category}/{skill-name}/SKILL.md`, opening with valid YAML frontmatter (`name`, `description`, `license`, `metadata.author`, `metadata.version`). Look at an existing skill such as `ux/audits/heuristics` or `ux/screens/login-signup` as a reference.

## Licensing

This project is [MIT](./LICENSE) licensed. By submitting a contribution, you agree it may be distributed under the same license.
