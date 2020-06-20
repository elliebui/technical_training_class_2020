def solve_rule_1(input_matrix):
    n = len(input_matrix)
    # by column
    for i in range(n - 1):
        for j in range(n):
            if input_matrix[i][j] == input_matrix[i + 1][j] and input_matrix[i][j] != 0:
                # if the 2 elements in middle of column are the same
                if i - 1 >= 0 and i + 2 < n:
                    if input_matrix[i][j] == 1:
                        input_matrix[i - 1][j] = 2
                        input_matrix[i + 2][j] = 2
                    else:
                        input_matrix[i - 1][j] = 1
                        input_matrix[i + 2][j] = 1
                # if the first 2 elements are the same
                if i - 1 < 0:
                    if input_matrix[i][j] == 1:
                        input_matrix[i + 2][j] = 2
                    else:
                        input_matrix[i + 2][j] = 1
                # if the last 2 elements are the same
                if i + 2 == n:
                    if input_matrix[i][j] == 1:
                        input_matrix[i - 1][j] = 2
                    else:
                        input_matrix[i - 1][j] = 1
            if i + 2 <= n - 1 and input_matrix[i][j] == input_matrix[i + 2][j] and input_matrix[i][j] != 0 and \
                    input_matrix[i + 1][j] == 0:
                if input_matrix[i][j] == 1:
                    input_matrix[i + 1][j] = 2
                else:
                    input_matrix[i + 1][j] = 1

    # by row
    for row in input_matrix:
        for j in range(n - 1):
            if row[j] == row[j + 1] and row[j] != 0:
                # if the 2 elements in middle of row are the same
                if j - 1 >= 0 and j + 2 < n:
                    if row[j] == 1:
                        row[j - 1] = 2
                        row[j + 2] = 2
                    else:
                        row[j - 1] = 1
                        row[j + 2] = 1
                # if the first 2 elements are the same
                if j - 1 < 0:
                    if row[j] == 1:
                        row[j + 2] = 2
                    else:
                        row[j + 2] = 1
                # if the last 2 elements are the same
                if j + 2 == n:
                    if row[j] == 1:
                        row[j - 1] = 2
                    else:
                        row[j - 1] = 1
            if j + 2 <= n - 1 and row[j] == row[j + 2] and row[j] != 0 and row[j + 1] == 0:
                if row[j] == 1:
                    row[j + 1] = 2
                else:
                    row[j + 1] = 1

    return input_matrix


def solve_rule_2(input_matrix):
    n = len(input_matrix)
    # by column
    for i in range(n):
        one_count = 0
        two_count = 0
        for j in range(n):
            if input_matrix[j][i] == 1:
                one_count += 1
            elif input_matrix[j][i] == 2:
                two_count += 1
        if one_count == n / 2:
            for j in range(n):
                if input_matrix[j][i] == 0:
                    input_matrix[j][i] = 2
        if two_count == n / 2:
            for j in range(n):
                if input_matrix[j][i] == 0:
                    input_matrix[j][i] = 1

    # by row
    for row in input_matrix:
        one_count = 0
        two_count = 0
        for j in range(n):
            if row[j] == 1:
                one_count += 1
            elif row[j] == 2:
                two_count += 1
        if one_count == n / 2:
            for j in range(n):
                if row[j] == 0:
                    row[j] = 2
        if two_count == n / 2:
            for j in range(n):
                if row[j] == 0:
                    row[j] = 1

    return input_matrix


