
prime_numbers = [2]
number = 2

while True:
    is_prime = True
    # For each number, divide it by each number in list of prime number less than it
    for i in prime_numbers:
        if number % i == 0:
            # If number is divisible by any number already in list of prime numbers, it is not prime
            # Stop for loop to check for prime
            is_prime = False
            break
        # If number is not divisible by each number in list of prime numbers, increment i by 1
        i += 1

    # If number is not divisible by any number in list of prime numbers,
    # is_prime should have value True. Add it to the list.
    if is_prime:
        prime_numbers.append(number)

    # Once a number is checked, increment number by 1
    # While loop starts again for the next number
    number += 1

    # If length of prime number list reaches 10001, stop while loop
    if len(prime_numbers) == 10001:
        break

# Return the 10001st prime number (last item in list of 10001 items)
print(prime_numbers[-1])


"""
Answer:
104743
"""