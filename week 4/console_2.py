def count_uppercase(password):
    count = 0
    for i in password:
        if i >= 'A' and i <= 'Z':
            count += 1        
    return count

def count_lowercase(password):
    count = 0
    for i in password:
        if i >= 'a' and i <= 'z':
            count += 1
    return count

def count_digits(password):
    count = 0
    for i in password:
        if i >= '0' and i <= '9':
            count += 1
    return count

def has_special_char(password):
    special_chars = "!@#$%^&*"
    for i in password:
        if i in special_chars:
            return True
    return False

def calculate_strength(password):
    score = 0
    if count_uppercase(password) >= 2:
        score += 1
    if count_lowercase(password) >= 2:
        score += 1
    if count_digits(password) >= 2:
        score += 1
    if has_special_char(password) >= 2:
        score += 1
    if len(password) >= 8:
        score += 1
    return score
def get_strength_label(score):
    if score <= 1:
        return 'Very Weak'
    elif score==2:
        return 'Weak'
    elif score ==3:
        return 'Medium'
    elif score == 4:
        return 'Strong'
    else:
        return 'Very strong'

print("Password Strength Analysis")
print("-" * 40)

password1 = "abc"
score1 = calculate_strength(password1)
label1 = get_strength_label(score1)
print(f"Password: {password1}")
print(f"  Uppercase: {count_uppercase(password1)}, Lowercase: {count_lowercase(password1)}, Digits: {count_digits(password1)}")
print(f"  Strength Score: {score1}/5")
print(f"  Strength Label: {label1}")
print()

password2 = "Hello"
score2 = calculate_strength(password2)
label2 = get_strength_label(score2)
print(f"Password: {password2}")
print(f"  Uppercase: {count_uppercase(password2)}, Lowercase: {count_lowercase(password2)}, Digits: {count_digits(password2)}")
print(f"  Strength Score: {score2}/5")
print(f"  Strength Label: {label2}")
print()

password3 = "HeLLo123"
score3 = calculate_strength(password3)
label3 = get_strength_label(score3)
print(f"Password: {password3}")
print(f"  Uppercase: {count_uppercase(password3)}, Lowercase: {count_lowercase(password3)}, Digits: {count_digits(password3)}")
print(f"  Strength Score: {score3}/5")
print(f"  Strength Label: {label3}")
print()

password4 = "Pass@123"
score4 = calculate_strength(password4)
label4 = get_strength_label(score4)
print(f"Password: {password4}")
print(f"  Uppercase: {count_uppercase(password4)}, Lowercase: {count_lowercase(password4)}, Digits: {count_digits(password4)}")
print(f"  Strength Score: {score4}/5")
print(f"  Strength Label: {label4}")
print()

password5 = "MyP@ssW0rd!"
score5 = calculate_strength(password5)
label5 = get_strength_label(score5)
print(f"Password: {password5}")
print(f"  Uppercase: {count_uppercase(password5)}, Lowercase: {count_lowercase(password5)}, Digits: {count_digits(password5)}")
print(f"  Strength Score: {score5}/5")
print(f"  Strength Label: {label5}")