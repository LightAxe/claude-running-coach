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

## Strava Integration (Optional Enhancement)

**This skill is fully functional without Strava.** The standard question-based approach provides complete, comprehensive training plan creation for any runner.

Strava integration is an optional enhancement that can make data gathering faster by automatically pulling your recent training history. This is purely a convenience feature - all the same information can be gathered through questions.

### Benefits of Using Strava (Optional)

When connected to Strava, this skill can optionally:
- Analyze your last 4+ weeks of running activity for ACWR calculation
- Calculate actual weekly mileage and training frequency
- Determine your typical training paces from recent runs
- Assess training consistency and patterns
- View year-to-date and all-time running statistics

This provides more accurate baseline data than manual estimates and saves time during the information-gathering phase.

### Setting Up Strava MCP

**Note**: Setting up Strava MCP requires obtaining API credentials from Strava, which takes about 10-15 minutes.

**Quick setup overview:**
1. Create a free Strava API application at [strava.com/settings/api](https://www.strava.com/settings/api)
2. Set the authorization callback domain to "localhost"
3. Note your Client ID and Client Secret
4. Configure the Strava MCP server with your credentials
5. Authorize the connection when prompted

**Detailed instructions**: See the [Strava MCP GitHub repository](https://github.com/r-huijts/strava-mcp) for complete setup steps.

### When Strava Integration Might Be Offered

**Note**: Manual questions provide the same complete information - Strava is just an optional shortcut.

At the start of the information-gathering process (only if creating a plan for yourself), the skill may:
1. Offer to connect to your Strava account to auto-fill training data
2. If you decline or if you're creating a plan for someone else, continue with standard questions
3. If you accept and it's connected, pull recent training data and present for confirmation
4. Still ask about injury history, age, goals, and other personal factors not available in Strava

**Strava is only mentioned once.** If you decline or if you're coaching someone else, the conversation continues with standard questions without any further Strava references.

## Training Intensity Profiles

This skill offers three training intensity profiles based on recent sports science research (2024-2025). Each balances performance and injury risk differently.

### Profile Overview

**Conservative (Default for Most Runners)**
- **Best for**: Beginners, injury-prone runners, those building base, runners over 40, returning from injury
- **Intensity split**: 85% easy / 15% hard (true beginners: start 90-100% easy for first 2-3 months)
- **Workout frequency**: 1 quality session per week
- **Strides**: 2x per week (after base phase)
- **Target ACWR**: 0.8-1.2
- **Weekly progression**: 5-10% (following 3 weeks up, 1 week down pattern)
- **Speed work introduction**: Week 4-6 (beginners may delay to 8-12 weeks)
- **Philosophy**: Safety first, arrive healthy at start line

**Moderate (Balanced Approach)**
- **Best for**: Intermediate runners (1-3 years), injury-free with solid base, general fitness goals
- **Intensity split**: 80% easy / 20% hard (true 80/20 rule)
- **Workout frequency**: 1-2 quality sessions per week (build from 1 to 2)
- **Strides**: 3x per week
- **Micro-intervals**: Added to easy runs for variation
- **Target ACWR**: 0.8-1.3
- **Weekly progression**: 10-15% max during build weeks (3 weeks up, 1 week down)
- **Recovery**: Minimum 24 hours between quality sessions
- **Speed work introduction**: Week 2-3
- **Philosophy**: Balance performance gains with injury prevention

**Performance-Focused (Speed Priority)**
- **Best for**: Experienced runners (3+ years), competitive racers, those with strong training history, post-race building to next goal
- **Intensity split**: 75% easy / 25% hard (use polarized early season, pyramidal near racing)
- **Workout frequency**: 2 quality sessions per week from start
- **Strides**: 3x per week from week 1
- **Target ACWR**: 0.8-1.4 (accepts brief controlled spikes, not sustained)
- **Weekly progression**: 15-20% max during build weeks (still follow 3 up, 1 down pattern)
- **Recovery**: Minimum 48 hours between hard quality sessions
- **Speed work introduction**: Week 1-2 (can start immediately for experienced runners)
- **Periodization**: Polarized (lots easy, lots hard) in base phase; pyramidal (more threshold) near race
- **Philosophy**: Maximize performance gains, accept higher injury risk
- **Warning**: ⚠️ This profile carries significantly higher injury risk. Only for experienced runners with strong training history.

### Research Basis

Recent research (2024-2025) shows:
- **Pace variation prevents overuse injuries**: Running the same pace repeatedly causes repetitive microtrauma. [80-90% of running injuries occur suddenly during single sessions, often from lack of variation](https://medicalxpress.com/news/2025-07-injuries-suddenly-gradually-overuse.html)
- **Strides improve economy with low injury risk**: 2% running economy improvement and 3.2% performance gain after just 40 days
- **Interval training enhances performance**: 6-7% VO2max improvement in 6 weeks, but injury data is limited
- **Polarized training works**: 30% greater marathon improvement vs. pyramidal approach in recent studies
- **Individual response varies**: 31.5% respond best to polarized, 31.9% to pyramidal, 18.7% to both

### Single-Session Spike Warning

**Critical 2025 finding**: Injury risk increases significantly when any single run exceeds 10% of the longest run in the last 30 days. Monitor individual session spikes, not just weekly totals.

**Note on the 10% Rule**: While the classic "10% weekly mileage increase" rule is widely known, recent research shows individual variation matters significantly. The "3 weeks up, 1 week down" pattern with appropriate percentage increases based on experience level is more effective than rigid 10% limits. Low-mileage runners can often increase by higher percentages; high-mileage runners should be more conservative.

## Process for Creating Training Plans

### Step 1: Gather Essential Information

**IMPORTANT**: Always gather required information BEFORE creating a training plan. Do not generate the plan until all required information is collected and the user confirms they're ready.

#### Preliminary: Check for Strava Integration (Optional Enhancement)

**IMPORTANT**: The manual question process below is the complete, primary method for gathering information. Strava integration is purely an optional shortcut that can auto-fill some answers - the skill is fully functional without it.

**Before beginning the standard question flow**, quickly check if Strava integration might be useful:

1. **Identify the use case**:
   - If user indicates they're creating a plan for **someone else** (coaching scenario): Skip Strava entirely, proceed directly to "Required Information" below
   - If user is creating a plan for **themselves**: Attempt Strava connection

2. **Attempt Strava connection** (only if creating plan for self):
   - Try to access Strava MCP tools silently

3. **Offer Strava option** (one time only):
   - If connected: "I can connect to your Strava account to analyze your recent training, or I can ask you questions directly. Which would you prefer?"
   - If not connected: "I can either ask you questions about your training history, or if you'd like, I can connect to Strava to pull your data automatically (requires setup). Which would you prefer?"

4. **Handle user response and never mention Strava again**:
   - **User wants to use Strava (already connected)**: Proceed to "Pulling Strava Data" below, then continue with remaining questions
   - **User wants to set up Strava**: Offer brief help: "Setting up Strava MCP takes about 10-15 minutes. Would you like to do that now, or continue with questions?"
     - If yes: Provide setup guidance, wait for completion, proceed to "Pulling Strava Data"
     - If no: Proceed to "Required Information"
   - **User prefers manual questions**: Proceed directly to "Required Information" below
   - **Any decline/no**: Never mention Strava again in this conversation, proceed to "Required Information"

#### Pulling Strava Data (If User Agrees)

When user agrees to use Strava, pull and analyze the following data:

**Data to retrieve**:
1. **Recent activities** (last 4-8 weeks):
   - Use Strava MCP to list activities
   - Filter for activity type = "Run" only (includes treadmill and trail runs)
   - Include both training runs and races
   - Get: distance, duration, date, average pace for each activity

2. **Year-to-date and all-time statistics**:
   - Total runs, total distance, total time
   - Provides context for training history

3. **Training zones** (if configured in Strava):
   - Heart rate zones
   - Useful for understanding current fitness level

**Analyze and calculate**:
- Weekly mileage for each of the last 4 weeks
- Running frequency (days per week) over last 4 weeks
- Training consistency (gaps, patterns)
- Typical training paces from recent runs
- Current chronic load (average of last 4 weeks)

**Present findings for confirmation**:
After pulling data, present a summary and ask for confirmation:

"Based on your Strava data, here's what I see:

**Last 4 weeks:**
- Week 1: [X] miles, [Y] runs
- Week 2: [X] miles, [Y] runs
- Week 3: [X] miles, [Y] runs
- Week 4: [X] miles, [Y] runs

**Recent patterns:**
- Average: [X] miles/week over [Y] runs/week
- Typical easy pace: [X:XX]/mile
- Training consistency: [consistent/some gaps/spotty]

**Additional context:**
- Year-to-date: [X] runs, [Y] total miles
- All-time: [X] runs since [account start date or first activity]

Does this look accurate? Have you been running elsewhere (different app, no tracking) that I should know about?"

**Handle sparse data**:
If Strava shows very low volume (e.g., <5 runs in last month):
- Present the data honestly: "I see [X] runs in the last month totaling [Y] miles"
- Ask: "Have you been running elsewhere without tracking, or is this an accurate picture of your recent training?"
- Note: "Based on this volume, I'll recommend a conservative progression to build safely"
- If they confirm sparse training: Treat as novice/returning runner with high injury risk

**Still ask these questions manually** (not available in Strava):
- Age
- Injury history (last 6 months)
- Current pain or discomfort
- Training goal (race distance, date, objective)
- Desired training frequency (may differ from current)
- Risk tolerance
- Other relevant factors (life stress, scheduling constraints, etc.)

#### Required Information

**This is the primary, complete method for gathering information.** Whether or not Strava was used above, ask these questions systematically. If Strava data was pulled, some questions may already be answered - confirm the data rather than re-asking.

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

**Example dialogue flow (with Strava):**

User: "I want to train for a half marathon"

Claude: "Excellent! Let me first check if I can connect to your Strava account to analyze your recent training..."

Claude: [Attempts Strava MCP connection]

Claude: "I can connect to your Strava account to analyze your recent training. Would you like me to pull your running data? This will make the process faster and more accurate."

User: "Yes, please!"

Claude: [Pulls Strava data and analyzes]

Claude: "Great! Based on your Strava data, here's what I see:

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

Claude: "Perfect! Now I need to ask you a few more questions that I can't get from Strava. First, how old are you?"

User: "35"

Claude: "Thanks! Based on your Strava history since January 2024, it looks like you've been running for about a year. Would you say that's accurate for how long you've been running consistently?"

User: "Actually I ran in college, but took many years off. This is my comeback year."

Claude: "That's helpful context! Have you had any injuries in the last 6 months, or do you have any current pain or discomfort?"

[Continue with remaining manual questions: injury history, goal details, desired frequency, risk tolerance, etc.]

**Example dialogue flow (without Strava - User Declines):**

User: "I want to train for a half marathon"

Claude: "Excellent! I can either ask you questions about your training history, or if you'd like, I can connect to Strava to pull your data automatically. Which would you prefer?"

User: "Let's just do questions"

Claude: "Sounds good! I'd like to ask you a few questions to create the best training plan for you. First, how old are you?"

User: "35"

Claude: "Thanks! How long have you been running consistently?"

User: "About 2 years"

Claude: "Great. What has your training looked like recently - how many miles per week or days per week have you been running over the last month or so?"

User: "I've been running 3-4 times per week, probably around 15-20 miles per week"

[Continue with remaining questions - Strava is never mentioned again]

**Example dialogue flow (Coaching Use Case):**

User: "I want to create a half marathon training plan for my friend"

Claude: "Excellent! I'd be happy to help you create a training plan for your friend. Let me ask you some questions about their training background and goals. First, how old are they?"

User: "They're 28"

Claude: "Thanks! How long have they been running consistently?"

[Continue with all questions - Strava is never mentioned since this is for someone else]

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

**Plan structure by Training Profile**:

**Conservative Profile:**
- Weekly increases: 5-10% max during build weeks
- Pattern: 3 weeks up, 1 week down (deload)
- Deload: Every 3-4 weeks (30-40% volume reduction from peak)
- ACWR target: 0.8-1.2
- Intensity split: 85/15 (easy/hard) - true beginners start 90-100% easy for first 2-3 months
- Speed work introduction: Week 4-6 for intermediate; week 8-12 for true beginners
- Strides: 2x/week starting week 2-3
- Workout frequency: 1 quality session/week
- Philosophy: Slow and steady, prioritize consistency and injury prevention

**Moderate Profile:**
- Weekly increases: 10-15% max during build weeks (not every week)
- Pattern: 3 weeks up, 1 week down (deload)
- Deload: Every 3 weeks (30% volume reduction from peak)
- ACWR target: 0.8-1.3
- Intensity split: 80/20 (true 80/20 rule)
- Speed work introduction: Week 2-3
- Strides: 3x/week starting week 1-2
- Micro-intervals: Add 30-60 sec pickups to easy runs for pace variation
- Workout frequency: 1-2 quality sessions/week (build from 1 to 2 over 4-6 weeks)
- Recovery: Minimum 24 hours between quality sessions
- Philosophy: Balanced performance and safety

**Performance-Focused Profile:**
- Weekly increases: 15-20% max during build weeks (still follow 3-up-1-down pattern, not sustained)
- Pattern: 3 weeks up, 1 week down (sometimes 2 up, 1 down if very aggressive)
- Deload: Every 3-4 weeks (30% volume reduction)
- ACWR target: 0.8-1.4 (accepts brief controlled spikes to 1.4, not sustained above 1.3)
- Intensity split: 75/25 or polarized distribution
- Periodization: Polarized (very easy + very hard) in base/early season; pyramidal (more threshold) near racing
- Speed work introduction: Week 1-2 (can start immediately for experienced runners)
- Strides: 3x/week from week 1
- Workout frequency: 2 quality sessions/week from start
- Recovery: Minimum 48 hours between hard quality sessions (easy days or rest between)
- Philosophy: Maximize speed development, accept higher injury risk
- **Monitor single-session spikes**: No single run >110% of longest run in last 30 days
- **Warning**: Brief ACWR spikes to 1.4 acceptable for 1-2 weeks only, then must return to 1.3 or below

**Critical rules (all profiles)**:
- Progress only ONE variable at a time (frequency, duration, OR intensity)
- Monitor ACWR weekly
- Respect deload weeks (non-negotiable)
- Allow 48 hours between hard workouts

**Post-race scenarios**:
- After race: 1-2 week recovery period (easy running only, 50-70% of pre-race volume)
- Then: Experienced runners can jump into Performance-Focused if desired
- Base-building phase may be minimal (1-2 weeks) for experienced post-race runners

### Step 5: Determine Weekly Run Distribution

Based on the runner's desired frequency and training profile, determine the types and distribution of runs each week:

**3 days/week** (beginner or time-limited):
- 2 easy runs
- 1 long run
- **Conservative**: Strides 1-2x/week after week 2-3, one workout after week 4-6
- **Moderate**: Strides 2x/week from week 2, one workout from week 3
- **Performance-Focused**: Strides 2x/week from week 1, one workout from week 1-2

**4 days/week** (intermediate):
- 2 easy runs
- 1 workout (tempo or intervals)
- 1 long run
- **Conservative**: Strides 2x/week, 1 workout/week from week 4-6
- **Moderate**: Strides 3x/week, 1 workout/week from week 2, build to 2 workouts by mid-plan
- **Performance-Focused**: Strides 3x/week from week 1, 2 workouts/week from week 2

**5 days/week** (intermediate to advanced):
- 2-3 easy runs (one may be recovery run)
- 1-2 workouts (different stimulus - e.g., tempo + intervals)
- 1 long run
- **Conservative**: Strides 2x/week, 1 workout/week
- **Moderate**: Strides 3x/week, 1-2 workouts/week (vary the stimulus)
- **Performance-Focused**: Strides 3x/week, 2 workouts/week (polarized or pyramidal)

**6-7 days/week** (advanced):
- 3-4 easy/recovery runs
- 2 quality sessions per week (tempo, intervals, etc.)
- 1 long run
- May include double-run days for high volume
- **All profiles**: Strides 3x/week, 2 workouts/week minimum

**What are Strides?**

Strides are short 20-30 second bursts at 85-90% effort (not a full sprint) that improve running economy, form, and speed with minimal injury risk. Research shows 2% running economy improvement and 3.2% performance gain from just 1-2 stride sessions per week.

**How to do strides**:
1. Do them AFTER an easy run (not when fatigued from hard workouts)
2. Find a flat, clear section of road or track
3. Gradually accelerate for 20-30 seconds up to about 85-90% of max effort
4. Focus on smooth, controlled form - not an all-out sprint
5. Decelerate gradually, then walk back to start (full recovery, 60-90 seconds)
6. Repeat 4-8 times depending on fitness level
7. Total time: 5-10 minutes

**Example**: "After your 5-mile easy run, find a flat section and do 6 strides: accelerate smoothly for 20 seconds to about mile race pace, then walk back for full recovery. Focus on quick, light turnover."

**Micro-intervals (Moderate profile)**:

For pace variation without excessive fatigue, add 30-60 second pickups during easy runs:
- During middle 3-4 miles of an easy run
- 30-60 seconds at steady/moderate pace (not hard)
- 2-3 minutes easy recovery
- Repeat 4-6 times
- Purpose: Vary stimulus, prevent repetitive strain

**Workout distribution principles**:
- Hard workouts need at least 48 hours between them (easy day or rest day)
- Long run is typically the longest single effort of the week
- Easy runs make up 75-85% of weekly volume depending on profile
- Strides don't count as "intensity" workload (too short)
- Recovery runs (when doing 6+ days/week) are shorter and easier than regular easy runs
- **Pace variation is injury prevention**: Never run the same pace every run

**Note**: Since plans don't assign specific days, remind runners to space hard efforts appropriately when scheduling their own week.

### Step 6: Create Week-by-Week Plan

**IMPORTANT**: Plans should list runs for each week WITHOUT assigning them to specific days. Let runners schedule runs based on their own calendar and preferences.

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
- **CRITICAL**: Keep hard workouts separated by at least 48 hours (one easy day or rest)
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

### Strava MCP Tools (If Available)

When Strava MCP is connected, use these tools during the information-gathering phase:

**Primary tools for training plan creation:**

1. **List Recent Activities**:
   - Tool: `strava_list_activities` or similar
   - Purpose: Get last 4-8 weeks of running data
   - Filters: Activity type = "Run" (includes road, trail, treadmill)
   - Returns: Distance, duration, date, pace, elevation for each run
   - Use for: Calculating weekly mileage, frequency, consistency patterns

2. **Get Athlete Stats**:
   - Tool: `strava_get_stats` or similar
   - Purpose: Retrieve year-to-date and all-time statistics
   - Returns: Total runs, total distance, total time
   - Use for: Understanding overall training history and experience level

3. **Get Training Zones** (optional):
   - Tool: `strava_get_zones` or similar
   - Purpose: Retrieve user's configured heart rate zones
   - Returns: HR zone boundaries
   - Use for: Understanding current fitness level if zones are set

**How to use the data:**

1. **Calculate weekly totals**: Sum distance and count activities for each of the last 4 weeks
2. **Determine frequency**: Calculate average days/week of running
3. **Assess consistency**: Look for gaps, patterns, or recent changes
4. **Extract paces**: Use average pace from recent easy runs for pace calculations
5. **Calculate current ACWR**: Use last 4 weeks to determine baseline chronic load

**Important filtering:**
- Only count activities where `type = "Run"`
- Include all run types: road, trail, treadmill, virtual
- Include both training runs and races
- DO NOT pull or use weight data from Strava

**Example MCP tool usage:**
```
# Check if Strava is available and connected
# Attempt to list recent activities
# Filter for runs only
# Analyze last 4-8 weeks of data
# Present summary to user for confirmation
```

**When Strava data is sparse or missing:**
- Present what you found honestly
- Ask if they've been running elsewhere (different app, no tracking)
- Use sparse data as an indicator for conservative progression
- Fill in gaps with manual questions

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

- **STRAVA IS OPTIONAL** - Manual questions are the complete, primary method. Strava is just a shortcut. Only mention Strava once at the start. If user declines or is creating plan for someone else, never mention Strava again.
- **TRAINING PROFILES AVAILABLE** - Offer Conservative, Moderate, or Performance-Focused based on runner's goals and experience. Respect user choice but warn if mismatch with injury risk.
- **ALWAYS gather required information FIRST** - Collect: age, running experience, recent training, injury history, goal, desired frequency, and training profile preference. Wait for user confirmation before generating plan.
- **PACE VARIATION PREVENTS INJURY** - Never create plans with same pace every run. Include strides, varied workouts, and micro-intervals (Moderate profile) to prevent repetitive strain.
- **STRIDES ARE STANDARD** - Include 2-3x/week after week 1-2 for all profiles. Explain what they are and how to do them in every plan.
- **ACWR targets by profile** - Conservative: 0.8-1.2, Moderate: 0.8-1.3, Performance-Focused: 0.8-1.4
- **Single-session spike rule** - No run should exceed 10% of longest run in last 30 days
- **Deload weeks are non-negotiable** - plan them every 3-4 weeks for all profiles
- **Progress ONE variable at a time** - never increase frequency, duration, AND intensity simultaneously
- **Intensity distribution by profile** - Conservative: 85/15, Moderate: 80/20, Performance-Focused: 75/25 or polarized
- **POST-RACE EXPERIENCED RUNNERS** - Can jump to Performance-Focused after 1-2 week recovery. Don't force conservative base phase on established runners.
- **Individual risk factors matter** - assess injury risk but respect user's informed choice of profile
- **Flexibility is essential** - real life disrupts training; plans should accommodate this

## Output Format

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
