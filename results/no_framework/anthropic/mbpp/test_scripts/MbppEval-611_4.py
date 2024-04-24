def max_of_nth(test_list, N):
    """
    Write a function which given a matrix represented as a list of lists returns the max of the n'th column.

    Examples:
    max_of_nth([(5, 6, 7), (1, 3, 5), (8, 9, 19)], 2) == 19
    max_of_nth([(6, 7, 8), (2, 4, 6), (9, 10, 20)], 1) == 10
    max_of_nth([(7, 8, 9), (3, 5, 7), (10, 11, 21)], 1) == 11
    """
    if not test_list:
        return None

    max_values = [float('-inf')] * len(test_list[0])

    for row in test_list:
        for i, value in enumerate(row):
            if value > max_values[i]:
                max_values[i] = value

    return max_values[N]

def check(candidate):
    assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
    assert max_of_nth([[6, 7, 8], [2, 4, 6], [9, 10, 20]], 1) == 10
    assert max_of_nth([[7, 8, 9], [3, 5, 7], [10, 11, 21]], 1) == 11

check(max_of_nth)