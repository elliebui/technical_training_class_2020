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
        for j in range(n):
            if i != j and list_columns[i] == list_columns[j]:
                if list_columns[i].count(0) == 2:
                    first_index = list_columns[i].index(0)
                    second_index = list_columns[i].index(0, first_index + 1, n)
                    input_matrix[first_index][i] = 1
                    input_matrix[second_index][i] = 2
                    input_matrix[first_index][j] = 2
                    input_matrix[second_index][j] = 1

    # by row
    for i in range(n):
        for j in range(n):
            if i != j and input_matrix[i] == input_matrix[j]:
                if input_matrix[i].count(0) == 2:
                    first_index = input_matrix[i].index(0)
                    second_index = input_matrix[i].index(0, first_index + 1, n)
                    input_matrix[i][first_index] = 1
                    input_matrix[i][second_index] = 2
                    input_matrix[j][first_index] = 2
                    input_matrix[j][second_index] = 1

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


input_matrix = [
    [1, 1, 0, 0],
    [2, 0, 0, 0],
    [0, 0, 0, 2],
    [0, 0, 1, 0],
]
# print_matrix(solve_game(input_matrix))
print_matrix(solve_rule_1(input_matrix))
print()
print_matrix(solve_rule_2(input_matrix))
print()
print_matrix(solve_rule_1(input_matrix))
print()
print_matrix(solve_rule_2(input_matrix))
print()
print_matrix(solve_rule_2(input_matrix))

# print_matrix(solve_rule_3(solve_rule_2(solve_rule_1(input_matrix))))
