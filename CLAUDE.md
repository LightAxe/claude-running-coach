# CLAUDE.md

## Project Overview

This is a Claude skill for creating personalized, evidence-based running training plans. It is not a traditional software project — the primary deliverable is `SKILL.md`, a skill instruction file uploaded to Claude. Reference documents and a Python utility support the skill's content.

## File Structure

```
SKILL.md                          # Main skill instructions — what Claude reads at runtime
scripts/
  calculate_acwr.py               # Python utility for ACWR calculations (standalone, importable)
references/
  training-profiles.md            # Profile specs, weekly distribution matrices, stride guidance, research basis
  training-load-principles.md     # ACWR, progression rates, deload protocols
  pace-calculations.md            # Training zones, workout types, pace adjustments
  injury-risk-assessment.md       # Risk scoring, plan adjustments, warning signs
README.md                         # Project documentation for GitHub
```

## Making Changes

- Work directly on `main` — no branching strategy for this project
- Auto-commit all changes after testing
- Every tested, pushed change triggers a version bump (see Versioning below)
- Future contributors will typically work via forks

## Versioning

- Bump the version number on every tested and pushed content change
- There is no strict major/minor policy — use judgment based on scope of change
- Update the version number and changelog in **both** `SKILL.md` and `README.md`
- Version format: `X.Y` (e.g., `1.3`)

## Style & Content Conventions

- Match `SKILL.md` content and structure to Claude Skills best practices (reference the Skill Builder skill)
- Reference docs use plain markdown with headers, bullet lists, and bold for key terms
- Tone in `SKILL.md` is warm but evidence-based; casual recommendations, not clinical
- Avoid IMPORTANT/CRITICAL/ALWAYS/NEVER directive language — explain the *why* behind instructions instead
- Keep `SKILL.md` under 500 lines; move detail into `references/` with clear pointers from the main file
- The description frontmatter is the primary triggering mechanism — keep it focused on planning intent, not casual running conversation

## Testing

Currently manual: upload `SKILL.md` to Claude and validate behavior against example use cases in `README.md`.

**Planned (not yet implemented):**
- Automated testing for skill behavior
- Linting and formatting for `calculate_acwr.py` (target: `ruff` or `black` + `flake8`)
- Packaging script to generate distribution zip from repo contents

## Open Architecture Questions

- **SKILL.md structure**: Consider whether to split `SKILL.md` into modular files as it grows. No sections are currently off-limits for editing, but this is worth revisiting.
- **Versioning policy**: Define clearer major vs. minor bump criteria as the skill matures.
