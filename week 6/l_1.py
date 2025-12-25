def calculate_student_averages(scores):
    averages = []
    for i in scores:
        a = sum(i)/len(i)
        averages.append(a)
    return averages

student_scores = [
	[85, 92, 78],
	[90, 88, 94],
	[76, 80, 82]
]

student_averages = calculate_student_averages(student_scores)
print(f"Student averages: {student_averages}")