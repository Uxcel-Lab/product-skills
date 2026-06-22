<!-- Keep PRs focused — ideally one skill per PR. -->

## What does this change?

<!-- Brief summary. Link any related issue, e.g. Closes #12. -->

## Type

- [ ] Fix/improvement to an existing skill
- [ ] New skill (please open a `[new-skill]` issue first)
- [ ] Docs / repo housekeeping

## Checklist

- [ ] The change makes the skill produce **better output than the assistant's default** — it doesn't just restate what the model already does.
- [ ] It's written as **decision rules / if-then triggers with good and bad examples**, not a knowledge dump.
- [ ] Correct behavior for its kind — generative skills **gate** context-dependent decisions; audits return severity-rated findings with fixes.
- [ ] Source lessons are cited and the links resolve.
- [ ] Structure intact: one `SKILL.md` at `{discipline}/{category}/{skill-name}/` with valid frontmatter (`name`, `description`, `license`, `metadata.author`, `metadata.version`).
