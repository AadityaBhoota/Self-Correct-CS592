def check_K(test_tup, K):
    return K in test_tup

# Testing the function with provided examples




def check(candidate):
    assert check_K((10, 4, 5, 6, 8), 6) == True
    assert check_K((1, 2, 3, 4, 5, 6), 7) == False
    assert check_K((7, 8, 9, 44, 11, 12), 11) == True

check(check_K)