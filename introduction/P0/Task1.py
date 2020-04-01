"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# Set to store all unique phone numbers
unique_phone_numbers = set()

for record in texts:
    unique_phone_numbers.add(record[0])
    unique_phone_numbers.add(record[1])

for record in calls:
    unique_phone_numbers.add(record[0])
    unique_phone_numbers.add(record[1])

print(f"There are {len(unique_phone_numbers)} different telephone numbers in the records")

# for record in texts: O(N) complexity
# for record in calls: O(N) complexity
# Total: O(N)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

"""
Answer:
There are 570 different telephone numbers in the records
"""