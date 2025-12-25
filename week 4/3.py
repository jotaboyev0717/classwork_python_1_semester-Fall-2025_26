def hours_to_minutes(hours):
    return hours * 60

def minutes_to_seconds(minutes):
    return minutes * 60

def total_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

def format_time(total_minutes):
    return f"{total_minutes // 60}hours and {total_minutes % 60}minutes"

def can_fit_task(available_hours, task_hours, task_minutes):
    available_minutes = available_hours * 60
    task_total_minutes = task_hours * 60 + task_minutes
    return task_total_minutes <= available_minutes

def schedule_summary(task_name, hours, minutes):
    total_min = hours * 60 + minutes
    total_sec = total_min * 60
    
    print(f"Task: {task_name}")
    print(f"Duration: {int(hours)} hours, {int(minutes)} minutes")
    print(f"Total Minutes: {total_min}")
    print(f"Total Seconds: {total_sec}")

print("TIME CONVERTER AND SCHEDULER")
print("========================================")

# Test 1: Convert 2.5 hours to minutes
result1 = hours_to_minutes(2.5)
print(f"Converting 2.5 hours to minutes: {result1} minutes")

# Test 2: Calculate total seconds for 1 hour, 45 minutes, 30 seconds
result2 = total_seconds(1, 45, 30)
print(f"Total seconds for 1 hour, 45 minutes, 30 seconds: {result2} seconds")

# Test 3: Format 200 minutes into hours and minutes
result3 = format_time(200)
print(f"Formatting 200 minutes: {result3}")

can_fit = can_fit_task(3.5, 3, 20)
fit_message = "Yes, the task fits!" if can_fit else "No, the task doesn't fit!"
print(f"Can a 3 hour 20 minute task fit in 3.5 hours? {fit_message}")

print("\nSCHEDULE SUMMARIES:")
print("------------------------------")

# Test 5: Schedule summaries
schedule_summary("Study", 2, 30)
print()  # Empty line for separation
schedule_summary("Exercise", 0, 45)
