# def letter_grade(A , B, C, D, F):
#     if A >= 90:
#         print(f"Processing score {A}:")
#         print(f"    Letter grade: A")
#         print(f"    Passing: True")
#         print(f"Score: {A} | Grade: A | Status: PASS")
#         print()
#     if B >= 80:
#         print(f"Processing score {B}:")
#         print(f"    Letter grade: B")
#         print(f"    Passing: True")
#         print(f"Score: {B} | Grade: B | Status: PASS")
#         print()
#     if C >= 70:
#         print(f"Processing score {C}:")
#         print(f"    Letter grade: C")
#         print(f"    Passing: True")
#         print(f"Score: {C} | Grade: C | Status: PASS")
#         print()
#     if D >= 60:
#         print(f"Processing score {D}:")
#         print(f"    Letter grade: D")
#         print(f"    Passing: True")
#         print(f"Score: {D} | Grade: D | Status: PASS")
#         print()
#     if F>= 50:
#         print(f"Processing score {F}:")
#         print(f"    Letter grade: F")
#         print(f"    Passing: Fail")
#         print(f"Score: {F} | Grade: F | Status: Fail")
#     return letter_grade
# letter_grade(95, 82, 73, 65, 58)

# # week 4 
# def get_letter_grade(score):
#     if score >= 90:
#         return "A"
#     elif score >= 80:
#         return "B"
#     elif score >= 70:
#         return "C"
#     elif score >= 60:
#         return "D"
#     else:
#         return "F"


# def is_passing(score):
#     return score >= 60


# def print_grade_report(score):
#     grade = get_letter_grade(score)
#     passing = is_passing(score)
#     status = "PASS" if passing else "FAIL"

#     print(f"Processing score {score}:")
#     print(f"  Letter grade: {grade}")
#     print(f"  Passing: {passing}")
#     print(f"Score: {score} | Grade: {grade} | Status: {status}")
#     print()


# for s in [95, 82, 73, 65, 58]:
#     print_grade_report(s)

x = 10

def change_value():
    global x
    x = 20   # global x ni o'zgartiryapti

change_value()
print(x)