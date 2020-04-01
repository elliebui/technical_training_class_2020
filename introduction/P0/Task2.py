"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import defaultdict

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# Dictionary to store all numbers and its time spent on the phone
number_to_time = defaultdict(int)

for record in calls:
    calling_number = record[0]
    answering_number = record[1]
    time = int(record[3])

    number_to_time[calling_number] += time
    number_to_time[answering_number] += time

# Find phone number with max time value and max time spent on the phone value
max_time_value, number_with_max_time_value = max((value, key) for key, value in number_to_time.items())

print(f"{number_with_max_time_value} spent the longest time, {max_time_value} seconds, on the phone during September 2016")

# for record in calls: O(N) complexity
# max((value, key) for key, value in number_to_time.items()): O(N) complexity
# Total: O(N) complexity


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


"""
Answer:
(080)33251027 spent the longest time, 90456 seconds, on the phone during September 2016
"""