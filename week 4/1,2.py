def calculate_average(score1, score2, score3):
    score = [score1, score2, score3]
    return sum(score)/len(score)

def drop_lowest(score1, score2, score3):
    scores = [score1, score2, score3]
    scores.remove(min(scores))
    return sum(scores)/2

def calculate_weighted(assignments, midterm, final):
    return assignments * 0.3 + midterm * 0.3 + final * 0.4

def determine_grade(average):
    if average >=90:
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
    grade_minimums = {'A': 90, 'B': 80, 'C': 70, 'D': 60}
    target_min = grade_minimums[target_grade]
    if current_avg < target_min:
        return True, round(target_min - current_avg, 2)
    else:
        return False, 0
