[← Back to all Product Skills](../README.md)

# UX Design Skills

Everything a UX designer touches, from color tokens and button states to whole screens, multi-step flows, and full design reviews. **38 skills**, grouped by category. Each links to its `SKILL.md`.

---

## Types of skills

There are three kinds, and each one is used a little differently.

**Generative skills** (foundations, components, screens, flows) produce or shape work. Instead of applying every best practice at once, they *gate*: they establish context first, apply the always-true core, then surface the context-dependent choices with trade-offs and let you decide. Reach for these when you are creating or changing something. Answer their questions rather than rushing past them, because that is where the quality comes from.

**Evaluative skills** (audits) review existing work against a standard and hand back a prioritized, severity-rated list of issues, each with a concrete fix. Reach for these whenever you have something to check (a screen, a flow, a component) and want to know what is wrong and what matters most. You can run several at once for a fuller picture.

**Orchestrators** (workflows) are the front doors. They compose the other two for you: review an artifact holistically, or build something new from the ground up. Reach for these when you would rather not pick individual skills yourself.

> **New here?** Try [`audits/heuristics`](./audits/heuristics/SKILL.md) first. Drop it in, then ask your assistant to *"review this screen for usability issues"* and compare the result to what you would normally get. To build from zero, [`workflows/design-from-scratch`](./workflows/design-from-scratch/SKILL.md) composes the rest in the right order.

---

## Foundations

The cross-cutting visual and writing systems every screen rests on.

*Try: "Build a color palette and tokens for a finance dashboard, including dark mode."*

| Skill | Purpose |
|---|---|
| [color](./foundations/color/SKILL.md) | Build a color palette and system: hue, harmony, neutrals, semantic colors, tonal scales, tokens, dark mode. |
| [typography](./foundations/typography/SKILL.md) | Typeface selection and pairing, type scale, hierarchy, and readability settings. |
| [layout-spacing-grids](./foundations/layout-spacing-grids/SKILL.md) | Disciplined spacing, sizing, and grids on a single base unit, plus spatial hierarchy and alignment. |
| [iconography](./foundations/iconography/SKILL.md) | Choose and design icons that are understood, not decorative: one style, legible, labeled. |
| [microcopy](./foundations/microcopy/SKILL.md) | Write clear, concise, on-voice interface copy for labels, errors, empty states, tooltips, and confirmations. |

## Components

Individual UI building blocks: picking the right one and applying state, label, and styling rules.

*Try: "Which button type should this destructive action use, and how should its states behave?"*

| Skill | Purpose |
|---|---|
| [buttons](./components/buttons/SKILL.md) | Pick the right button type for an action's importance, plus sizing, labels, states, FABs, and icon-only. |
| [cards](./components/cards/SKILL.md) | One-topic, scannable cards with clear hierarchy and the right container style. |
| [inputs-and-forms](./components/inputs-and-forms/SKILL.md) | Field selection, labels, layout, validation, error states, and submission. |
| [loaders-and-progress](./components/loaders-and-progress/SKILL.md) | Match feedback (spinner, skeleton, bar, tracker) to wait duration, and manage perceived performance. |
| [menus](./components/menus/SKILL.md) | Pick the right menu type and apply item ordering, grouping, labeling, and states. |
| [modals-and-dialogs](./components/modals-and-dialogs/SKILL.md) | Gate when interrupting users is justified, then apply dismissal, title/button, and focus rules. |
| [navigation](./components/navigation/SKILL.md) | Match the nav pattern to the information architecture, with wayfinding, headers, breadcrumbs, and pagination. |
| [notifications-and-toasts](./components/notifications-and-toasts/SKILL.md) | Pick the right notification type for urgency, and respect attention with timing, frequency, and opt-outs. |
| [search](./components/search/SKILL.md) | Search input, auto-suggest, results, filtering and sorting, and zero-results recovery. |
| [selection-controls](./components/selection-controls/SKILL.md) | Pick the right control (checkbox, radio, toggle, slider, and more) and apply labeling and state rules. |
| [tables](./components/tables/SKILL.md) | Scannable tables and lists: alignment, sorting and filtering, row interactions, and the right list type. |
| [tooltips](./components/tooltips/SKILL.md) | Decide when a tooltip clarifies versus crutches unclear design, plus placement, styling, and brevity. |

