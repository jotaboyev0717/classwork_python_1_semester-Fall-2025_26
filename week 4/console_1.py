def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
def count_primes_between(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            count += 1
    return count
# print(count_primes_between(2, 8))

def nth_prime(n):
    if n < 1:
        return -1  # Invalid input
    
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1
    return -1

def is_twin_prime(n):
    return is_prime(n) and is_prime(n + 2)

a = is_twin_prime(15)
print(a)