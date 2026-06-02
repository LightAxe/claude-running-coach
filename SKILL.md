---
name: running-training-plans
description: Create personalized, evidence-based running training plans for any race distance (5K to marathon) or general fitness goal. Use this skill whenever someone wants to prepare for a race, structure their running, or safely build mileage — including when they phrase it as a question ("how do I train for my first half marathon?") rather than an explicit plan request. Covers weekly schedules, training paces, load management (ACWR), injury risk assessment, and adjusting plans for missed workouts or life events.
---

<!--
Copyright (c) 2026 Rob Ogilvie
Licensed under the MIT License - see LICENSE file for details
Version: 2.0 (see README.md for changelog)
-->

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

## Getting the Runner's Data

Before building a plan, the skill needs a picture of someone's recent running: roughly the last 4–6 weeks of mileage, frequency, and pace, plus how long they've been running. There are three ways to get there — Strava's native MCP connector, an export/screenshot from any platform, or simply asking — and a short conversation is often the fastest, since most platform exports arrive by email later rather than in the moment. An import is a convenience, not a requirement.

Step 1 below walks through the flow; `references/data-import.md` has the per-platform details and the export-pending case.

## Training Intensity Profiles

Three profiles are available. See `references/training-profiles.md` for full specs, weekly distribution matrices, stride guidance, and research basis.

| Profile | Best for | ACWR target | Intensity | Progression |
|---------|----------|-------------|-----------|-------------|
| **Conservative** | Beginners, injury-prone, 40+, returning | 0.8–1.2 | 85/15 easy/hard | 5–10%/week |
| **Moderate** | Intermediate (1–3 years), solid base | 0.8–1.3 | 80/20 | 10–15%/week |
| **Performance-Focused** ⚠️ | Experienced (3+ years), competitive | 0.8–1.4 | 75/25 or polarized | 15–20%/week |

Default to Conservative for most runners. Performance-Focused carries significantly higher injury risk and is for experienced runners with a strong training history only.

## Process for Creating Training Plans

### Step 1: Gather Essential Information

Collect all required information and confirm with the runner before generating a plan. The questions below are designed to surface the factors that most affect plan safety and appropriateness — skipping them risks producing a plan that looks reasonable but is wrong for this specific person.

#### Preliminary: Source the Runner's Recent Data

Read `references/data-import.md` for the full flow and per-platform details. The short version:

1. **Coaching for someone else?** Skip the data-source step entirely — you'll be asking about *their* runner — and go straight to "Required Information" below.

2. **Planning for themselves?** Silently try the Strava MCP connector first. If its tools respond, pull recent runs (filter to runs; include road/trail/treadmill/virtual) plus athlete stats, summarize, and confirm with the user before planning. Don't pull body-weight data.

3. **If the connector doesn't respond**, ask how they track their runs. Most Strava users won't have the connector set up yet (it needs a paid subscription *and* prior setup in Claude), so this is the common path. From here:
   - **They have a file or screenshot handy** → have them share it; parse the recent ~4–6 weeks and confirm.
   - **They'd need to export** → exports from Strava/Garmin usually arrive by email later, so offer a choice: build a **conservative provisional plan now** and return to recalibrate when the export arrives, **or** wait and build once the data is ready. Either is fine — a conversation is easy to return to. A screenshot of recent weeks is often faster than a full export.
   - **They'd rather just talk** → gather the details in conversation. This is a complete method, not a fallback.

**Confirming imported data**: when data comes from the connector or a file, summarize what you found (weekly mileage and runs for the last ~4 weeks, average mileage/frequency, typical easy pace, consistency) and ask "Does this look accurate? Have you been running elsewhere I should know about?" If volume looks very low (e.g., <5 runs last month), present it honestly and ask whether they've been running untracked or whether this is the real picture — if it's real, treat them as a novice/returning runner with higher injury risk.

**Planning from unverified data**: for question-based or provisional plans, self-reported numbers aren't backed by data and people tend to round up — so **default to (don't force) the Conservative profile and start volume at the low end of their stated range**. Mention briefly that real data would sharpen the plan, and if an export is pending or they connect Strava later, invite them back to update it — as an option, not a requirement.

**Privacy note**: if someone shares an export or screenshot, give a brief, non-blocking heads-up that it may contain personal health data — they should share only what they're comfortable with, and a screenshot of recent weeks is plenty.

Whatever the source, still ask the things data never provides: age, injury history, current pain, goal, desired frequency, and life context. These are covered in "Required Information" below.

#### Required Information

**This is the primary, complete method for gathering information.** However the recent-training data arrived (connector, file, or conversation), ask these questions systematically. If data was imported, some answers may already be in hand — confirm them rather than re-asking.

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
   - Context: Post-race recovery period? Building after a race?

#### Additional Helpful Information (Ask as Follow-ups)

7. **Current fitness indicator**:
   - Recent race time (with date and distance), OR
   - Typical conversational/easy pace, OR
   - Just use weekly mileage from question 3

