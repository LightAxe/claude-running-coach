# TODO

## Skill Builder Best Practices Review

- [x] **Restructure SKILL.md for size** (1,070 → 883 lines; target ~400)
  - [x] Move training profile specs out of Step 4 (duplicated from Step 1)
  - [x] Move Strava setup instructions to README (they're user-facing docs, not skill instructions)
  - [x] Delete "Critical Reminders" section (every point already stated earlier in the file)
  - [x] Move profile detail (ACWR ranges, intensity splits, schedule tables) to a new `references/training-profiles.md`
  - [x] Update Step 1, Step 4, and Step 5 to reference the new profile file instead of restating inline

- [x] **Replace CRITICAL/IMPORTANT/ALWAYS/NEVER directives with "why"-based reasoning**
  - [x] Audit all instances of bolded IMPORTANT/CRITICAL and all-caps directives
  - [x] Rewrite each to explain the reasoning rather than issue a command

- [x] **Sharpen the description for better triggering**
  - [x] Add a "use this whenever..." push to the frontmatter description
  - [ ] Run description optimization via Skill Builder eval loop (after other changes)

- [x] **Add tables of contents to large reference files**
  - [x] `references/injury-risk-assessment.md` (362 lines)
  - [x] `references/pace-calculations.md` (313 lines)

## Tooling & Automation

- [ ] **Add Python linting** for `scripts/calculate_acwr.py`
  - [ ] Set up `ruff` (or `black` + `flake8`)
  - [ ] Add to git pre-commit hook or CI

- [ ] **Build packaging script** to generate distribution zip from repo contents

- [ ] **Add automated testing** for skill behavior
  - [ ] Define test prompts (Skill Builder eval format)
  - [ ] Set up eval runner using Skill Builder tooling

## Future Discussions

- [ ] **SKILL.md modularization** — as the skill grows, consider splitting into domain-specific files (e.g., separate files per training profile) with SKILL.md as an orchestrator
- [ ] **Versioning policy** — define clearer criteria for major vs. minor bumps
