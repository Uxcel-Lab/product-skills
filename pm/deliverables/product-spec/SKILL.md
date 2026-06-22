---
name: pm-product-spec
description: Write a product requirements document (PRD) or spec anchored to a validated problem, with measurable requirements and surfaced risks — or review an existing one. Trigger when asked to write a PRD, product spec, user stories, technical requirements, or to review/critique an existing spec document.
license: MIT
metadata:
  author: uxcel
  version: "1.0.0"
---

# Product Spec / PRD Writer Skill


## How this skill behaves (read first)

Claude's default already produces a *plausible-looking* PRD on request — which is exactly the problem. The default tends to: invent requirements before the problem is pinned down, write vague targets ("fast", "user-friendly"), skip dependencies and assumptions, and phrase user stories as engineering tasks. A document that looks complete but is built on an unvalidated problem and untestable requirements is worse than no document, because teams build from it.

So this skill is **generative but gated**, and it enforces quality rather than just filling a template:

1. **Gate on the problem first.** Don't draft requirements until there's a clear, fact-based problem statement. If the user hasn't supplied one, build it with them — or flag that the spec rests on unverified assumptions.
2. **Write the right document.** PRD and spec are different artifacts for different audiences and moments — pick deliberately (see below).
3. **Enforce measurability.** Every requirement must be testable; every user story must express value; every assumption must be flagged as a risk.
4. **Self-audit before delivering** (built-in review pass — see final section).

---

## Step 0 — PRD or spec? Write the right one.

These are different documents; writing the wrong one (or blurring them) is a common failure.

| | **PRD (Product Requirements Document)** | **Product Specification** |
|---|---|---|
| Answers | *What* should the product do, and *why* | *How* it will be designed and built |
| Audience | Broad — PMs, execs, marketing, stakeholders | Technical — engineers, designers, QA |
| When | Early, during discovery/planning | After requirements are agreed |
| Flexibility | Adaptable as insights emerge | Stable once development starts; changes cause rework |
| Contains | Vision, goals, personas, user stories, success metrics | Components, behavior, performance targets, dependencies |

Rule of thumb: requirements **set priorities** (what/why); specs **define dependencies and behavior** (how). If the user is still deciding what to build, they need a PRD. If what-to-build is settled and they need a build blueprint, they need a spec. Confirm which before writing.

---

## The problem gate (do this before any requirements)

A specification built on a poorly-defined problem fails no matter how well-written. A complete problem statement has **three parts**:

- **Problem** — the gap between the current and desired state (facts, not assumptions).
- **Consequences** — the negative outcomes for users or the business.
- **Goal** — the improvement to achieve, *not* the solution.

Enforce these checks before proceeding:

- **Causes, not symptoms.** "Low retention" is a symptom; "onboarding doesn't convey core value" is a cause. Push past the symptom.
- **Specific, not broad.** "Improve the user experience" is not a problem — it produces an endless task list. Narrow it.
- **Facts, not assumptions.** "The process is inefficient" / "users are unhappy" hide the real cause and measurable impact. Tie to evidence (feedback, data) where possible.
- **Clarity test.** Could someone in design, eng, or leadership understand *what* the problem is, *who* it affects, and *why* it matters without extra explanation? If not, refine.

If the user can't supply evidence, proceed but **explicitly mark the problem as an unvalidated assumption** to be tested — don't paper over it.

---

## Spec / PRD structure

Build from this structure (adapt to the doc type from Step 0). Every section traces back to the problem statement.

1. **Summary** — what it is, why it exists now, who it serves.
2. **Problem statement** — from the gate above.
3. **Scope — in and out.** State explicitly what is *excluded*, not just included. Unstated scope is where misalignment hides.
4. **Personas & user stories** — who, and what they need (format below).
5. **Requirements** — what the product must do, each testable (rules below).
6. **Acceptance criteria** — what "done" looks like for each requirement.
7. **Dependencies, constraints & assumptions (DCA)** — what could derail delivery (below).
8. **Success metrics** — how the outcome will be measured, in specific terms.

---

## Requirement quality — make every requirement testable

Replace subjective descriptions with measurable targets. This is the highest-leverage thing the skill does.

- ❌ "The app should load quickly." → ✅ "The dashboard loads within 2 seconds on a standard mobile network."
- ❌ "Make checkout user-friendly." → ✅ "A returning user can complete checkout in ≤ 3 steps without re-entering saved details."
- Describe **complete workflows**, not isolated features.
- A requirement is testable when QA (or anyone) could write a pass/fail check from it without asking what you meant.

---

## User stories — express value, not tasks

Use the formula: **"As a [persona], I want to [action], so that [benefit]."** Tie each story to a real persona (goals + frustrations from research), so the backlog stays rooted in authentic needs.

Apply **INVEST** — Independent, Negotiable, Valuable, Estimable, Small, Testable.

**Flag weak stories** — these describe tasks, not user value, and should be rewritten:

