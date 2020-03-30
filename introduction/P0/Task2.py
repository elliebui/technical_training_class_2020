"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# Dictionary to store all numbers and its time spend on the phone
number_with_time = {}

for record in calls:
    incoming_number = record[0]
    answering_number = record[1]
    time = int(record[3])

    if incoming_number in number_with_time.keys():
        number_with_time[incoming_number] += time
    else:
        number_with_time.update({incoming_number: time})

    if answering_number in number_with_time.keys():
        number_with_time[answering_number] += time
    else:
        number_with_time.update({answering_number: time})


# Find phone number with max time
max_value = {"number": 0, "time": 0}

for number, time in number_with_time.items():
    if time > max_value["time"]:
        max_value["number"] = number
        max_value["time"] = time

print(max_value["number"], "spent the longest time, ", max_value["time"], "seconds, on the phone during September 2016.")

# O(N^2) complexity


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

