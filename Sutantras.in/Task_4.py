# 4. Task: Prime Number Generator
# Implement a generator function in Python that yields prime numbers indefinitely.
# Solution: Implement a generator function that generates prime numbers using a simple algorithm like the Sieve of Eratosthenes or trial division.

'''def generator():
    if (number <= 1) :
        return False
    count=0
    for i in range (2,number) :
	    if(number %i==0):
		    count +=count

While(True):
    for i in range (2,number):
        print(i," ")

number=int(input("Enter a number upto which you want to generate prime number : "))
a=generator()
print(a , " ")'''


def prime_generator():
    number = 2
    while True:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):  # Optimized by only checking up to the square root of the number
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            yield number
        number += 1

n = int(input("Enter a number to generate prime numbers up to it: "))
# Testing the prime generator
gen = prime_generator()
for _ in range(n):  # Generating and printing prime numbers
    print(next(gen))
