a = 1
b = 2
sum = 2

while True:
    new_term = a + b
    if new_term % 2 == 0:
        sum += new_term
    if new_term >= 4000000:
        break

    a = b
    b = new_term

print(sum)

"""
Answer:
4613732
"""