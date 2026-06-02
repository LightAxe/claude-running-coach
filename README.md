# Running Training Plans Skill

A Claude AI skill for creating personalized, evidence-based running training plans that balance performance goals with injury prevention.

## Overview

This skill enables Claude to create comprehensive training plans for runners of all levels, from beginners to experienced marathoners. Plans are built around modern sports science research on training load management and injury prevention.

## Key Features

- **Three Training Profiles**: Choose Conservative (injury prevention focus), Moderate (balanced 80/20), or Performance-Focused (speed priority with higher intensity)
- **Pace Variation for Injury Prevention**: Integrates strides, micro-intervals, and varied workouts to prevent overuse injuries from repetitive strain
- **Strides Integration**: Research-backed 20-30 second bursts improve running economy by 2% with minimal injury risk, included 2-3x/week
- **Flexible Data Import**: Pulls recent training automatically via Strava's native MCP connector (paid Strava), or works from an export/screenshot of any platform (Garmin, Apple Health, Intervals.icu), or a quick conversation
- **Post-Race Planning**: Specialized protocols for experienced runners building to next race after recovery period
- **Personalized Plans**: Customized based on age, experience, injury history, goals, and speed vs. safety preference
- **Injury Prevention**: Uses Acute:Chronic Workload Ratio (ACWR) with single-session spike monitoring
- **Progressive Training**: Safe weekly increases (5-20% depending on profile) with mandatory deload weeks
- **Detailed Workouts**: Daily workout specifications with paces, distances, effort descriptions, and stride explanations
- **Flexible Modifications**: Guidance for missed workouts, injuries, and life disruptions
- **Multiple Race Distances**: Supports 5K, 10K, half marathon, marathon, and general fitness

## Research-Based Principles

- **ACWR Sweet Spot (0.8-1.3)**: Maintains training load in safe range with lowest injury risk (4-5%)
- **Deload Weeks**: Scheduled recovery every 3-4 weeks allows body to adapt
- **One Variable at a Time**: Only changes frequency, duration, OR intensity - never multiple simultaneously
- **80/20 Rule**: 80% of training at easy intensity, 20% at moderate-high intensity
- **Progressive Overload**: Gradual increases based on experience level and chronic training load

## Structure

```
running-training-plans/
├── SKILL.md                          # Main skill instructions
├── scripts/
│   └── calculate_acwr.py            # ACWR calculation utilities
└── references/
    ├── training-profiles.md         # Profile specs, weekly distribution, stride guidance
    ├── training-load-principles.md  # ACWR, progression rates, deload protocols
    ├── pace-calculations.md         # Training zones, workout types, pace adjustments
    ├── injury-risk-assessment.md    # Risk scoring, plan adjustments, warning signs
    ├── data-import.md               # Sourcing recent training data (connector/export/Q&A)
    ├── plan-output-format.md        # Plan document template, formatting, worked example
    └── plan-types.md                # Distance-specific structure (5K/10K/half/marathon)
```

## How It Works

When creating a training plan, Claude follows this process:

1. **Source recent data**: Silently tries Strava's native MCP connector; if it's not available, works from an export/screenshot of any platform or a quick conversation
2. **Gather Information**: Uses imported data where available, and systematically asks about age, experience, recent training, injuries, goals, and training profile preference
3. **Select Training Profile**: Choose Conservative, Moderate, or Performance-Focused based on goals and experience
4. **Confirm Readiness**: Summarizes information and waits for user confirmation
5. **Assess Risk**: Calculates injury risk score and provides guidance if mismatch with chosen profile
6. **Calculate Paces**: Determines training zones from recent runs, race times, or conversational pace
7. **Design Progression**: Plans weekly increases (5-20% based on profile) maintaining appropriate ACWR range
8. **Structure Schedule**: Distributes workouts, strides, and intensity based on profile and available days
9. **Create Plan**: Generates week-by-week markdown document with detailed daily workouts and stride explanations

## Training Profiles

This skill offers three evidence-based training approaches:

