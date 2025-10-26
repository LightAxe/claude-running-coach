---
name: running-training-plans
description: Create personalized running training plans, modify existing plans, analyze running performance, and provide injury prevention guidance. Use when users ask about training schedules, building a running plan, preparing for races (5K, 10K, half marathon, marathon), increasing running distance or speed, or managing training load to prevent injuries. Supports creating week-by-week plans with detailed daily workouts, calculating training paces, assessing injury risk, and adjusting plans for missed workouts or life events.
---

# Running Training Plans

This skill helps create evidence-based running training plans that balance performance goals with injury prevention. Plans are built around managing the acute:chronic workload ratio (ACWR) to minimize injury risk while safely progressing toward race or fitness goals.

## Overview

This skill creates comprehensive, week-by-week training plans that include:
- Daily workout details with specific paces and effort levels
- Progressive training load management (ACWR <1.5)
- Scheduled deload/recovery weeks every 3-4 weeks
- Injury risk assessment and mitigation strategies
- Flexibility for life events and missed workouts
- Both distance race preparation and general fitness building

**Core principle**: Manage acute vs chronic training load to stay in the "sweet spot" (ACWR 0.8-1.3) while safely building fitness.

**Important workflow**: This skill uses a structured information-gathering process. Always ask the required questions (age, running experience, recent training, injury history, goal, availability) BEFORE creating a plan. Wait for the user to confirm they're ready before generating the training plan. Do not skip this step.

## Process for Creating Training Plans

### Step 1: Gather Essential Information

**IMPORTANT**: Always gather required information BEFORE creating a training plan. Do not generate the plan until all required information is collected and the user confirms they're ready.

#### Required Information (Must Ask)

Ask these questions systematically, waiting for responses before proceeding:

1. **Age**: "How old are you?"
   - Critical for injury risk assessment and recovery considerations

2. **Running experience**: "How long have you been running consistently?"
   - <1 year = Novice (requires most conservative approach)
   - 1-3 years = Intermediate
   - 3+ years = Experienced

3. **Recent training**: "What has your training looked like recently?"
   - How many days per week running (last 4 weeks)
   - Weekly mileage or total time per week
   - Typical run distances
   - Consistency level

4. **Desired frequency**: "How many days per week would you like to run during this training plan?"
   - Must ask this explicitly
   - Compare to current frequency - if increasing days/week, this counts as one variable change
   - Days per week will determine number of runs in weekly plan

5. **Injury history**: "Have you had any injuries in the last 6 months? Any current pain or discomfort?"
   - Specific injuries and affected areas
   - Whether fully healed
   - Any chronic/recurring issues
   - Current pain level (if any)

6. **Goal**: "What's your training goal?"
   - Race distance (5K, 10K, half marathon, marathon, other)
   - Target date or timeframe
   - Goal type (finish, specific time, PR)

#### Additional Helpful Information (Ask as Follow-ups)

7. **Current fitness indicator**:
   - Recent race time (with date and distance), OR
   - Typical conversational/easy pace, OR
   - Just use weekly mileage from question 3

8. **Risk tolerance**: "Are you looking for a conservative approach focused on injury prevention, or are you comfortable with a more aggressive training progression?"

9. **Other factors** (if relevant):
   - Prior athletic background
   - Current life stress, sleep quality
   - Any scheduling constraints (work travel, etc.)
   - Any other constraints or considerations

#### Confirmation Before Plan Generation

After gathering the required information:

1. **Summarize** what you've learned about the runner
2. **Ask explicitly**: "Do you have any other information you'd like me to know before I create your training plan?"
3. **Wait for user response**
4. **Only after they indicate they're ready**, proceed with: "Great! Let me create your personalized training plan. This will take a moment as I analyze the best approach for your situation..."

**Example dialogue flow:**

User: "I want to train for a half marathon"

Claude: "Excellent! I'd like to ask you a few questions to create the best training plan for you. First, how old are you?"

User: "35"

Claude: "Thanks! How long have you been running consistently?"

User: "About 2 years"

Claude: "Great. What has your training looked like recently - how many miles per week or days per week have you been running over the last month or so?"

[Continue through required questions...]

