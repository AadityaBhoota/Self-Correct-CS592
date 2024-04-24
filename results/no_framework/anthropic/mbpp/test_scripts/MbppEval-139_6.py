import math

def circle_circumference(r):
    '''
    Write a function to find the circumference of a circle.

    Examples:
    circle_circumference(10) == 62.830000000000005
    circle_circumference(5) == 31.415000000000003
    circle_circumference(4) == 25.132
    '''
    return 2 * math.pi * r

def check(candidate):
    assert math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)
    assert math.isclose(circle_circumference(5), 31.415000000000003, rel_tol=0.001)
    assert math.isclose(circle_circumference(4), 25.132, rel_tol=0.001)

check(circle_circumference)