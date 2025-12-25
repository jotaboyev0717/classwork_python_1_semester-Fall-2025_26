def calculate_calories_burned(exercise_type, duration_minutes, intensity):
    if exercise_type == "cardio":
        if intensity == "low":
            calories_per_min = 8
        elif intensity == "medium":
            calories_per_min = 12
        elif intensity == "hihh":
            calories_per_min = 16
        else: 
            return "Invalid Intensity"
    
    elif exercise_type == "strength":
        if intensity == "low":
            calories_per_min = 6
        elif intensity == "medium":
            calories_per_min = 9
        elif intensity == "hihh":
            calories_per_min = 12
        else: 
            return "Invalid Intensity"
        
    elif exercise_type == "flexibilty":
        if intensity == "low":
            calories_per_min = 3
        elif intensity == "medium":
            calories_per_min = 5
        elif intensity == "high":
            calories_per_min = 7
        else: 
            return "Invalid Intensity"
    else:
        return "Invalid exercise type"
    
    return calories_per_min * duration_minutes

def calculate_heart_rate_zone(age, resting_hr, exercise_hr):
    max_hr = 220 - age
    heart_rate_reserve = max_hr - resting_hr
    intensity_percent = (exercise_hr - resting_hr) / heart_rate_reserve * 100
    return intensity_percent

def determine_training_zone(intensity_percent):
    if intensity_percent < 50:
        return "Warm-up Zone"
    elif intensity_percent < 60:
        return "Fat Burn Zone"
    elif intensity_percent < 70:
        return "Cardio Zone"
    elif intensity_percent < 85:
        return "Performance Zone"
    else:
        return "Maximum Effort Zone"

def calculate_workout_score(calories, duration, zone_multiplier):
    if zone_multiplier == "Warm-up":
        multiplier = 0.5
    elif zone_multiplier == 
    base_score = calories * 0.1 + duration * 2
    