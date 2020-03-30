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

# Index each column
calling_number_index = 0
answering_number_index = 1
time_index = 2
duration_index = 3

first_text = texts[0]
print(f"First record of texts, {first_text[calling_number_index]}, texts {first_text[answering_number_index]} at time {first_text[time_index]}")

last_call = calls[-1]
print(f"Last record of calls, {last_call[calling_number_index]}, at time {last_call[time_index]}, lasting {last_call[duration_index]} seconds")

# O(1) complexity

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

"""
Answer:
First record of texts, 97424 22395, texts 90365 06212 at time 01-09-2016 06:03:22
Last record of calls, 98447 62998, at time 30-09-2016 23:57:15, lasting 2151 seconds
"""