def curve_grades(grades, curve_points):
    for i in range(len(grades)):
        grades[i] += curve_points
        if grades[i] > 100:
            grades[i] = 100
    return grades


test_scores = [85, 92, 77, 68, 100]
print(curve_grades(test_scores, 5))
final_exams = [95, 88, 98]
print(curve_grades(final_exams, 7))