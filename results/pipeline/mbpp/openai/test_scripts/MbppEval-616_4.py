def tuple_modulo(test_tup1, test_tup2):
    result = []
    
    for val1, val2 in zip(test_tup1, test_tup2):
        result.append(val1 % val2)

    return tuple(result)

def check(candidate):
    assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
    assert tuple_modulo((11, 5, 6, 7), (6, 7, 8, 6)) == (5, 5, 6, 1)
    assert tuple_modulo((12, 6, 7, 8), (7, 8, 9, 7)) == (5, 6, 7, 1)

check(tuple_modulo)