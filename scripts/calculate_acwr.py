#!/usr/bin/env python3
"""
Calculate Acute:Chronic Workload Ratio (ACWR) from training data.

This script helps calculate ACWR to monitor injury risk in training plans.
ACWR = Acute Load (last week) / Chronic Load (average of last 4 weeks)
"""

def calculate_acwr(weekly_loads):
    """
    Calculate ACWR from a list of weekly training loads.
    
    Args:
        weekly_loads: List of weekly training loads (miles, time, or training load units)
                     Most recent week should be LAST in the list.
                     Minimum 4 weeks of data required.
    
    Returns:
        float: ACWR value, or None if insufficient data
    
    Example:
        >>> calculate_acwr([30, 35, 38, 42])
        1.15  # 42 / average(30,35,38,42)
    """
    if len(weekly_loads) < 4:
        return None
    
    # Acute = most recent week
    acute = weekly_loads[-1]
    
    # Chronic = average of last 4 weeks (including current)
    chronic = sum(weekly_loads[-4:]) / 4
    
    if chronic == 0:
        return None
    
    acwr = acute / chronic
    return round(acwr, 2)


def calculate_rolling_acwr(weekly_loads):
    """
    Calculate ACWR for each week where sufficient data exists.
    
    Args:
        weekly_loads: List of weekly training loads in chronological order
    
    Returns:
        list: List of (week_number, acwr) tuples starting from week 4
    """
    results = []
    
    for i in range(3, len(weekly_loads)):
        acute = weekly_loads[i]
        chronic = sum(weekly_loads[i-3:i+1]) / 4
        
        if chronic > 0:
            acwr = acute / chronic
            results.append((i + 1, round(acwr, 2)))
    
    return results


def assess_injury_risk(acwr):
    """
    Assess injury risk based on ACWR value.
    
    Args:
        acwr: The acute:chronic workload ratio
    
    Returns:
        tuple: (risk_level, description, recommendation)
    """
    if acwr is None:
        return ("Unknown", "Insufficient data", "Need at least 4 weeks of training data")
    
    if acwr < 0.8:
        return (
            "Undertraining",
            "Training load is significantly below recent average",
            "Consider increasing volume gradually to maintain fitness"
        )
    elif 0.8 <= acwr <= 1.3:
        return (
            "Sweet Spot",
            "Optimal training load progression (4-5% injury risk)",
            "Continue current progression"
        )
    elif 1.3 < acwr <= 1.5:
        return (
            "Caution Zone",
            "Elevated training load (7-10% injury risk)",
            "Monitor closely. Consider deload next week if sustained"
        )
    else:  # acwr > 1.5
        return (
            "Danger Zone",
            "High injury risk (15-20%+ injury risk)",
            "Reduce load immediately. Take rest days or easy week"
        )


def plan_next_week(current_week, chronic_load, target_acwr=1.2):
    """
    Calculate recommended training load for next week based on target ACWR.
    
    Args:
        current_week: Current week's training load
        chronic_load: Average of last 4 weeks
        target_acwr: Desired ACWR for next week (default 1.2 for safe progression)
    
    Returns:
        float: Recommended training load for next week
    """
    recommended = chronic_load * target_acwr
    return round(recommended, 1)


def calculate_safe_progression(current_load, weeks_of_progression=3, target_acwr=1.2):
    """
    Calculate a safe progression plan maintaining target ACWR.
    
    Args:
        current_load: Current weekly training load
        weeks_of_progression: Number of weeks to plan
        target_acwr: Target ACWR for each progression week
    
    Returns:
        list: Planned weekly loads
    """
    plan = [current_load]
    loads = [current_load, current_load, current_load, current_load]  # Initialize with 4 weeks
    
    for _ in range(weeks_of_progression):
        chronic = sum(loads[-4:]) / 4
        next_week = chronic * target_acwr
        plan.append(round(next_week, 1))
        loads.append(next_week)
    
    return plan


# Example usage and tests
if __name__ == "__main__":
    print("=== ACWR Calculator Demo ===\n")
    
    # Example 1: Calculate current ACWR
    print("Example 1: Calculate ACWR from recent training")
    training_weeks = [30, 33, 36, 42]  # miles or training load units
    print(f"Training loads: {training_weeks}")
    
    acwr = calculate_acwr(training_weeks)
    print(f"ACWR: {acwr}")
    
    risk, description, recommendation = assess_injury_risk(acwr)
    print(f"Risk Level: {risk}")
    print(f"Description: {description}")
    print(f"Recommendation: {recommendation}\n")
    
    # Example 2: Rolling ACWR calculation
    print("Example 2: Rolling ACWR over 8 weeks")
    training_weeks = [25, 28, 30, 32, 35, 38, 40, 32]  # Last week is deload
    print(f"Training loads: {training_weeks}")
    
    rolling = calculate_rolling_acwr(training_weeks)
    print("Week | ACWR | Risk Assessment")
    print("-----|------|----------------")
    for week, acwr_val in rolling:
        risk, _, _ = assess_injury_risk(acwr_val)
        print(f"{week:4d} | {acwr_val:4.2f} | {risk}")
    print()
    
    # Example 3: Plan next week
    print("Example 3: Planning next week safely")
    current = 42
    chronic = 36.75  # Average of last 4 weeks
    print(f"Current week: {current} miles")
    print(f"Chronic load: {chronic} miles")
    
    for target in [1.1, 1.2, 1.3]:
        next_week = plan_next_week(current, chronic, target)
        print(f"For ACWR {target}: Next week should be ~{next_week} miles")
    print()
    
    # Example 4: Safe progression plan
    print("Example 4: 4-week safe progression from 30 miles")
    progression = calculate_safe_progression(30, weeks_of_progression=4, target_acwr=1.15)
    print(f"Safe progression maintaining ACWR ~1.15:")
    for week, load in enumerate(progression, 1):
        print(f"Week {week}: {load} miles")
