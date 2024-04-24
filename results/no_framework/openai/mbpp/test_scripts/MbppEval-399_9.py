def bitwise_xor(test_tup1, test_tup2):
    result = tuple(val1 ^ val2 for val1, val2 in zip(test_tup1, test_tup2))
    return result

def check(candidate):
    assert bitwise_xor((10, 4, 6, 9), (5, 2, 3, 3)) == (15, 6, 5, 10)
    assert bitwise_xor((11, 5, 7, 10), (6, 3, 4, 4)) == (13, 6, 3, 14)
    assert bitwise_xor((12, 6, 8, 11), (7, 4, 5, 6)) == (11, 2, 13, 13)

check(bitwise_xor)