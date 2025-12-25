def update_employee_score(employees, scores, employee_name, new_score):
    if employee_name in employees:
        index = employees.index(employee_name)
        scores[index] = new_score
        return True
    return False


def remove_underperforming(employees, scores, min_score):
    i = 0
    while i < len(scores):
        if scores[i] < min_score:
            employees.pop(i)
            scores.pop(i)
        else:
            i += 1


def group_by_performance(employees, scores, high_performer_threshold):
    high_performers = []
    core_contributors = []

    for i in range(len(employees)):
        if scores[i] >= high_performer_threshold:
            high_performers.append(employees[i])
        else:
            core_contributors.append(employees[i])

    return high_performers, core_contributors


def run_performance_review(initial_employees, initial_scores,
                           employee_to_update, min_performance_score,
                           high_performer_score):

    employees = initial_employees.copy()
    scores = initial_scores.copy()

    update_employee_score(
        employees, scores,
        employee_to_update[0],
        employee_to_update[1]
    )

    remove_underperforming(employees, scores, min_performance_score)

    high_performers, core_contributors = group_by_performance(
        employees, scores, high_performer_score
    )

    return high_performers, core_contributors

employees = ["Alice", "Bob", "Charlie", "David"]
scores = [70, 95, 88, 74]
update_info = ["Alice", 72]
min_required_score = 75
high_perf_score = 90

high_performers, core_contributors = run_performance_review(
    employees, scores, update_info,
    min_required_score, high_perf_score
)

print(high_performers)    
print(core_contributors)   