### Conservative (Injury Prevention Priority)
- **Best for**: Beginners, injury-prone runners, those over 40, returning from injury
- **Intensity**: 85% easy / 15% hard (true beginners: start 90-100% easy for first 2-3 months)
- **Workouts**: 1 quality session per week
- **Strides**: 2x per week (after initial weeks)
- **ACWR**: 0.8-1.2
- **Progression**: 5-10% max during build weeks (3 weeks up, 1 week down pattern)
- **Speed work**: Week 4-6 for intermediate; week 8-12 for true beginners

### Moderate (Balanced Approach)
- **Best for**: Intermediate runners (1-3 years), injury-free with solid base
- **Intensity**: 80% easy / 20% hard (true 80/20 rule)
- **Workouts**: 1-2 quality sessions per week (build from 1 to 2)
- **Strides**: 3x per week
- **Micro-intervals**: Added for pace variation
- **ACWR**: 0.8-1.3
- **Progression**: 10-15% max during build weeks (3 weeks up, 1 week down)
- **Recovery**: Minimum 24 hours between quality sessions
- **Speed work**: Introduced week 2-3

### Performance-Focused (Speed Priority)
- **Best for**: Experienced runners (3+ years), competitive racers, post-race building
- **Intensity**: 75% easy / 25% hard (polarized early season, pyramidal near racing)
- **Workouts**: 2 quality sessions per week from start
- **Strides**: 3x per week from start
- **ACWR**: 0.8-1.4 (brief controlled spikes only, not sustained)
- **Progression**: 15-20% max during build weeks (still follows 3 up, 1 down)
- **Recovery**: Minimum 48 hours between hard quality sessions
- **Periodization**: Polarized in base phase, pyramidal near race
- **Speed work**: Can start week 1-2
- **⚠️ Higher injury risk**: For experienced runners only. ACWR spikes to 1.4 acceptable for 1-2 weeks only

## Example Use Cases

- "Create a 12-week half marathon training plan for me" (skill will help choose appropriate profile)
- "Build a performance-focused 5K plan to improve my time, I'm an experienced runner"
- "I just ran a marathon 2 weeks ago and want to start training for a fall half marathon" (post-race scenario)
- "Help me safely increase my weekly mileage from 20 to 35 miles with a conservative approach"
- "Create a moderate intensity 10K plan with the 80/20 method, I have a solid base"
- "I missed two weeks of training - how should I adjust my plan?"
- "Create a base-building plan to establish a consistent running habit"

## Installation

This skill is designed for use with Claude AI. To use it:

1. Download the skill package (`running-training-plans.zip`)
2. Upload to Claude via the Skills interface
3. The skill will automatically activate when you ask about running training plans

## Getting Your Training Data

The skill needs a picture of your recent running — roughly the last 4–6 weeks of mileage, frequency, and pace. There are three ways to get there, and a short conversation is often the fastest:

