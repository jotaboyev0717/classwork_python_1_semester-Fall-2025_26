def calculate_average(score1, score2, score3):
    # Calculates the average of three scores
    return (score1 + score2 + score3) / 3


def drop_lowest(score1, score2, score3):
    # Drops the lowest score and averages the two highest
    scores = [score1, score2, score3]
    scores.remove(min(scores))
    return sum(scores) / 2


def calculate_weighted(assignments, midterm, final):
    # Calculates weighted average using 30% + 30% + 40%
    return assignments * 0.3 + midterm * 0.3 + final * 0.4


def determine_grade(average):
    # Determines letter grade
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'


def needs_improvement(current_avg, target_grade):
    # Minimum score needed for each grade
    grade_minimums = {'A': 90, 'B': 80, 'C': 70, 'D': 60}
    target_min = grade_minimums[target_grade]
    if current_avg < target_min:
        return True, round(target_min - current_avg, 2)
    else:
        return False, 0


# ---------- TEST DATA ----------
assignment1, assignment2, assignment3 = 85, 78, 92
midterm = 88
final = 82

# ---------- CALCULATIONS ----------
regular_avg = calculate_average(assignment1, assignment2, assignment3)
dropped_avg = drop_lowest(assignment1, assignment2, assignment3)
better_avg = max(regular_avg, dropped_avg)
weighted_avg = calculate_weighted(better_avg, midterm, final)
letter = determine_grade(weighted_avg)
needs_imp, points_needed = needs_improvement(weighted_avg, 'A')


# ---------- OUTPUT ----------
print("STUDENT GRADE CALCULATOR")
print("========================================")
print(f"Assignment Scores: {assignment1}, {assignment2}, {assignment3}")
print(f"Midterm Score: {midterm}")
print(f"Final Score: {final}")
print("----------------------------------------")
print(f"Regular Assignment Average: {regular_avg:.2f}")
print(f"Average with Lowest Dropped: {dropped_avg:.2f}")
print(f"Using Better Average: {better_avg:.2f}\n")

print(f"Weighted Course Average: {weighted_avg:.2f}")
print(f"Letter Grade: {letter}\n")

print(f"Needs improvement for an 'A': {'Yes' if needs_imp else 'No'}")
if needs_imp:
    print(f"Points needed: {points_needed}")
else:
    print("Already meets or exceeds 'A' grade requirement")
