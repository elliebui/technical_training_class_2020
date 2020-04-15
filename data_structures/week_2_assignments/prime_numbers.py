import math

prime_numbers = []
number = 2

while len(prime_numbers) < 10001:
    is_prime = True
    # For each number, divide it by each number in list of prime number less than its square root
    for i in prime_numbers:
        if i > math.sqrt(number):
            break
        if number % i == 0:
            # If number is divisible by any number already in list of prime numbers, it is not prime
            # Stop for loop to check for prime
            is_prime = False
            break

    # If number is not divisible by any number in list of prime numbers,
    # is_prime should have value True. Add it to the list.
    if is_prime:
        prime_numbers.append(number)

    # Once a number is checked, increment number by 1
    # While loop starts again for the next number
    number += 1


# Return the 10001st prime number (last item in list of 10001 items)
print(prime_numbers[-1])


"""
Answer:
104743
"""