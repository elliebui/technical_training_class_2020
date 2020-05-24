def case_sort(string):
    sorted_string = sorted(string)
    lower_chars = list()
    upper_chars = list()
    for char in sorted_string:
        if char.islower():
            lower_chars.append(char)
        elif char.isupper():
            upper_chars.append(char)

    out_string = ""

    for char in string:
        if char.islower():
            char = lower_chars.pop(0)
        elif char.isupper():
            char = upper_chars.pop(0)
        out_string += char

    return out_string


def test_function(test_case):
    test_string = test_case[0]
    solution = test_case[1]

    if case_sort(test_string) == solution:
        print("Pass")
    else:
        print("False")


test_string = 'fedRTSersUXJ'
solution = "deeJRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)

test_string = "defRTSersUXI"
solution = "deeIRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)