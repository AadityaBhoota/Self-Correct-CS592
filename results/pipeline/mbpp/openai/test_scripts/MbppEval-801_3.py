def test_three_equal(x, y, z):
    if x == y == z:
        return 3
    elif x == y or y == z or x == z:
        return 2
    else:
        return 0

def check(candidate):
    assert test_three_equal(1,1,1) == 3
    assert test_three_equal(-1,-2,-3) == 0
    assert test_three_equal(1,2,2) == 2

check(test_three_equal)