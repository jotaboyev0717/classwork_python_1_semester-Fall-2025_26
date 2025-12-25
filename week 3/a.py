# --- Problem 3: Prime Number Checker ---
print("--- Prime Number Checker ---")
number = int(input("Enter a positive integer to check: "))

# A "flag" variable to keep track of the result. Assume it's prime.
is_prime = True

# Prime numbers must be greater than 1
if number <= 1:
    is_prime = False
else:
    # Check for divisors from 2 up to number-1
    for i in range(2, number):
        # If the number is perfectly divisible by any 'i', it's not prime
        if (number % i) == 0:
            is_prime = False # Change the flag
            print(f"{number} is divisible by {i}, so it is not a prime number.")
            break # Found a divisor, no need to check further.

# After the loop, check the flag to print the final result
if is_prime:
    print(f"{number} is a prime number!")
# This condition prevents printing the message twice for numbers <= 1
elif number > 1:
    print(f"{number} is not a prime number.")
else: # Handles the specific case of numbers <= 1
    print(f"{number} is not considered a prime number.")