def find_best_student(student_names, student_scores):
    if not student_scores or not student_names:
        return None
    highest_score = max(student_scores)
    index = student_scores.index(highest_score)
    return student_names[index]

names = ["Alice", "Bob", "Charlie", "David"]
scores = [88, 92, 99, 95]
print(find_best_student(names, scores))

names = ["Eve", "Frank", "Grace"]
scores = [95, 85, 95]
print(find_best_student(names, scores))


names = []
scores = []
print(find_best_student(names, scores))
