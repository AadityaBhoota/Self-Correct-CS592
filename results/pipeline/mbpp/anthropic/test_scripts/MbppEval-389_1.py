def find_lucas(n):
    """
    Write a function to find the n'th lucas number.

    Examples:
    find_lucas(9) == 76
    find_lucas(4) == 7
    find_lucas(3) == 4
    """
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        a, b = 2, 1
        for _ in range(3, n+1):
            a, b = b, a + b
        return b

def check(candidate):
    assert find_lucas(9) == 76
    assert find_lucas(4) == 7
    assert find_lucas(3) == 4

check(find_lucas)