- ❌ "Add login feature" / "Improve dashboard performance" (tasks, no who/why)
- ✅ "As a returning user, I want to log in quickly so I can access my saved data."

---

## Dependencies, Constraints & Assumptions (DCA)

The section the default most often omits — and where delivery actually breaks.

- **Dependencies** — one step enabling the next. Distinguish **internal** (within the team — manageable via planning) from **external** (legal approval, third-party vendors, other teams — higher risk). Map the chain so a single delay's downstream impact is visible.
- **Constraints** — the boundaries: budget, deadlines, legacy tech, legal/compliance. Name them early to avoid unrealistic plans.
- **Assumptions** — what the team believes but hasn't confirmed. **Turn each assumption into a measurable check** with an owner. An untested assumption left sitting is a hidden risk; surface it as one.

Early-warning signals to call out if reviewing an existing spec: vague ownership of a critical dependency, inconsistent timelines across teams, assumptions still unverified after several sprints.

---

## Self-audit before delivering (built-in review pass)

Before presenting the document, run this quality check on your own output — this is what separates the skill from a template fill:

- [ ] Every requirement is **measurable/testable** (no "fast", "intuitive", "user-friendly" left undefined).
- [ ] Every user story expresses **value** (has a who + why), passes INVEST, and isn't a disguised task.
- [ ] **Scope explicitly lists what's out**, not only what's in.
- [ ] Each requirement **traces back to the problem statement**.
- [ ] **Assumptions are flagged as risks** with a way to test them; dependencies note internal vs. external.
- [ ] Success is defined in **specific, measurable** terms.

Then hand the document to the audit lenses. These are **candidate** lenses — posture per `docs/orchestration-policy.md`, or route the whole artifact through `pm-product-review`. Here **`assumption-rigor` is the always-relevant lens (auto-runs)**; the others are **offered**, tied to what the artifact actually contains. If the user invoked this skill for one specific thing, respect that scope.

> In a full idea-to-plan build, this spec is the **final rung** of `pm-idea-to-plan` — it should arrive already resting on a framed problem, discovery evidence, and a tested riskiest assumption, and stay proportionate to them. A spec produced before those rungs is a polished PRD on an unvalidated bet, which is the exact failure that front door exists to prevent.

> Hand-offs name each lens by its installable skill `name`. Invoke one only if that skill is installed; if it isn't, this skill's own self-audit checklist above already carries these rules — proceed without it rather than blocking.

- **`pm-assumption-rigor-audit`** *(auto-runs)* — when the spec rests on material unvalidated assumptions: whether the riskiest one is being tested, with a right-fidelity method and pre-set success criteria, rather than left as a belief dressed up as a fact.
- **`pm-spec-quality-audit`** *(offer — if it writes a spec)* — the full document review: testability of every requirement, complete flows vs. happy paths, scope exclusions, DCA completeness, validation evidence, layer-mixing, audience fit.
- **`pm-okr-metric-validity-audit`** *(offer — if it names success metrics)* — the success metrics specifically: vanity metrics, unfalsifiable targets, outputs disguised as outcomes, and gameable metrics missing guardrails.

Report anything that can't be satisfied (e.g. "Success metric for requirement 3 is undefined — needs a target") rather than silently filling it with plausible-sounding text. Note that a spec is a **living document**: requirements should be revalidated after sprint reviews and releases.

---

## Common do/don't patterns

| ❌ Don't | ✅ Do |
|---|---|
| Draft requirements before the problem is clear | Gate on a problem statement (problem + consequence + goal) first |
| Describe symptoms ("low retention") | Frame the underlying cause |
| "Improve the user experience" | Narrow to a specific, evidence-based problem |
| "The page should be fast" | "Loads within 2 seconds on a standard mobile network" |
| "Add login feature" | "As a returning user, I want to log in quickly so I can access my saved data" |
| List only what's in scope | State what's explicitly out of scope too |
| Omit dependencies and assumptions | Include a DCA section; turn assumptions into testable checks with owners |
| Blur PRD and spec | Decide which doc the moment/audience needs |
| Present a polished-but-vague doc | Self-audit; flag undefined targets instead of inventing them |
| Treat the spec as final | Treat it as living — revalidate after reviews and releases |

---

## Source lessons (Uxcel)

- [Understanding Product Specifications](https://uxcel.com/lessons/understanding-product-specifications-734)
- [Product Specs vs. Product Requirements Documents](https://uxcel.com/lessons/product-specs-vs-product-requirements-documents-679)
- [Defining Problems for Effective Specifications](https://uxcel.com/lessons/defining-problems-for-effective-specifications-501)
- [Dependencies, Constraints, and Assumptions](https://uxcel.com/lessons/dependencies-constraints-and-assumptions-327)
- [Reviewing and Validating Specifications](https://uxcel.com/lessons/reviewing-and-validating-specifications-295)
- [Understanding Users and Framing User Stories](https://uxcel.com/lessons/understanding-users-and-framing-user-stories-802)
