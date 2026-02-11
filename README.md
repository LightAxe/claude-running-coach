# Running Training Plans Skill

A Claude AI skill for creating personalized, evidence-based running training plans that balance performance goals with injury prevention.

## Overview

This skill enables Claude to create comprehensive training plans for runners of all levels, from beginners to experienced marathoners. Plans are built around modern sports science research on training load management and injury prevention.

## Key Features

- **Strava Integration**: Optional automatic data import from Strava via MCP server for accurate training history analysis
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

1. **Check for Strava** (optional): Attempts to connect to Strava MCP to automatically pull recent training data
2. **Gather Information**: Uses Strava data or systematically asks about age, experience, recent training, injuries, goals, and availability
3. **Confirm Readiness**: Summarizes information and waits for user confirmation
4. **Assess Risk**: Calculates injury risk score and determines appropriate conservativeness
5. **Calculate Paces**: Determines training zones from recent runs, race times, or conversational pace
6. **Design Progression**: Plans safe weekly increases maintaining ACWR 0.8-1.3
7. **Structure Schedule**: Distributes workouts based on available days and experience
8. **Create Plan**: Generates week-by-week markdown document with detailed daily workouts

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

This skill is provided as-is for use with Claude AI. Feel free to modify and adapt for your own use.

## Version

Current version: 1.2

Last updated: February 2026

## Changelog

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