1. **Strava native MCP connector** — As of June 2026, Strava offers an [official MCP connector](https://press.strava.com/articles/strava-launches-mcp-connector) that lets Claude read your training directly. It requires a **paid Strava subscription** and that you've enabled the connector in your Claude settings. The skill detects it automatically and uses it if it's there — no manual setup walkthrough, no API keys.
2. **An export or screenshot from any platform** — Don't have the connector? Share an export or a screenshot of your recent weeks from whatever you use (Strava, Garmin, Apple Health, Intervals.icu). Note that full Strava/Garmin exports are emailed to you and can take hours to arrive, so a screenshot of recent weeks is usually quicker.
3. **Just tell the skill** — A quick Q&A about your recent running is a complete method, not a fallback. When exports are delayed and the connector isn't set up, it's often the fastest path.

If your data isn't available right now (e.g., an export is still pending), the skill can build a **conservative provisional plan** from what you tell it and recalibrate later when real data arrives — or you can wait and build the plan once the export is ready. A conversation is easy to return to.

> **Note on the Strava community server:** Earlier versions of this skill walked you through setting up a self-hosted Strava MCP server with your own API key. Strava's June 2026 API changes require a paid subscription for that path too and restrict third-party intermediaries, so the native connector (for subscribers) plus the export/conversation paths (for everyone) replace it.

### Privacy

- Imported data is only used during the conversation and isn't stored
- Only running activities are analyzed; body-weight data is not pulled or used
- An export or screenshot can contain a fair amount of personal health data — share only what you're comfortable with (a screenshot of recent weeks is plenty)

## Safety Philosophy

This skill prioritizes injury prevention by:

- Conservative progression based on individual risk factors
- Mandatory deload weeks
- Clear guidance on pain and warning signs
- Flexibility for life events
- Emphasis on listening to your body

**Core belief**: Better to arrive at the start line slightly undertrained and healthy than injured.

## Research References

The training principles in this skill are based on current sports science research:

- Acute:Chronic Workload Ratio (ACWR) research from Gabbett et al.
- Training load progression studies from running injury prevention literature
- 80/20 training intensity distribution from endurance training research
- Recovery and adaptation research from exercise physiology

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests with:

- Updated research findings
- Improved training methodologies
- Bug fixes or clarifications
- Additional workout types or training scenarios

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2026 Rob Ogilvie

You are free to use, modify, and distribute this skill, including for commercial purposes, as long as you include the copyright notice and license text in any copies or substantial portions of the work.

## Version

Current version: 2.0

Last updated: June 2026

## Changelog

### v2.0
- **Pivot to Strava's native MCP connector**: Strava launched an official first-party MCP connector (June 1, 2026). The skill now detects it silently and uses it when present — no API app, Client ID/Secret, callback domain, or 10–15 minute setup walkthrough.
- **Removed the self-hosted community-server setup**: Strava's June 2026 API changes require a paid subscription for self-hosted Standard Tier access (new developers immediately; existing by June 30, 2026) and restrict third-party intermediary platforms, removing the old "free" advantage. The native connector (paid Strava) plus export/conversation paths replace it.
- **Data-source-agnostic import**: Works from an export or screenshot of any platform (Strava, Garmin, Apple Health, Intervals.icu), not just Strava. Screenshots of recent weeks are encouraged since full exports are emailed and delayed.
- **Question-based flow elevated**: A short Q&A is now framed as a complete, often-fastest method — the genuine path for non-subscribers and coaches — not a fallback.
- **Provisional plans for pending data**: When an export hasn't arrived yet, the skill offers to build a conservative starter plan now and recalibrate later, or wait — the user chooses.
- **Conservative posture for unverified data**: Question-based and provisional plans default to (don't force) the Conservative profile and start volume at the low end of the stated range.
- **Privacy heads-up**: Brief, non-blocking note that exports/screenshots may contain personal health data.
- New `references/data-import.md` consolidates the data-gathering flow and per-platform details.

### v1.3
- **Three Training Profiles**: Conservative, Moderate, and Performance-Focused options
  - Conservative: 85/15 intensity, 1 workout/week, ACWR 0.8-1.2 (injury prevention priority)
  - Moderate: 80/20 intensity, 1-2 workouts/week, ACWR 0.8-1.3 (balanced approach)
  - Performance-Focused: 75/25 intensity, 2 workouts/week, ACWR 0.8-1.4 (speed priority)
- **Strides Integration**: 2-3x/week with detailed "how-to" explanations in every plan
- **Pace Variation**: Research-based approach to prevent overuse injuries from repetitive strain
- **Micro-Intervals**: Added to Moderate profile for pace variation without excessive fatigue
- **Post-Race Planning**: Specialized protocols for experienced runners after race recovery
- **Single-Session Spike Rule**: Monitor individual run increases (10% max of longest run in 30 days)
- **Polarized Training Option**: Available for Performance-Focused profile
- **Updated Research**: Based on 2024-2025 sports science findings on interval training and injury prevention
- Speed work introduction varies by profile (week 4-6 Conservative, week 2-3 Moderate, week 1-2 Performance)
- Strides shown to improve running economy 2% in 40 days per recent research
- Profile selection guidance based on experience, injury history, and goals

### v1.2
- **Strava Integration**: Added optional Strava MCP server integration
- Automatic training data analysis from Strava activities
- Pulls last 4+ weeks of running data for ACWR calculation
- Automatic pace analysis from recent runs
- Training consistency assessment
- Setup guidance for Strava API connection
- Fallback to manual questions if Strava not available

### v1.1
- Added structured information-gathering process
- Required questions before plan generation
- Confirmation workflow
- Enhanced example dialogue

### v1.0
- Initial release
- Core training plan creation
- ACWR-based progression
- Injury risk assessment
- Pace calculations
