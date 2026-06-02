# Gathering a Runner's Training Data

This skill needs a picture of someone's recent running before it can build a sensible plan. There are three ways to get there, and they're not equal in speed or reliability. This document covers how to source the data, what's actually needed, and how to handle the common case where the data isn't available right now.

The goal isn't "use the fanciest source." It's "get an honest picture of recent training with the least friction." Often that's a short conversation, not an import.

## The data we actually need

Keep imports focused on roughly the **last 4–6 weeks**, plus a little history. Everything below can also be gathered by just asking:

- **Recent runs** (last 4–6 weeks): date, distance, and duration (or pace) per run
- **Longest recent run** (within ~30 days) — anchors the single-session spike rule
- **How long they've been running** consistently (years) — experience level
- **Typical easy/conversational pace** — for pace zones

Things no data source provides — always ask these regardless of how the rest arrived:

- Age
- Injury history (last 6 months) and any current pain
- Goal (distance, date, finish vs. time vs. PR)
- Desired training frequency
- Life context (stress, sleep, schedule constraints)

We don't need years of history or per-second files. Recent volume, frequency, longest run, and a pace anchor are enough.

## Three ways to get the data

### 1. Strava native MCP connector (detect first)

As of June 2026, Strava ships an official first-party MCP connector. It's the cleanest path when it's available, but it has gates worth understanding:

- It requires a **paid Strava subscription**.
- The user must have already **enabled the Strava connector** in their Claude settings — the skill cannot trigger that setup or the OAuth flow mid-conversation.

Because of the second point, most people won't have it connected yet even if they pay for Strava. So **try the connector silently first**; if its tools respond, use them. If nothing responds, don't quiz the user about their subscription tier — just move on to asking where their data lives.

When the connector responds, pull recent running activities (filter to runs — road, trail, treadmill, virtual), plus athlete stats for history context. Summarize weekly mileage, frequency, consistency, and typical pace, then confirm with the user before planning. Don't pull or use body-weight data.

The connector also exposes richer data (per-second streams, heart-rate zones, gear/shoe mileage). This version of the skill doesn't use those — recent volume, frequency, and pace are enough for planning. They're a possible future enhancement.

### 2. An export or screenshot from any platform

If the connector isn't available, ask how they track their runs and work with whatever they have. The important reality: **most platform exports arrive later by email, not instantly.**

- **Strava bulk export** — a GDPR archive request emailed as a download link, often hours later. Not available in-conversation. The `activities.csv` inside is the useful part.
- **Garmin Connect export** — also a delayed, emailed GDPR archive; large and spread across many files.
- **Apple Health export** — generated on the iPhone (Health app → profile → Export All Health Data). Available fairly quickly but is one very large XML.
- **Intervals.icu** — has a free API and can ingest directly from devices, so it's a useful free hub; data can be exported from the activities view.

Because full exports are delayed and bulky, the **fastest "data" option for most people is a screenshot or copy-paste of their recent weekly view** from whatever app they use. Claude can read a screenshot of the last few weeks of runs directly. Suggest this before sending someone off to request a full export.

When a file is provided, parse the recent slice (last 4–6 weeks), summarize it, and confirm before planning — same as the connector path.

### 3. Just ask

A short Q&A is a complete, legitimate method — not a consolation prize. When exports are delayed and the connector isn't set up, asking is usually *faster*. Gather recent frequency, weekly volume, typical run length, longest recent run, and how long they've been running, alongside the always-ask questions above.

## When the data isn't here yet

A common situation: the connector isn't set up, and any useful export will arrive by email later. Don't leave the runner empty-handed. Offer a clear choice:

- **Build a conservative provisional plan now** from what they can tell you, then have them return to recalibrate when real data arrives, **or**
- **Wait** and build the plan once the export is ready.

Either is fine — let them decide. A conversation is easy to return to in a few hours or the next day, so "come back when your export arrives" is a reasonable plan, not a dead end.

If they choose a provisional plan, see "Planning from unverified data" below.

## Planning from unverified data

Self-reported numbers (and provisional plans built before an export arrives) aren't backed by real data, and people tend to round their training up. So lean cautious:

- **Default to the Conservative profile** (don't force it — an experienced, clearly well-trained runner can still choose otherwise; just start from Conservative).
- **Start volume at the low end of their stated range** rather than the top.
- Note briefly that real data would sharpen the plan, and — if an export is pending or they later connect Strava — invite them back to update it with actual numbers. Frame this as an option, not a requirement.

## A note on privacy

An export or screenshot can contain a fair amount of personal health data. Give a brief, non-blocking heads-up: share only what you're comfortable with, and a screenshot of the last few weeks is usually plenty — there's no need to upload a full archive. This is informational, not a roadblock.
