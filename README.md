# Running Training Plans Skill

A Claude AI skill for creating personalized, evidence-based running training plans that balance performance goals with injury prevention.

## Overview

This skill enables Claude to create comprehensive training plans for runners of all levels, from beginners to experienced marathoners. Plans are built around modern sports science research on training load management and injury prevention.

## Key Features

- **Three Training Profiles**: Choose Conservative (injury prevention focus), Moderate (balanced 80/20), or Performance-Focused (speed priority with higher intensity)
- **Pace Variation for Injury Prevention**: Integrates strides, micro-intervals, and varied workouts to prevent overuse injuries from repetitive strain
- **Strides Integration**: Research-backed 20-30 second bursts improve running economy by 2% with minimal injury risk, included 2-3x/week
- **Strava Integration**: Optional automatic data import from Strava via MCP server for accurate training history analysis
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
    ├── training-load-principles.md  # ACWR, progression rates, deload protocols
    ├── pace-calculations.md         # Training zones, workout types, pace adjustments
    └── injury-risk-assessment.md    # Risk scoring, plan adjustments, warning signs
```

## How It Works

When creating a training plan, Claude follows this process:

1. **Check for Strava** (optional): Attempts to connect to Strava MCP to automatically pull recent training data
2. **Gather Information**: Uses Strava data or systematically asks about age, experience, recent training, injuries, goals, and training profile preference
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

## Strava Integration (Optional)

**This skill is fully functional without Strava.** Manual questions provide complete, comprehensive training plan creation.

Strava integration is an optional enhancement that can make data gathering faster by automatically pulling your recent training history. It's purely a convenience feature - perfect for individual runners who track their runs on Strava. Coaches creating plans for others or runners who don't use Strava will use the standard question-based approach, which is equally complete.

### Benefits

- Automatically pulls your last 4+ weeks of running data
- Calculates accurate weekly mileage and training frequency
- Identifies your typical training paces from recent runs
- Assesses training consistency and patterns
- No need to manually estimate your recent training volume

### Setup

To use Strava integration, you'll need to set up the [Strava MCP server](https://github.com/r-huijts/strava-mcp):

1. Create a free Strava API application at [strava.com/settings/api](https://www.strava.com/settings/api)
2. Set the authorization callback domain to "localhost"
3. Configure the Strava MCP server with your Client ID and Secret
4. Authorize the connection when prompted

Setup takes about 10-15 minutes. **Strava setup is completely optional** - the skill works perfectly well without it. If you're creating plans for others (coaching) or prefer not to connect Strava, simply use the standard question-based approach.

### Privacy

- Your Strava data is only accessed when you explicitly request it
- Only running activities are analyzed (no other activity types)
- Weight and other personal data are not pulled or used
- All data processing happens during the conversation and is not stored

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

Current version: 1.3

Last updated: February 2026

## Changelog

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
