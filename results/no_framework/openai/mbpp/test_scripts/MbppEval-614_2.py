def cummulative_sum(test_list):
    total_sum = 0
    for sub_list in test_list:
        total_sum += sum(sub_list)
    return total_sum

# Test cases




def check(candidate):
    assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
    assert cummulative_sum([(2, 4), (6, 7, 8), (3, 7)]) == 37
    assert cummulative_sum([(3, 5), (7, 8, 9), (4, 8)]) == 44

check(cummulative_sum)