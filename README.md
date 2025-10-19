# Running Training Plans Skill

A Claude AI skill for creating personalized, evidence-based running training plans that balance performance goals with injury prevention.

## Overview

This skill enables Claude to create comprehensive training plans for runners of all levels, from beginners to experienced marathoners. Plans are built around modern sports science research on training load management and injury prevention.

## Key Features

- **Personalized Plans**: Customized based on age, experience, injury history, and goals
- **Injury Prevention**: Uses Acute:Chronic Workload Ratio (ACWR) to keep injury risk low
- **Progressive Training**: Safe weekly increases with mandatory deload weeks every 3-4 weeks
- **Detailed Workouts**: Daily workout specifications with paces, distances, and effort descriptions
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

1. **Gather Information**: Systematically asks about age, experience, recent training, injuries, goals, and availability
2. **Confirm Readiness**: Summarizes information and waits for user confirmation
3. **Assess Risk**: Calculates injury risk score and determines appropriate conservativeness
4. **Calculate Paces**: Determines training zones from race times or conversational pace
5. **Design Progression**: Plans safe weekly increases maintaining ACWR 0.8-1.3
6. **Structure Schedule**: Distributes workouts based on available days and experience
7. **Create Plan**: Generates week-by-week markdown document with detailed daily workouts

## Example Use Cases

- "Create a 12-week half marathon training plan for me"
- "Build a 5K plan to improve my time, running 3 days per week"
- "Help me safely increase my weekly mileage from 20 to 35 miles"
- "I missed two weeks of training - how should I adjust my plan?"
- "Create a base-building plan to establish a consistent running habit"

## Installation

This skill is designed for use with Claude AI. To use it:

1. Download the skill package (`running-training-plans.zip`)
2. Upload to Claude via the Skills interface
3. The skill will automatically activate when you ask about running training plans

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

This skill is provided as-is for use with Claude AI. Feel free to modify and adapt for your own use.

## Version

Current version: 1.1

Last updated: October 2025

## Changelog

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
