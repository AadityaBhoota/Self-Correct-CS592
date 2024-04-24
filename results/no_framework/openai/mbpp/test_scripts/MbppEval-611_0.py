def max_of_nth(test_list, N):
    if not test_list:
        return None

    max_val = None
    for row in test_list:
        if len(row) <= N:
            continue
        if max_val is None or row[N] > max_val:
            max_val = row[N]

    return max_val

# Test the function with the provided examples




def check(candidate):
    assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
    assert max_of_nth([[6, 7, 8], [2, 4, 6], [9, 10, 20]], 1) == 10
    assert max_of_nth([[7, 8, 9], [3, 5, 7], [10, 11, 21]], 1) == 11

check(max_of_nth)