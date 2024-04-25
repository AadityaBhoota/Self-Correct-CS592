def sum(a, b):
    """
    Write a python function to find the sum of common divisors of two given numbers.

    Examples:
    sum(10, 15) == 6
    sum(100, 150) == 93
    sum(4, 6) == 3
    """
    divisors_a = [i for i in range(1, a+1) if a % i == 0]
    divisors_b = [i for i in range(1, b+1) if b % i == 0]
    common_divisors = [x for x in divisors_a if x in divisors_b]
    return sum(common_divisors)

def check(candidate):
    assert sum(10,15) == 6
    assert sum(100,150) == 93
    assert sum(4,6) == 3

check(sum)