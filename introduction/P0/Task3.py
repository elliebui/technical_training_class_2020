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

# PART A

# List to store all numbers called by people in Bangalore
list_call_from_Bangalore = []

for number in calls:
    incoming_number = number[0]
    answering_number = number[1]
    if incoming_number[0:5] == "(080)":
        list_call_from_Bangalore.append(answering_number)

# Lists to store all fixed line code and mobile code called by people in Bangalore
list_fixed_line_code = []
list_mobile_code = []

for number in list_call_from_Bangalore:
    if number[0:2] == "(0":
        part = number.split("(")
        list_fixed_line_code.append(part[1].split(")")[0])
    elif number[5] == " " and number[0] in ["7", "8", "9"]:
        list_mobile_code.append(number[0:4])


# Lists to store unique fixed line code and mobile code
unique_fixed_line_code_list = []

for number in list_fixed_line_code:
    if number not in unique_fixed_line_code_list:
        unique_fixed_line_code_list.append(number)
sorted_unique_fixed_line_code_list = sorted(unique_fixed_line_code_list)


unique_mobile_code_list = []

for number in list_mobile_code:
    if number not in unique_mobile_code_list:
        unique_mobile_code_list.append(number)
sorted_unique_mobile_code_list = sorted(unique_mobile_code_list)


print("Part A: The numbers called by people in Bangalore have codes:")
for number in sorted_unique_fixed_line_code_list:
    print(number)
for number in sorted_unique_mobile_code_list:
    print(number)

# O(N^2) complexity

# PART B

# List to store all numbers called by people in Bangalore
list_call_from_Bangalore = []

for record in calls:
    incoming_number = record[0]
    if incoming_number[0:5] == "(080)":
        list_call_from_Bangalore.append(record)

list_call_to_Bangalore_from_Bangalore = []

for record in list_call_from_Bangalore:
    answering_number = record[1]
    if answering_number[0:5] == "(080)":
        list_call_to_Bangalore_from_Bangalore.append(record)


percentage = len(list_call_to_Bangalore_from_Bangalore)/len(list_call_from_Bangalore)*100

print("Part B")
print(round(percentage, 2), "percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

# O(N^2) complexity


"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
