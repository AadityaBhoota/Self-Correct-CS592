def substract_elements(test_tup1, test_tup2):
    result = tuple(a - b for a, b in zip(test_tup1, test_tup2))
    return result

# Test cases




def check(candidate):
    assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
    assert substract_elements((11, 2, 3), (24, 45 ,16)) == (-13, -43, -13)
    assert substract_elements((7, 18, 9), (10, 11, 12)) == (-3, 7, -3)

check(substract_elements)