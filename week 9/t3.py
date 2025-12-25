# def reformat_number(phone_number):
#     for i in " .,-":
#         phone_number = phone_number.replace(i, "")
#     a = []
#     i = 0
#     while len(phone_number) - i > 4:
#         a.append(phone_number[i:i+3])
#         i += 3
        
#     remain = len(phone_number) - 1
#     if remain == 4:
#         a.append(phone_number[i:i+2])
#         a.append(phone_number[i+2:])
#     else:
#         a.append(phone_number[i:])
#     return '-'.join(a)
# print(reformat_number("123 456 789"))     # 9 digits -> 3-3-3
# print(reformat_number("123-456-7890"))    # 10 digits -> 3-3-2-2 (4 remaining -> 2-2)
# print(reformat_number("123 45 678"))      # 8 digits -> 3-3-2
# print(reformat_number("12"))              # 2 digits -> 2
# print(reformat_number("12345"))           # 5 digits -> 3-2
# print(reformat_number("--1 23 4-5 6-7--")) # 7 digits -> 3-2-2 (4 remaining -> 2-2)

def reformat_number(phone_number):
    for i in " .,-":
        phone_number = phone_number.replace(i, "")
    a = []
    i = 0

    while len(phone_number) - i > 4:
        a.append(phone_number[i:i+3])
        i += 3
        
    remain = len(phone_number) - i

    if remain == 4:
        a.append(phone_number[i:i+2])
        a.append(phone_number[i+2:])
    else:
        a.append(phone_number[i:])
    return '-'.join(a)


print(reformat_number("123 456 789"))     # 9 digits -> 3-3-3
print(reformat_number("123-456-7890"))    # 10 digits -> 3-3-2-2
print(reformat_number("123 45 678"))      # 8 digits -> 3-3-2
print(reformat_number("12"))              # 2 digits -> 2
print(reformat_number("12345"))           # 5 digits -> 3-2
print(reformat_number("--1 23 4-5 6-7--")) # 7 digits -> 3-2-2
