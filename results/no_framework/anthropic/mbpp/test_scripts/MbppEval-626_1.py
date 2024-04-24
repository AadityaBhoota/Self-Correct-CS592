import math

def triangle_area(r):
    """
    Write a python function to find the area of the largest triangle that can be inscribed in a semicircle with a given radius.

    Examples:
    triangle_area(0) == 0
    triangle_area(-1) == -1
    triangle_area(2) == 4
    """
    if r < 0:
        return -1
    elif r == 0:
        return 0
    else:
        area = (1/2) * r * r * math.sin(math.pi / 3)
        return area

def check(candidate):
    assert triangle_area(-1) == None
    assert triangle_area(0) == 0
    assert triangle_area(2) == 4

check(triangle_area)