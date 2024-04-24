def max_difference(test_list):
    # Initialize max_diff to a very small value
    max_diff = float('-inf')
    
    for pair in test_list:
        current_diff = abs(pair[0] - pair[1])
        max_diff = max(max_diff, current_diff)
    
    return max_diff

# Test the function with the provided examples




def check(candidate):
    assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
    assert max_difference([(4, 6), (2, 17), (9, 13), (11, 12)]) == 15
    assert max_difference([(12, 35), (21, 27), (13, 23), (41, 22)]) == 23

check(max_difference)