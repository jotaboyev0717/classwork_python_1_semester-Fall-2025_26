def find_best_student(student_names, student_scores):
    if not student_names or not student_scores:
        return None
    
    highest_score = max(student_scores)
    
    best_index = student_scores.index(highest_score)
    
    return student_names[best_index]


names1 = ["Alice", "Bob", "Charlie", "David", "Bekzod"]
scores1 = [88, 92, 99, 95, 100]
print("Top student is: ", find_best_student(names1, scores1))

names2 = ["Eve", "Frank", "Grace"]
scores2 = [95, 85, 95]
print("Top student in a tie is: ", find_best_student(names2, scores2))


names3 = []
scores3 = []
print("Result for empty lists: ", find_best_student(names3, scores3))