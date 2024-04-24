def cummulative_sum(test_list):
    """
    Write a function to find the cumulative sum of all the values that are present in the given tuple list.

    Examples:
    cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
    cummulative_sum([(2, 4), (6, 7, 8), (3, 7)]) == 37
    cummulative_sum([(3, 5), (7, 8, 9), (4, 8)]) == 44
    """
    total = 0
    for tup in test_list:
        total += sum(tup)
    return total

def check(candidate):
    assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
    assert cummulative_sum([(2, 4), (6, 7, 8), (3, 7)]) == 37
    assert cummulative_sum([(3, 5), (7, 8, 9), (4, 8)]) == 44

check(cummulative_sum)