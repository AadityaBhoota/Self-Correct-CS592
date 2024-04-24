def opposite_Signs(x, y):
    """
    Write a python function to check whether the given two integers have opposite sign or not.

    Examples:
    opposite_Signs(1, -2) == True
    opposite_Signs(3, 2) == False
    opposite_Signs(-10, -10) == False
    """
    return (x < 0 and y > 0) or (x > 0 and y < 0)

def check(candidate):
    assert opposite_Signs(1,-2) == True
    assert opposite_Signs(3,2) == False
    assert opposite_Signs(-10,-10) == False
    assert opposite_Signs(-2,2) == True

check(opposite_Signs)