Claude: "Perfect! Let me summarize what I know:
- Age: 35
- Experience: 2 years of consistent running
- Recent training: 15-20 miles/week, 3-4 days
- Injury history: IT band issue 8 months ago, fully healed
- Goal: Half marathon in 14 weeks, finish comfortably
- Availability: 4 days per week

Do you have any other information you'd like me to know before I create your training plan?"

User: "No, I think that covers it"

Claude: "Perfect! Let me create your personalized training plan. This will take a moment as I analyze the best approach for your situation..."

[Then proceed with Steps 2-7]

**Critical**: Do NOT skip the information gathering phase. Do NOT generate a plan until you have confirmed the runner is ready. Missing key information (especially age, experience, injuries, and recent training) leads to inappropriate or potentially dangerous plans.

### Step 2: Calculate Training Paces

Read `references/pace-calculations.md` to:
- Determine training zones from race times or conversational pace
- Calculate specific paces for each workout type
- Understand effort-based descriptions for each zone

**Output format for paces**: Always include effort description + estimated pace range + purpose.

Example: "Easy pace: conversational, should feel comfortable. Based on your 55-minute 10K, aim for 9:30-10:00 min/mile, but go slower if needed to stay conversational."

### Step 3: Assess Injury Risk

Read `references/injury-risk-assessment.md` to:
- Calculate injury risk score from gathered information
- Determine risk category (Low, Moderate, High)
- Identify appropriate plan adjustments

Key considerations:
- Recent injury to same area within 6 months = highest risk
- Low chronic training load + aggressive goals = high risk
- Age 40+ with limited running history = higher risk
- Multiple risk factors compound

**Adjust plan conservativeness based on risk level.**

### Step 4: Design Training Progression

Read `references/training-load-principles.md` to understand:
- Safe weekly progression rates (5-25% depending on experience and chronic load)
- ACWR targets (0.8-1.3 sweet spot)
- Deload week frequency and structure
- 80/20 intensity distribution

**Plan structure**:

**For Low Risk runners:**
- 10-15% weekly increases
- Deload every 3-4 weeks
- Can introduce workouts week 2-3

**For Moderate Risk runners:**
- 5-10% weekly increases  
- Deload every 3 weeks
- Introduce workouts after 2-3 weeks

**For High Risk runners:**
- 5% weekly increases maximum
- Deload every 2-3 weeks
- Delay speed work 4-6 weeks
- Extended base building phase

**Critical rule**: Progress only ONE variable at a time (frequency, duration, OR intensity - never multiple simultaneously).

### Step 5: Determine Weekly Run Distribution

Based on the runner's desired frequency, determine the types and distribution of runs each week:

**3 days/week** (beginner or time-limited):
- 2 easy runs
- 1 long run
- Add strides to one easy run after base phase
- Introduce one workout (tempo or intervals) only after solid base established

**4 days/week** (intermediate):
- 2 easy runs
- 1 workout (tempo or intervals - introduced after base phase)
- 1 long run
- Can add strides to easy runs

**5 days/week** (intermediate to advanced):
- 2-3 easy runs (one may be recovery run)
- 1-2 workouts (different stimulus - e.g., tempo + intervals)
- 1 long run
- Strides added to easy runs regularly

**6-7 days/week** (advanced):
- 3-4 easy/recovery runs
- 2 quality sessions per week (tempo, intervals, etc.)
- 1 long run
- May include double-run days for high volume

**Workout distribution principles**:
- Hard workouts need at least one easy day between them
- Long run is typically the longest single effort of the week
- Easy runs make up 60-80% of weekly volume (80/20 rule)
- Strides (short 20-30 sec bursts) can be added to easy runs without counting as "intensity"
- Recovery runs (when doing 6+ days/week) are shorter and easier than regular easy runs

**Note**: Since plans don't assign specific days, remind runners to space hard efforts appropriately when scheduling their own week.

### Step 6: Create Week-by-Week Plan

**IMPORTANT**: Plans should list runs for each week WITHOUT assigning them to specific days. Let runners schedule runs based on their own calendar and preferences.

Generate a markdown document with this structure:

