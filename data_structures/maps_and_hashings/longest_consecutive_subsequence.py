def longest_consecutive_subsequence(input_list):
    # Write longest consecutive subsequence solution
    input_dict = dict()
    output_list = list()
    longest_count = 0

    for number in input_list:
        input_dict[number] = 0

    for number in input_dict:
        if (number - 1) not in input_dict:
            current = number
            count = 1

            while (current + 1) in input_dict:
                current += 1
                count += 1

            if count > longest_count:
                longest_count = count
                start_number = number

    for i in range(longest_count):
        output_list.append(start_number + i)

    return output_list


input_list = [5, 4, 7, 10, 1, 3, 55, 2]
print(longest_consecutive_subsequence(input_list))