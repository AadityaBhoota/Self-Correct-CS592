def find_equal_tuple(Input, length):
    for tup in Input:
        if len(tup) != length:
            return 'All tuples do not have the same length'
    return 'All tuples have the same length'

def check(candidate):
    assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
    assert get_equal([(1, 2, 3), (4, 5, 6, 7)]) == False
    assert get_equal([(1, 2), (3, 4)]) == True

check(find_equal_tuple)