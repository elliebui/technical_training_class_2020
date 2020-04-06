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
sending_text_numbers = set()
receiving_text_numbers = set()

for number in texts:
    sending_text_numbers.add(number[0])
    receiving_text_numbers.add(number[1])

# Lists to store numbers that are giving or answering calls
calling_call_numbers = set()
answering_call_numbers = set()

for number in calls:
    calling_call_numbers.add(number[0])
    answering_call_numbers.add(number[1])

# If a number only receives call and not sending text, receiving text, or answering call
# add it to list of telemarketers

not_telemarketer_numbers = answering_call_numbers | sending_text_numbers | receiving_text_numbers

telemarketers_numbers = calling_call_numbers.difference(not_telemarketer_numbers)


print("These numbers could be telemarketers: ")
for number in sorted(telemarketers_numbers):
    print(number)


# for number in texts/calls: O(1) complexity
# list_telemarketers: O(1) complexity
# sorted: O(nlogn) complexity
# Total: O(nlogn) complexity

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

"""
These numbers could be telemarketers: 
(022)37572285
(022)65548497
(022)68535788
(022)69042431
(040)30429041
(044)22020822
(0471)2171438
(0471)6579079
(080)20383942
(080)25820765
(080)31606520
(080)40362016
(080)60463379
(080)60998034
(080)62963633
(080)64015211
(080)69887826
(0821)3257740
1400481538
1401747654
1402316533
1403072432
1403579926
1404073047
1404368883
1404787681
1407539117
1408371942
1408409918
1408672243
1409421631
1409668775
1409994233
74064 66270
78291 94593
87144 55014
90351 90193
92414 69419
94495 03761
97404 30456
97407 84573
97442 45192
99617 25274
"""

