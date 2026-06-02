# Plan Output Format

How the final training-plan document should be structured, what each week and run includes, and an end-to-end example of the information-gathering conversation that precedes it.

## Contents
- [Document template](#document-template)
- [What each week heading includes](#what-each-week-heading-includes)
- [What each run includes](#what-each-run-includes)
- [Key principles](#key-principles)
- [Formatting checklist](#formatting-checklist)
- [Example interaction flow](#example-interaction-flow)

## Document template

List runs for each week without assigning them to specific days. Runners have different schedules and commitments — a plan that locks in specific days feels rigid and is harder to stick to when life gets in the way.

Generate a markdown document with this structure:

```markdown
# [Distance] Training Plan for [Name/User]

## Plan Overview
- **Goal**: [Race distance and date, or fitness goal]
- **Current training**: [X days/week, Y miles/week]
- **Plan structure**: [X days per week, Y weeks total]
- **Training profile**: [Conservative/Moderate/Performance-Focused]
- **Start date**: [Date if provided, or "Start when ready"]
- **Approach rationale**: [Explain why this profile was chosen based on experience, goals, injury history, etc.]
- **Intensity split**: [85/15, 80/20, or 75/25 depending on profile]
- **Target ACWR range**: [0.8-1.2, 0.8-1.3, or 0.8-1.4]

[If Performance-Focused profile selected]:
**⚠️ Performance-Focused Notice**: This plan prioritizes speed development and accepts higher injury risk. It includes 2 quality sessions per week and faster progression. Monitor your body closely and don't hesitate to dial back if you experience pain or excessive fatigue.

[If post-race scenario]:
**Post-Race Building**: This plan includes a [1-2] week recovery period following your recent race, then builds into [profile] training to prepare for your next goal.

[If provisional plan built from unverified data]:
**Provisional Plan**: This is built from estimates rather than measured data, so it starts a little conservative. When your export arrives or you connect Strava, come back and I'll recalibrate with real numbers.

## Training Paces
[List each zone with effort description and estimated pace range]

**Example:**
- **Easy/Conversational**: 9:30-10:00 min/mile - Should be able to hold full conversation
- **Tempo/Threshold**: 8:15-8:30 min/mile - Comfortably hard, can speak short phrases
- **Interval/5K Pace**: 7:45-8:00 min/mile - Hard effort, only 1-2 words at a time
- **Long Run**: 9:30-10:00 min/mile early, can progress to 9:00-9:15 in final miles
- **Strides**: 85-90% effort, roughly mile race pace, 20-30 seconds

## What Are Strides?

Strides are short 20-30 second bursts at 85-90% effort that improve running economy and form with minimal injury risk. Research shows they improve running economy by 2% in just 40 days.

**How to do strides**:
1. Perform AFTER an easy run (not when tired from hard workouts)
2. Find a flat, clear section of road or track
3. Gradually accelerate for 20-30 seconds up to 85-90% effort (not a full sprint)
4. Focus on smooth, controlled form with quick turnover
5. Walk back to start for full recovery (60-90 seconds)
6. Repeat 4-8 times (work up gradually)
7. Total time: 5-10 minutes

Think of it as "practicing fast running" without the fatigue of a full workout.

[If Moderate profile includes micro-intervals]:
## Micro-Intervals (Pace Variation)

Some easy runs include micro-intervals to prevent repetitive strain injury. These are NOT hard workouts:
- During the middle miles of an easy run
- 30-60 seconds at steady pace (moderate, not hard)
- 2-3 minutes easy recovery
- Repeat 4-6 times
- Purpose: Vary your pace to reduce repetitive stress

## How to Use This Plan
- Schedule runs on days that work for your calendar
- Ideally space runs throughout the week
- Keep hard workouts separated by at least 48 hours — muscles need time to repair and adapt after quality sessions, and stacking them prevents the recovery that makes training effective
- [If 2 workouts/week]: Space quality sessions evenly (e.g., Tuesday/Saturday)
- Rest days are flexible - take them when needed
- [If frequency is increasing from current]: We're building from X to Y days per week gradually
- **Single-session rule**: Don't increase any single run by more than 10% of your longest run in the last 30 days

## Week 1: October 26 - November 1 | Base Building | ACWR: 1.15
**Weekly Volume**: 18 miles
**Focus**: Establishing consistent easy mileage

**Runs this week (4 total):**

1. **Easy Run**: 4 miles at easy pace (9:30-10:00 min/mile)
   - Focus on conversational pace, building aerobic base

2. **Easy Run**: 5 miles at easy pace (9:30-10:00 min/mile)
   - Stay relaxed and comfortable

3. **Easy Run with Strides**: 4 miles easy + 4 strides
   - After the easy miles, do 4 × 20 seconds at 90% effort with full recovery between
   - Strides improve form and leg turnover

4. **Long Run**: 5 miles at easy pace (9:30-10:00 min/mile)
   - Can be slightly slower if needed, focus on time on feet

## Week 2: November 2-8 | Build | ACWR: 1.18
**Weekly Volume**: 20 miles
**Focus**: Gradual volume increase

**Runs this week (4 total):**

1. **Easy Run**: 5 miles at easy pace
   - Keep it conversational

2. **Easy Run**: 5 miles at easy pace
   - Focus on consistent effort

3. **Easy Run with Strides**: 4 miles easy + 6 strides
   - 6 × 20 seconds at ~90% effort

4. **Long Run**: 6 miles at easy pace
   - Building endurance, stay patient with pace

[Continue for all weeks...]

## Week 4: November 16-22 | Deload/Recovery | ACWR: 0.88
**Weekly Volume**: 14 miles (30% reduction from peak)
**Focus**: Recovery and adaptation

**Runs this week (4 total):**

1. **Recovery Run**: 3 miles very easy
   - Extra easy today, focus on feeling good

2. **Easy Run**: 4 miles at easy pace
   - Comfortable effort

3. **Easy Run**: 4 miles at easy pace
   - Enjoy the lower volume week

4. **Long Run**: 5 miles at easy pace
   - Shorter than usual, allow body to recover

**Note**: This is a scheduled recovery week. The reduced volume allows your body to absorb the previous weeks' training and adapt. You should feel fresh and ready to build again next week.

[Continue pattern...]
```

## What each week heading includes

1. Week number
2. Date range (calculate from start date or race date working backward)
3. Week theme/type (Base Building, Build, Peak, Deload, Taper, etc.)
4. ACWR value (calculate using the script or estimated based on progression)

## What each run includes

1. Run type (Easy Run, Long Run, Tempo Run, Interval Workout, Recovery Run, etc.)
2. Distance or duration
3. Pace with range and effort description
4. Brief instruction on execution or focus
5. Purpose or specific notes when relevant

## Key principles

- List runs as numbered items, not assigned to specific days
- Include total number of runs for the week
- Provide flexibility for runners to schedule themselves
- Include notes about spacing hard workouts when relevant
- Mark deload weeks clearly with reduced volume
- Calculate and show ACWR for each week
- Include date ranges to help with planning

## Formatting checklist

Always create training plans as **markdown documents** with:
- Clear week-by-week structure with date ranges
- **Training profile** (Conservative/Moderate/Performance-Focused) clearly stated in overview
- **"What Are Strides?" section** explaining how to do them (many runners don't know)
- **Micro-intervals section** if Moderate profile
- ACWR calculated and displayed for each week
- Week themes (Base Building, Build, Peak, Deload, Taper, etc.)
- Weekly volume and focus
- Runs listed without specific day assignments (numbered list)
- Detailed workout descriptions with paces and instructions
- Strides included 2-3x/week in individual run descriptions
- Explanatory headers and guidance sections
- Conversational tone with specific instructions

**Key formatting elements**:
- Training profile and rationale in Plan Overview
- ACWR target range based on profile (0.8-1.2, 0.8-1.3, or 0.8-1.4)
- Intensity split noted (85/15, 80/20, 75/25)
- Warning if Performance-Focused profile selected
- Week heading: `## Week X: [Date Range] | [Theme] | ACWR: X.XX`
- Weekly volume and focus in bold
- Runs as numbered list with type, distance, pace, and details
- Include "How to Use This Plan" section explaining flexibility and 48-hour spacing for hard workouts
- Note single-session spike rule (10% of longest run in 30 days)
- For strides: "After your 5-mile easy run, do 6 strides: 20 seconds at 85-90% effort, walk back for full recovery"

Plans should be easily printable, savable, and modifiable. Runners schedule their own days based on their calendar and preferences. Use headers, bold text for emphasis, and clear structure for scannability.

## Example interaction flow

**User**: "I want to train for a half marathon in 12 weeks. I just ran a 10K in 55 minutes."

**Claude**: "That's a great goal! A half marathon in 12 weeks is definitely doable. I'd like to ask you several questions to create the best training plan for your specific situation. Let's start with a few basics.

First, how old are you?"

**User**: "I'm 32"

**Claude**: "Thanks! How long have you been running consistently?"

**User**: "About 18 months"

**Claude**: "Great. What has your training looked like recently? Can you tell me about your typical week over the last month - how many days per week and roughly how many miles?"

**User**: "I've been running 3-4 times per week, probably around 15-20 miles per week"

**Claude**: "Perfect. How many days per week would you like to run during this training plan?"

**User**: "I'd like to bump it up to 4 days consistently"

**Claude**: "Great - we'll build from 3-4 days up to a consistent 4 days. Have you had any injuries in the last 6 months, or do you have any current pain or discomfort?"

**User**: "No injuries, feeling good"

**Claude**: "Excellent! What's your goal for this training?"

**User**: "I want to run a half marathon in 12 weeks"

**Claude**: "Perfect. Do you have a specific race date, or is this a general 12-week timeframe?"

**User**: "I have a race on February 15th"

**Claude**: "Great! And you mentioned earlier you just ran a 10K in 55 minutes - when was that race?"

**User**: "Two weeks ago"

**Claude**: "Perfect. Are you looking for a conservative approach focused on staying injury-free, or are you comfortable pushing a bit harder with a more aggressive progression?"

**User**: "I'd prefer to stay conservative and just finish strong"

**Claude**: "Smart approach! Let me summarize what I have:
- Age: 32
- Experience: 18 months of consistent running
- Recent training: 15-20 miles/week over 3-4 days
- Plan frequency: 4 days per week consistently
- Injury history: None currently, feeling good
- Recent performance: 10K in 55 minutes (2 weeks ago)
- Goal: Half marathon on February 15th (12 weeks), finish strong
- Approach: Conservative, injury prevention focused

Do you have any other information you'd like me to know before I create your training plan? Any scheduling constraints, previous injuries I should know about, or other considerations?"

**User**: "Nope, that covers it!"

**Claude**: "Perfect! Let me create your personalized training plan. This will take a moment as I analyze the best approach for your situation..."

[Then proceed with Steps 2-7: Read references, assess risk, calculate paces, design progression, create plan]
