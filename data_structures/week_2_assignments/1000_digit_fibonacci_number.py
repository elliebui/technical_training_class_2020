f2 = 1
f3 = 2
index = 3

while True:
    new_term = f2 + f3
    index += 1

    digit = len(str(new_term))
    if digit == 1000:
        break

    f2 = f3
    f3 = new_term

print("index", index)

"""
Answer:
4782
"""