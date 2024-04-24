def harmonic_sum(n):
    """
    Calculates the harmonic sum of n-1.

    The harmonic sum is the sum of the reciprocals of the positive integers up to n.
    It is calculated as: 1 + 1/2 + 1/3 + ... + 1/n.

    Args:
        n (int): The value up to which the harmonic sum is calculated.

    Returns:
        float: The harmonic sum of n-1.
    """
    if n <= 0:
        return 0
    else:
        return 1/n + harmonic_sum(n-1)

def check(candidate):
    assert math.isclose(harmonic_sum(7), 2.5928571428571425, rel_tol=0.001)
    assert math.isclose(harmonic_sum(4), 2.083333333333333, rel_tol=0.001)
    assert math.isclose(harmonic_sum(19), 3.547739657143682, rel_tol=0.001)

check(harmonic_sum)