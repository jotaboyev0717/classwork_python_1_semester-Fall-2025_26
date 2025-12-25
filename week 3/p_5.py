numbers = int(input())
a = 0
b = 1
for i in range(numbers):
    print(a, end=" ")
    a, b = b, a + b
print()

n = int(input("Nechta Fibonacci sonini chiqarmoqchisiz? "))

fib = [0, 1]  # boshlang‘ich sonlar
for i in range(2, n):
    fib.append(fib[-1] + fib[-2])  # oxirgi 2 ta element yig‘indisi

print(fib[:n])  # faqat n ta birinchi sonni chiqaradi

n = int(input("Nechta Fibonacci sonini chiqarmoqchisiz? "))

a, b = 0, 1
count = 0

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
    
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Nechta Fibonacci sonini chiqarmoqchisiz? "))
for i in range(n):
    print(fibonacci(i), end=" ")
