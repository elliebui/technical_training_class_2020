import math

prime_numbers = [2]
number = 2

while True:
    i = 2
    is_prime = 1
    # For each number, divide it by each number in range(2 and its square root +1)
    for i in range(2, math.ceil(math.sqrt(number)) + 1):
        if number % i == 0:
            # If number is divisible by any number in that range, it is not prime
            # Stop for loop to check for prime
            is_prime -= 1
            break
        # If number is not divisible by each number in range, increment i by 1
        i += 1

    # If number is not divisible by any number in that range,
    # is_prime should have value 1. Add it to the list.
    if is_prime == 1:
        prime_numbers.append(number)

    # Once a number is checked, increment number by 1
    # While loop starts again for the next number
    number += 1

    # If length of prime number list reaches 10001, stop while loop
    if len(prime_numbers) == 10001:
        break

# Return the 10001st prime number
print(prime_numbers[10000])


"""
Answer:
104743
"""