## Screens

Whole screens with established conversion and usability patterns.

*Try: "Design a settings screen for a mobile app without overwhelming the user."*

| Skill | Purpose |
|---|---|
| [login-signup](./screens/login-signup/SKILL.md) | Auth screens: separate pages, minimal fields, inline validation, and full password reset. Gates social and 2FA. |
| [pricing](./screens/pricing/SKILL.md) | Pricing pages: plan ordering, CTA clarity, and ethics guardrails. Gates freemium, sliders, and PPP. |
| [dashboard](./screens/dashboard/SKILL.md) | Which metrics earn a place, how to organize them, and which chart fits each. |
| [settings](./screens/settings/SKILL.md) | Organize many options without overwhelm, and choose the save model (autosave versus explicit save, revert). |
| [landing-page](./screens/landing-page/SKILL.md) | Focused, conversion-oriented page around a single goal: headline, value prop, CTA, and trust. |
| [empty-states](./screens/empty-states/SKILL.md) | First-use, cleared, no-results, and 404 screens that explain and guide the next action. |
| [activity-feed](./screens/activity-feed/SKILL.md) | Scannable update streams: chronological versus ranked, aggregation, timestamps, and refresh status. |
| [contact-support](./screens/contact-support/SKILL.md) | Help center, FAQ, contact methods, live chat, and point-of-error help. Leads with self-service. |

## Flows

Multi-step journeys.

*Try: "Design an onboarding flow that gets a new user to first value fast."*

| Skill | Purpose |
|---|---|
| [onboarding](./flows/onboarding/SKILL.md) | First-run experience that gets users to value fast. Gates method, progressive profiling, and tours. |
| [checkout-payment](./flows/checkout-payment/SKILL.md) | The path from ready to buy to order confirmed: guest checkout, cost transparency, and confirmation. |
| [error-recovery](./flows/error-recovery/SKILL.md) | Prevent, surface, and recover from errors, and never dead-end. Confirm versus undo, and validation timing. |
| [offboarding](./flows/offboarding/SKILL.md) | Cancel, unsubscribe, and delete flows: an easy, respectful exit with retention levers that avoid manipulation. |

## Audits _(evaluative)_

Review existing work against a standard and return a prioritized, severity-rated issue list with fixes.

*Try: "Audit this dashboard against Nielsen's heuristics."*

| Skill | Purpose |
|---|---|
| [heuristics](./audits/heuristics/SKILL.md) | Usability audit against Nielsen's 10 heuristics. |
| [accessibility](./audits/accessibility/SKILL.md) | WCAG 2.1 AA audit. Each finding cites the criterion, severity, and a fix. |
| [aesthetics](./audits/aesthetics/SKILL.md) | Visual-quality audit of hierarchy, contrast, spacing, and alignment. Catches overdesign and clutter. |
| [dark-patterns](./audits/dark-patterns/SKILL.md) | Find deceptive patterns in UI, flows, or copy. Names each one and gives an honest-design fix. |
| [information-architecture](./audits/information-architecture/SKILL.md) | Audit sitemaps, nav trees, categories, and labels for findability and scent. |
| [microcopy](./audits/microcopy/SKILL.md) | Audit interface copy for clarity, tone, and consistency, with concrete rewrites. |
| [mobile-responsiveness](./audits/mobile-responsiveness/SKILL.md) | Audit viewport reflow, touch targets, reachability, gestures, and mobile readability. |

## Workflows _(orchestrators)_

*Try: "Review this design end to end and tell me what to fix first."*

| Skill | Purpose |
|---|---|
| [design-review](./workflows/design-review/SKILL.md) | Holistic review. Auto-runs the always-relevant lenses, offers the rest, and returns one prioritized report. |
| [design-from-scratch](./workflows/design-from-scratch/SKILL.md) | Build from zero. Composes the generative ladder (foundations, components, screens, flows), then reviews. |

---

All skills are derived from [Uxcel lessons](https://uxcel.com/lessons), part of the broader [Uxcel courses](https://uxcel.com/courses). See the **Source lessons** section in each `SKILL.md`.
