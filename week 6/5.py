n = int(input())
for i in range(3, 155):
    if n % i == 0:
        print("Yes")
        break
    else:
        print("No")
        break