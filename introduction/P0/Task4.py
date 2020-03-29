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

# Lists to store numbers that are sending and receiving text
sending_text_number = []
receiving_text_number = []

for number in texts:
    receiving_text_number.append(number[0])
    receiving_text_number.append(number[1])

# Lists to store numbers that are giving or answering calls
incoming_call_number = []
answering_call_number = []

for number in calls:
    incoming_call_number.append(number[0])
    answering_call_number.append(number[1])

# If a number only receives call and not sending text, receiving text, or answering call
# add it to list of telemarketers
list_telemarketers = []

for number in incoming_call_number:
    if number not in sending_text_number or receiving_text_number or answering_call_number:
        list_telemarketers.append(number)

unique_list = []
for number in list_telemarketers:
    if number not in unique_list:
        unique_list.append(number)

for number in sorted(unique_list):
    print(number)

# O(N^2) complexity

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

