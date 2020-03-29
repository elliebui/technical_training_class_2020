"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('textes.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# Index each column
incoming_number = 0
answering_number = 1
time = 2
during = 3

first_text = texts[0]
print("First record of texts, ", first_text[incoming_number], "texts ", first_text[answering_number], "at time ", first_text[time])

last_call = calls[-1]
print("Last record of calls, ", last_call[incoming_number], "calls ", last_call[answering_number], "at time ", last_call[time], ", lasting ", last_call[during], " seconds")

# O(1) complexity

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""