def solve_rule_3(input_matrix):
    n = len(input_matrix)
    # by column
    list_columns = list()
    for i in range(n):
        list_columns.append(get_column(input_matrix, i))
    for i in range(n):
        if list_columns[i].count(0) == 2:
            first_index = list_columns[i].index(0)
            second_index = list_columns[i].index(0, first_index + 1, n)
            for j in range(n):
                list_columns[i].pop(first_index)
                list_columns[i].pop(second_index - 1)
                if i != j:
                    j_first_index = list_columns[j][first_index]
                    j_second_index = list_columns[j][second_index]
                    list_columns[j].pop(first_index)
                    list_columns[j].pop(second_index-1)
                    if list_columns[i] == list_columns[j] and j_first_index != 0 and j_second_index != 0:
                        if j_first_index == 1:
                            input_matrix[first_index][i] = 2
                        else:
                            input_matrix[first_index][i] = 1
                        if j_second_index == 1:
                            input_matrix[second_index][i] = 2
                        else:
                            input_matrix[second_index][i] = 1
                    else:
                        list_columns[i].insert(first_index, 0)
                        list_columns[i].insert(second_index, 0)
                        list_columns[j].insert(first_index, j_first_index)
                        list_columns[j].insert(second_index, j_second_index)
                else:
                    list_columns[i].insert(first_index, 0)
                    list_columns[i].insert(second_index, 0)

    # by row
    for i in range(n):
        if input_matrix[i].count(0) == 2:
            first_index = input_matrix[i].index(0)
            second_index = input_matrix[i].index(0, first_index + 1, n)
            for j in range(n):
                input_matrix[i].pop(first_index)
                input_matrix[i].pop(second_index - 1)
                if i != j:
                    j_first_index = input_matrix[j][first_index]
                    j_second_index = input_matrix[j][second_index]
                    input_matrix[j].pop(first_index)
                    input_matrix[j].pop(second_index-1)
                    if input_matrix[i] == input_matrix[j] and j_first_index != 0 and j_second_index != 0:
                        if j_first_index == 1:
                            input_matrix[i].insert(first_index, 2)
                            input_matrix[j].insert(first_index, 1)
                        else:
                            input_matrix[i].insert(first_index, 1)
                            input_matrix[j].insert(first_index, 2)

                        if j_second_index == 1:
                            input_matrix[i].insert(second_index, 2)
                            input_matrix[j].insert(second_index, 1)
                        else:
                            input_matrix[i].insert(second_index, 1)
                            input_matrix[j].insert(second_index, 2)
                    else:
                        input_matrix[i].insert(first_index, 0)
                        input_matrix[i].insert(second_index, 0)
                        input_matrix[j].insert(first_index, j_first_index)
                        input_matrix[j].insert(second_index, j_second_index)
                else:
                    input_matrix[i].insert(first_index, 0)
                    input_matrix[i].insert(second_index, 0)

    return input_matrix


def get_column(matrix, i):
    return [row[i] for row in matrix]


def is_matrix_complete(input_matrix):
    n = len(input_matrix)
    for i in range(n):
        for j in range(n):
            if input_matrix[i][j] == 0:
                return False
    return True


def print_matrix(input_matrix):
    for row in input_matrix:
        print(row)


def solve_game(input_matrix):
    while not is_matrix_complete(input_matrix):
        solve_rule_3(solve_rule_2(solve_rule_1(input_matrix)))
    return input_matrix


input_1 = [
    [1, 1, 0, 0],
    [2, 0, 0, 0],
    [0, 0, 0, 2],
    [0, 0, 1, 0],
]
print_matrix(solve_game(input_1))

"""
Answer:
[1, 1, 2, 2]
[2, 1, 2, 1]
[1, 2, 1, 2]
[2, 2, 1, 1]
"""

input_matrix_3 = [
  [0, 0, 0, 1, 1, 0],
  [0, 0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0, 1],
  [0, 2, 0, 0, 0, 0],
  [0, 0, 0, 0, 2, 2],
  [0, 0, 0, 0, 2, 0],
]
print_matrix(solve_game(input_matrix_3))

"""
Answer:
1, 2, 2, 1, 1, 2]
[2, 1, 2, 1, 2, 1]
[2, 2, 1, 2, 1, 1]
[1, 2, 1, 2, 1, 2]
[1, 1, 2, 1, 2, 2]
[2, 1, 1, 2, 2, 1]
"""