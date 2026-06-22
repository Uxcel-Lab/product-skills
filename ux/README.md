# UX Skills

38 skills for designing and reviewing user interfaces — grouped by category. Each links to its `SKILL.md`.

**Kinds:** _foundations / components / screens / flows_ are **generative** (they gate decisions on context); _audits_ are **evaluative** (they review work and return severity-rated fixes); _workflows_ are **orchestrators** (they compose the others).

---

## Foundations

The cross-cutting visual and writing systems every screen rests on.

| Skill | Purpose |
|---|---|
| [color](./foundations/color/SKILL.md) | Build a color palette and system — hue, harmony, neutrals, semantic colors, tonal scales, tokens, dark mode. |
| [typography](./foundations/typography/SKILL.md) | Typeface selection and pairing, type scale, hierarchy, and readability settings. |
| [layout-spacing-grids](./foundations/layout-spacing-grids/SKILL.md) | Disciplined spacing, sizing, and grids on a single base unit; spatial hierarchy and alignment. |
| [iconography](./foundations/iconography/SKILL.md) | Choose and design icons that are understood, not decorative — one style, legible, labeled. |
| [microcopy](./foundations/microcopy/SKILL.md) | Write clear, concise, on-voice interface copy — labels, errors, empty states, tooltips, confirmations. |

## Components

Individual UI building blocks — picking the right one and applying state/label/styling rules.

| Skill | Purpose |
|---|---|
| [buttons](./components/buttons/SKILL.md) | Pick the right button type for an action's importance; sizing, labels, states, FABs, icon-only. |
| [cards](./components/cards/SKILL.md) | One-topic, scannable cards with clear hierarchy and the right container style. |
| [inputs-and-forms](./components/inputs-and-forms/SKILL.md) | Field selection, labels, layout, validation, error states, and submission. |
| [loaders-and-progress](./components/loaders-and-progress/SKILL.md) | Match feedback (spinner, skeleton, bar, tracker) to wait duration; manage perceived performance. |
| [menus](./components/menus/SKILL.md) | Pick the right menu type and apply item ordering, grouping, labeling, and states. |
| [modals-and-dialogs](./components/modals-and-dialogs/SKILL.md) | Gate when interrupting users is justified, then apply dismissal, title/button, and focus rules. |
| [navigation](./components/navigation/SKILL.md) | Match the nav pattern to the information architecture; wayfinding, headers, breadcrumbs, pagination. |
| [notifications-and-toasts](./components/notifications-and-toasts/SKILL.md) | Pick the right notification type for urgency; respect attention with timing, frequency, opt-outs. |
| [search](./components/search/SKILL.md) | Search input, auto-suggest, results, filtering/sorting, and zero-results recovery. |
| [selection-controls](./components/selection-controls/SKILL.md) | Pick the right control (checkbox, radio, toggle, slider…) and apply labeling and state rules. |
| [tables](./components/tables/SKILL.md) | Scannable tables and lists — alignment, sorting/filtering, row interactions, the right list type. |
| [tooltips](./components/tooltips/SKILL.md) | Decide when a tooltip clarifies vs. crutches unclear design; placement, styling, brevity. |

## Screens

Whole screens with established conversion and usability patterns.

| Skill | Purpose |
|---|---|
| [login-signup](./screens/login-signup/SKILL.md) | Auth screens — separate pages, minimal fields, inline validation, full password-reset; gates social/2FA. |
| [pricing](./screens/pricing/SKILL.md) | Pricing pages — plan ordering, CTA clarity, ethics guardrails; gates freemium, sliders, PPP. |
| [dashboard](./screens/dashboard/SKILL.md) | Which metrics earn a place, how to organize them, and which chart fits each. |
| [settings](./screens/settings/SKILL.md) | Organize many options without overwhelm; the save model (autosave vs. explicit save, revert). |
| [landing-page](./screens/landing-page/SKILL.md) | Focused, conversion-oriented page around a single goal — headline, value prop, CTA, trust. |
| [empty-states](./screens/empty-states/SKILL.md) | First-use, cleared, no-results, and 404 screens that explain and guide the next action. |
| [activity-feed](./screens/activity-feed/SKILL.md) | Scannable update streams — chronological vs. ranked, aggregation, timestamps, refresh status. |
| [contact-support](./screens/contact-support/SKILL.md) | Help center, FAQ, contact methods, live chat, point-of-error help; leads with self-service. |

## Flows

Multi-step journeys.

| Skill | Purpose |
|---|---|
| [onboarding](./flows/onboarding/SKILL.md) | First-run experience that gets users to value fast; gates method, progressive profiling, tours. |
| [checkout-payment](./flows/checkout-payment/SKILL.md) | The path from "ready to buy" to "order confirmed" — guest checkout, cost transparency, confirmation. |
| [error-recovery](./flows/error-recovery/SKILL.md) | Prevent, surface, and recover from errors; never dead-end. Confirm vs. undo, validation timing. |
| [offboarding](./flows/offboarding/SKILL.md) | Cancel/unsubscribe/delete flows — easy and respectful exit; retention levers without manipulation. |

## Audits _(evaluative)_

Review existing work against a standard and return a prioritized, severity-rated issue list with fixes.

| Skill | Purpose |
|---|---|
| [heuristics](./audits/heuristics/SKILL.md) | Usability audit against Nielsen's 10 heuristics. |
| [accessibility](./audits/accessibility/SKILL.md) | WCAG 2.1 AA audit — each finding cites the criterion, severity, and a fix. |
| [aesthetics](./audits/aesthetics/SKILL.md) | Visual-quality audit — hierarchy, contrast, spacing, alignment; catches overdesign and clutter. |
| [dark-patterns](./audits/dark-patterns/SKILL.md) | Find deceptive patterns in UI, flows, or copy; name each and give an honest-design fix. |
| [information-architecture](./audits/information-architecture/SKILL.md) | Audit sitemaps, nav trees, categories, and labels for findability and scent. |
| [microcopy](./audits/microcopy/SKILL.md) | Audit interface copy for clarity, tone, and consistency with concrete rewrites. |
| [mobile-responsiveness](./audits/mobile-responsiveness/SKILL.md) | Audit viewport reflow, touch targets, reachability, gestures, and mobile readability. |

## Workflows _(orchestrators)_

| Skill | Purpose |
|---|---|
| [design-review](./workflows/design-review/SKILL.md) | Holistic review — auto-runs the always-relevant lenses, offers the rest, returns one prioritized report. |
| [design-from-scratch](./workflows/design-from-scratch/SKILL.md) | Build from zero — composes the generative ladder (foundations → components → screens → flows), then reviews. |

---

All skills are derived from [Uxcel lessons](https://uxcel.com/lessons), part of the broader [Uxcel courses](https://uxcel.com/courses); see the **Source lessons** section in each `SKILL.md`.
