# 4. Task: Prime Number Generator
# Implement a generator function in Python that yields prime numbers indefinitely.
# Solution: Implement a generator function that generates prime numbers using a simple algorithm like the Sieve of Eratosthenes or trial division.

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

n = int(input("Enter a number to generate prime numbers up to it: "))
# Testing the prime generator
gen = prime_generator()
for _ in range(n):  # Generating and printing prime numbers
    print(next(gen))


# The algorithm used in the provided code is called the "trial division" algorithm for checking primality. Here's how it works:
    
    # Basic Checks: The function first performs some basic checks to quickly identify numbers that are not prime. These include checking if the number is less than or equal to 1, less than or equal to 3, or divisible by 2 or 3 (excluding 2 and 3 themselves).
    # Looping through Potential Divisors: The function then enters a loop starting from 5 (since we've already checked divisibility by 2 and 3). It iterates as long as the square of the current divisor is less than or equal to the number being checked.
    # Incrementing by 6: Within the loop, the algorithm increments the divisor by 6 at each step. This is because after checking divisibility by 2 and 3, all prime numbers greater than 3 can be expressed in the form 6k ± 1. By incrementing by 6, the algorithm skips even numbers and multiples of 3, reducing the number of checks needed.
    # Checking Divisibility: At each step of the loop, the algorithm checks if the number is divisible by the current divisor or the next number after it (i + 2). If the number is divisible by any of these factors, it is not prime.
    # Returning the Result: If the loop completes without finding any factors, the number is determined to be prime and the function returns True.