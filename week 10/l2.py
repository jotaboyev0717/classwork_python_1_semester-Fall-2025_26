grades = {"Math":85,
          "History": 92,
          "Physics":78,
          "Programming":95}
average = 0
for val in grades.values():
    average += val
    
print(f"Average score: {average / len(grades)}")
# keyy = []
# for key, values in grades.items():
#     keyy.append(key)
#     max(keyy) 2
# best_subject = max(grades, key=grades.get)
# print(best_subject, grades[best_subject])

max_key = None
max_value = 0

for key, value in grades.items():
    if value > max_value:
        max_value = value
        max_key = key

print(max_key, max_value)