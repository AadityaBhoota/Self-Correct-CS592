def count_list(input_list):
    return len([item for item in input_list if isinstance(item, list)])

# Test the function with the provided examples




def check(candidate):
    assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
    assert count_list([[1,2],[2,3],[4,5]]) == 3
    assert count_list([[1,0],[2,0]]) == 2

check(count_list)