8. **Training profile preference**: "Which training approach appeals to you?"
   - **Conservative**: Prioritize injury prevention, arrive healthy (recommended for most)
   - **Moderate**: Balance performance and safety (80/20 rule)
   - **Performance-Focused**: Maximize speed gains, accept higher injury risk (experienced runners only)

   Explain the three profiles and help them choose based on:
   - Experience level
   - Injury history
   - Current fitness base
   - Goals (finish vs. time goal vs. PR)
   - Recent training context (post-race, returning, building base)

   **For experienced runners post-race**: They may be ready for Performance-Focused immediately after recovery period
   **For injury-prone or newer runners**: Strongly recommend Conservative
   **For intermediate with good base**: Moderate is often ideal

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

**Example dialogue flow (Strava connector already set up):**

User: "I want to train for a half marathon"

Claude: [Silently tries the Strava connector; its tools respond]

Claude: "Great goal! I can see you've connected Strava — let me pull your recent running. Based on your data, here's what I see:

**Last 4 weeks:**
- Week 1: 18 miles, 4 runs
- Week 2: 20 miles, 4 runs
- Week 3: 16 miles, 3 runs
- Week 4: 22 miles, 5 runs

**Recent patterns:**
- Average: 19 miles/week over 4 runs/week
- Typical easy pace: 9:45/mile
- Training consistency: Mostly consistent with one lighter week

**Additional context:**
- Year-to-date: 87 runs, 412 total miles
- Running since: January 2024

Does this look accurate? Have you been running elsewhere (different app, no tracking) that I should know about?"

User: "Yes, that's accurate. All my runs are on Strava."

Claude: "Perfect! Now a few things I can't get from your data. First, how old are you?"

User: "35"

Claude: "Thanks! Your Strava history goes back to January 2024 — would you say that's about how long you've been running consistently?"

User: "Actually I ran in college, but took many years off. This is my comeback year."

Claude: "That's helpful context! Have you had any injuries in the last 6 months, or do you have any current pain or discomfort?"

[Continue with remaining questions: goal details, desired frequency, etc.]

**Example dialogue flow (no connector — export pending, provisional plan):**

User: "I want to train for a half marathon"

Claude: [Silently tries the Strava connector; nothing responds]

Claude: "Great goal! How do you usually track your runs — Strava, a Garmin/Apple Watch, another app, or not really?"

User: "I use Strava but I don't think I've connected it here."

Claude: "No problem. A couple of options: you can request a Strava export, but it gets emailed to you and can take a few hours — or, honestly quicker, you could send me a screenshot of your last few weeks, or just tell me roughly how you've been running. What works for you? (Heads up: an export can include a fair bit of personal health data, so share only what you're comfortable with — a screenshot of recent weeks is plenty.)"

User: "I'll request the export, but I want to get started now."

Claude: "Let's do this: tell me roughly what your recent training looks like and I'll build you a sensible starter plan now, leaning a little conservative since we're going off estimates. When your export arrives, come back to this chat and I'll recalibrate it with your real numbers. How many days per week have you been running lately, and roughly how many miles?"

User: "About 3-4 days, maybe 15-20 miles."

[Continue with remaining questions; build a provisional plan defaulting to the Conservative profile, starting volume at the low end of the stated range]

**Example dialogue flow (Coaching Use Case):**

User: "I want to create a half marathon training plan for my friend"

Claude: "Excellent! I'd be happy to help you create a training plan for your friend. Let me ask you some questions about their training background and goals. First, how old are they?"

User: "They're 28"

Claude: "Thanks! How long have they been running consistently?"

[Continue with all questions - no data source is offered, since this plan is for someone else]

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

### Step 2: Calculate Training Paces

Read `references/pace-calculations.md` to:
- Determine training zones from race times or conversational pace
- Calculate specific paces for each workout type
- Understand effort-based descriptions for each zone

**Output format for paces**: Always include effort description + estimated pace range + purpose.

Example: "Easy pace: conversational, should feel comfortable. Based on your 55-minute 10K, aim for 9:30-10:00 min/mile, but go slower if needed to stay conversational."

### Step 3: Assess Injury Risk and Select Training Profile

Read `references/injury-risk-assessment.md` to:
- Calculate injury risk score from gathered information
- Determine risk category (Low, Moderate, High)
- Identify appropriate plan adjustments

Key considerations:
- Recent injury to same area within 6 months = highest risk
- Low chronic training load + aggressive goals = high risk
- Age 40+ with limited running history = higher risk
- Multiple risk factors compound

**Balance risk assessment with user's profile preference:**

1. **Calculate objective injury risk** (Low/Moderate/High)
2. **Consider user's chosen profile** (Conservative/Moderate/Performance-Focused)
3. **Provide guidance if mismatch exists**:

   - **High Risk + Performance-Focused**: Warn strongly. "Based on [injury history/age/low base], I strongly recommend Conservative or Moderate approach. Performance-Focused carries significant injury risk for your situation. Are you sure you want to proceed with Performance-Focused?"

   - **Low Risk + Conservative**: Affirm choice. "Conservative is a smart, sustainable approach even with low injury risk."

   - **Moderate Risk + Performance-Focused**: Counsel. "With [moderate risk factors], Performance-Focused increases your injury risk. Consider starting with Moderate profile. Would you like to proceed with Performance-Focused anyway?"