```markdown
# [Distance] Training Plan for [Name/User]

## Plan Overview
- Goal: [Race distance and date, or fitness goal]
- Current training: [X days/week, Y miles/week]
- Plan structure: [X days per week, Y weeks total]
- Start date: [Date if provided, or "Start when ready"]
- Approach: [Conservative/Moderate/Standard] based on [risk factors]

## Training Paces
[List each zone with effort description and estimated pace range]

**Example:**
- **Easy/Conversational**: 9:30-10:00 min/mile - Should be able to hold full conversation
- **Tempo/Threshold**: 8:15-8:30 min/mile - Comfortably hard, can speak short phrases
- **Interval/5K Pace**: 7:45-8:00 min/mile - Hard effort, only 1-2 words at a time
- **Long Run**: 9:30-10:00 min/mile early, can progress to 9:00-9:15 in final miles

## How to Use This Plan
- Schedule runs on days that work for your calendar
- Ideally space runs throughout the week (avoid back-to-back hard efforts)
- If you need to shuffle runs, keep hard workouts separated by at least one easy day
- Rest days are flexible - take them when needed
- [If frequency is increasing from current]: We're building from X to Y days per week gradually

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

**For each week's heading, include**:
1. Week number
2. Date range (calculate from start date or race date working backward)
3. Week theme/type (Base Building, Build, Peak, Deload, Taper, etc.)
4. ACWR value (calculate using the script or estimated based on progression)

**For each run, include**:
1. Run type (Easy Run, Long Run, Tempo Run, Interval Workout, Recovery Run, etc.)
2. Distance or duration
3. Pace with range and effort description
4. Brief instruction on execution or focus
5. Purpose or specific notes when relevant

**Key principles**:
- List runs as numbered items, not assigned to specific days
- Include total number of runs for the week
- Provide flexibility for runners to schedule themselves
- Include notes about spacing hard workouts when relevant
- Mark deload weeks clearly with reduced volume
- Calculate and show ACWR for each week
- Include date ranges to help with planning

### Step 7: Include Guidance and Modifications

At the end of the plan, include:

**Listening to Your Body**:
- Pain scale guidelines (when to modify vs stop)
- Signs to take extra rest
- When to repeat a week vs progress

**Modifying for Life Events**:
- How to adjust for missed workouts
- What to do after illness or travel
- Prioritizing key workouts when time-limited

**Deload Week Guidelines**:
- Reduce volume by 30-40%
- Maintain some intensity
- Use for recovery and adaptation

**Pre-Race Taper** (if applicable):
- How to reduce volume while maintaining intensity
- Typical 2-3 week taper structure

## Tools and Resources

### Calculate ACWR

Use the ACWR calculation script when:
- Analyzing current training load progression
- Determining safe progression for next week  
- Evaluating whether a proposed plan maintains safe ratios

```bash
python scripts/calculate_acwr.py
```

The script provides functions to:
- Calculate current ACWR from recent weekly loads
- Assess injury risk based on ACWR value
- Plan next week's load targeting specific ACWR
- Generate safe progression sequences

**Use this proactively** when creating plans with multiple build weeks to verify ACWR stays in sweet spot.

### Reference Documents

**Read these references as needed:**

1. **training-load-principles.md**: 
   - When designing overall plan progression
   - Understanding ACWR targets and deload timing
   - Determining safe weekly increase percentages
   - Learning 80/20 intensity distribution

2. **pace-calculations.md**:
   - When calculating training paces from race times
   - Understanding different training zones
   - Learning workout type definitions
   - Adjusting paces for conditions (heat, terrain, etc.)

3. **injury-risk-assessment.md**:
   - When assessing individual injury risk
   - Determining how conservative to be
   - Understanding age and injury history impacts
   - Creating return-from-injury protocols

**When to read**: Read the relevant reference(s) at the beginning of creating each new plan. Sections are comprehensive, so you'll have all needed context.

## Plan Modification Scenarios

### Missed Workout

**Single missed easy run**: Skip it, continue with plan
**Missed workout day**: Try to fit it in later in week if possible; if not, continue with plan
**Missed week**: Resume at previous week's volume, don't try to "catch up"

### Injury or Pain

**Minor soreness (<2/10)**: Continue, monitor
**Moderate pain (3-5/10) improving**: Easy runs only until resolved
**Persistent or worsening pain**: Stop running, seek medical advice, use return-from-injury protocol

### Life Disruption (Travel, Work, Stress)

**Known in advance**: Plan around it - build into schedule
**Unexpected**: Prioritize sleep and recovery, reduce volume 30-50%, maintain some running
**Extended (>1 week)**: Plan recovery week upon return, don't resume at full volume

### Progress Too Easy or Too Hard

**Too easy**: Can increase by 5-10% if ACWR allows, but conservative is okay
**Too hard**: Reduce volume 10-20%, repeat previous week, or add extra recovery day

## Creating Specific Plan Types

### Race-Specific Plans

**5K Plans** (8-12 weeks):
- Higher intensity (intervals, tempo)
- Moderate volume
- Focus on speed and VO2max work

**10K Plans** (10-14 weeks):
- Balance of volume and intensity
- Threshold/tempo work emphasized
- Long runs build to 10-13 miles

**Half Marathon Plans** (12-16 weeks):
- Volume emphasis with sustained efforts
- Long runs build to 13-15 miles
- Tempo runs and long runs with uptempo finish

**Marathon Plans** (16-20 weeks):
- High volume emphasis
- Long runs build to 18-22 miles
- Marathon pace practice crucial
- Extended taper (2-3 weeks)

### Distance Progression Plans

When progressing from shorter to longer distances (e.g., 5K to 10K, 10K to half):

1. **Establish base** at current distance (4-6 weeks)
2. **Build volume gradually** toward new distance (8-12 weeks)
3. **Add race-specific work** (4-6 weeks)
4. **Taper and race** (2-3 weeks)

**Timeline**: Allow minimum 12 weeks for single distance jump, longer for larger jumps.

### General Fitness Plans

For non-race goals (build base, lose weight, general fitness):

- Emphasize consistent easy running (80%+)
- Gradual volume increases
- Limited intensity (strides, easy fartleks)
- Focus on enjoyment and sustainability
- Can introduce variety for interest

## Communication Style

**Be supportive and realistic**:
- Acknowledge their goal while ensuring safety
- Explain reasoning for conservative approaches when needed
- Provide flexibility and alternatives
- Empower runners to listen to their body

**Be specific**:
- Give exact paces with ranges
- Include detailed workout instructions  
- Explain the "why" behind workouts
- Provide actionable guidance

**Be practical**:
- Plans should fit their life, not vice versa
- Built-in flexibility for missed workouts
- Clear guidance on decision-making
- Realistic about time commitments

## Example Interaction Flow

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

## Critical Reminders

- **ALWAYS gather required information FIRST** - Ask about age, running experience, recent training, injury history, goal, and availability. Wait for user confirmation before generating plan
- **ACWR 0.8-1.3 is the target** - stay in sweet spot for injury prevention
- **Deload weeks are non-negotiable** - plan them every 3-4 weeks
- **Progress ONE variable at a time** - never increase frequency, duration, AND intensity simultaneously
- **Easy days should be EASY** - 80% of volume at low intensity
- **Individual risk factors matter** - adjust conservativeness based on injury history, age, chronic load
- **Flexibility is essential** - real life disrupts training; plans should accommodate this
- **Safety over speed** - better to arrive at start line undertrained and healthy than injured

## Output Format

Always create training plans as **markdown documents** with:
- Clear week-by-week structure with date ranges
- ACWR calculated and displayed for each week
- Week themes (Base Building, Build, Peak, Deload, Taper, etc.)
- Weekly volume and focus
- Runs listed without specific day assignments (numbered list)
- Detailed workout descriptions with paces and instructions
- Explanatory headers and guidance sections
- Conversational tone with specific instructions

**Key formatting elements**:
- Week heading: `## Week X: [Date Range] | [Theme] | ACWR: X.XX`
- Weekly volume and focus in bold
- Runs as numbered list with type, distance, pace, and details
- Include "How to Use This Plan" section explaining flexibility
- Note when building frequency (if increasing days/week from current)

Plans should be easily printable, savable, and modifiable. Runners schedule their own days based on their calendar and preferences. Use headers, bold text for emphasis, and clear structure for scannability.
