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


def extract_area_code(number, number_type):
    if number_type == "fixed_line":
        part = number.split("(")
        area_code = part[1].split(")")[0]
    elif number_type == "mobile":
        area_code = number[0:5]
    elif number_type == "telemarketer":
        area_code = "140"
    else:
        raise Exception(f"Number type {number_type} is not implemented.")

    return area_code


def get_sorted_unique_area_code_list(area_code_list):
    unique_list = set()
    for code in area_code_list:
        unique_list.add(code)
    return sorted(unique_list)


# List to store all numbers called by people in Bangalore
list_number_call_from_bangalore = [number[1] for number in calls if number[0][0:5] == "(080)"]

# List to store all fixed line code called by people in Bangalore
list_fixed_line_code = [extract_area_code(number, number_type="fixed_line") for number in
                        list_number_call_from_bangalore if number[0:2] == "(0"]

list_sorted_unique_fixed_line_code = get_sorted_unique_area_code_list(list_fixed_line_code)

# List to store all mobile code called by people in Bangalore
list_mobile_code = [extract_area_code(number, number_type="mobile") for number in list_number_call_from_bangalore if
                    number[5] == " " and number[0] in ["7", "8", "9"]]

list_sorted_unique_mobile_code = get_sorted_unique_area_code_list(list_mobile_code)

# List to store all telemarketer code called by people in Bangalore
list_telemarketer_code = [extract_area_code(number, number_type="telemarketer") for number in
                          list_number_call_from_bangalore if number[0:3] == "140"]

list_sorted_unique_telemarketer_code = get_sorted_unique_area_code_list(list_telemarketer_code)

print("Part A: The numbers called by people in Bangalore have codes:")
for number in list_sorted_unique_fixed_line_code:
    print(number)
for number in list_sorted_unique_mobile_code:
    print(number)
for number in list_sorted_unique_telemarketer_code:
    print(number)

# list_number_call_from_bangalore: O(N) complexity
# list_fixed_line_code & similar & similar ones: O(N^2) complexity
# list_sorted_unique_fixed_line_code & similar ones: O(N) complexity
# sorted: O(nlogn) complexity
# Total: O(N^2) complexity

# PART B

list_call_from_bangalore = [record for record in calls if record[0][0:5] == "(080)"]

list_call_to_bangalore_from_bangalore = [record for record in list_call_from_bangalore if record[1][0:5] == "(080)"]

percentage = len(list_call_to_bangalore_from_bangalore) / len(list_call_from_bangalore) * 100

print("Part B")
print(round(percentage, 2),
      "percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

# list_call_from_bangalore: O(N) complexity
# list_call_to_bangalore_from_bangalore: O(N) complexity
# percentage: O(1) complexity
# Total: O(N) complexity


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

"""
Part A: The numbers called by people in Bangalore have codes:
022
040
04344
044
04546
0471
080
0821
74062
74064
74066
77956
78130
78135
78293
78295
81510
81513
81515
81517
81524
83013
84312
84313
84319
87146
90087
90088
90192
90194
90196
90199
90351
90355
90365
90368
92414
92415
92421
92423
92429
93412
93414
93426
93427
93428
93432
93434
94001
94002
94005
94480
94482
94488
94491
94495
95263
95266
95267
96569
97380
97386
97402
97406
97410
97415
97416
97418
97422
97424
98440
98442
98443
98445
98446
98447
98448
98458
98459
99001
99003
99004
99612
Part B
24.81 percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.
"""