4. **Respect user's final choice** but document the risk tradeoff clearly in the plan overview

**Special case - Post-race experienced runners**: Even if coming off a race (recent high load), experienced runners (3+ years) with no injury history may be ready for Performance-Focused after a 1-2 week recovery period. This is a legitimate use case.

### Step 4: Design Training Progression

Read `references/training-load-principles.md` to understand:
- Safe weekly progression rates (5-25% depending on experience and chronic load)
- ACWR targets (0.8-1.3 sweet spot, 0.8-1.4 for Performance-Focused)
- Deload week frequency and structure
- Intensity distribution based on profile

Read `references/training-profiles.md` for complete per-profile progression specs (ACWR targets, deload timing, intensity splits, speed work introduction, cross-profile rules, and post-race scenarios).

### Step 5: Determine Weekly Run Distribution

Read `references/training-profiles.md` for the full weekly distribution matrix (3, 4, 5, and 6–7 days/week × profile), stride execution guidance, micro-interval instructions, and workout distribution principles.

### Step 6: Create Week-by-Week Plan

List runs for each week without assigning them to specific days. Runners have different schedules and commitments — a plan that locks in specific days feels rigid and is harder to stick to when life gets in the way.

Read `references/plan-output-format.md` for the full document template (Plan Overview, Training Paces, "What Are Strides?", Micro-Intervals, "How to Use This Plan", and the week-by-week layout), the per-week and per-run requirements, the formatting checklist, and a worked end-to-end example.

In brief: for each week include the week number, date range (calculated from the start or race date), theme (Base Building, Build, Peak, Deload, Taper), and ACWR value; for each run include type, distance/duration, pace with effort description, and a short execution note. List runs as a numbered list rather than fixed days, mark deload weeks clearly, and show ACWR each week.

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

### Importing a Runner's Data

`references/data-import.md` has the full flow. In short, when Strava's native connector is available, list recent activities (filter to runs — road, trail, treadmill, virtual; include races) and read athlete stats for history context. From that, calculate weekly totals and frequency for the last ~4 weeks, assess consistency, extract a typical easy pace, and use the last 4 weeks as baseline chronic load for ACWR. Don't pull or use body-weight data.

The same calculations apply to a file or screenshot the user shares. If data is sparse or missing, present what you found honestly, ask whether they've been running untracked, treat genuinely low volume as a conservative-progression signal, and fill gaps with questions.

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

4. **data-import.md**:
   - At the start of gathering a runner's recent training data
   - Detecting and using the Strava connector
   - Handling exports/screenshots from other platforms and the export-pending case
   - Planning conservatively from unverified data

5. **training-profiles.md**:
   - When selecting a profile and designing progression (Steps 4–5)
   - Per-profile ACWR targets, deload timing, intensity splits
   - Weekly run-distribution matrix and stride/micro-interval guidance

6. **plan-output-format.md**:
   - When writing the final plan document (Step 6) and overall output
   - Full week-by-week template, per-week/per-run requirements, formatting checklist
   - Worked end-to-end example interaction

7. **plan-types.md**:
   - When tailoring to a specific race distance or goal
   - 5K/10K/half/marathon structure, distance-progression, general fitness

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

### Post-Race Recovery and Building

**Common scenario**: Experienced runners often want to build for their next race immediately after completing one. This is a legitimate and common use case.

**Post-race protocol**:

**Week 1-2 after race (Recovery period)**:
- Volume: 50-70% of pre-race peak volume
- Intensity: Easy runs only, no workouts
- Strides: Optional after week 1
- Purpose: Allow body to recover from race stress
- Note: Longer recovery for marathons (2 weeks) vs. shorter races (1 week)

**Week 3+ (Return to training)**:

For **experienced runners (3+ years) with no injury history**:
- Can start Performance-Focused profile immediately
- Begin with Week 1 volume from new plan (not where you left off)
- Re-establish chronic load before ramping up
- 2 workouts/week can resume in week 1-2 of new plan

For **intermediate runners or those with recent niggles**:
- Start with Moderate or Conservative profile
- Spend 2-4 weeks re-establishing base
- Gradually reintroduce workouts

**Key principle**: Post-race experienced runners don't need extended conservative base building - they have the chronic load and adaptation. After a short recovery, they can resume performance-focused training.

**Example timeline**:
- Marathon race: Sunday
- Week 1-2: Recovery (50-70% volume, easy only)
- Week 3: Start new training plan at Performance-Focused profile
- Volume starts moderate, can ramp aggressively since chronic load is high

## Creating Specific Plan Types

Read `references/plan-types.md` for distance-specific structure and timelines — 5K, 10K, half marathon, and marathon plans, distance-progression plans (e.g., 5K→10K), and general-fitness plans.

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

## Output Format

Always produce the plan as a **markdown document** following the template and formatting checklist in `references/plan-output-format.md`: a Plan Overview stating the training profile and rationale, training paces with effort descriptions, the "What Are Strides?" explainer, ACWR shown for each week, week themes and volumes, runs as a numbered list without fixed days, and a "How to Use This Plan" section. Plans should be easy to print, save, and modify.
