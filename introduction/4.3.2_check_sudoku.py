correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]

# Define a function check_sudoku() here:


def check_sudoku(square_list):
    n = len(square_list)

    # check if each row contains unique number from 1 to n
    for i in range(0, n):
        unique_list = list(range(1, n + 1))
        for j in range(0, n):
            if square_list[i][j] in unique_list:
                unique_list.remove(square_list[i][j])
            else:
                return False

    # check if each column contains unique number from 1 to n
    for i in range(0, n):
        unique_list = list(range(1, n + 1))
        for j in range(0, n):
            if square_list[j][i] in unique_list:
                unique_list.remove(square_list[j][i])
            else:
                return False

    return True


print(check_sudoku(correct))
# >>> True

print(check_sudoku(incorrect))
# >>> False

print(check_sudoku(incorrect2))
# >>> False

print(check_sudoku(incorrect3))
# >>> False

print(check_sudoku(incorrect4))
# >>> False

print(check_sudoku(incorrect5))
# >>> False
