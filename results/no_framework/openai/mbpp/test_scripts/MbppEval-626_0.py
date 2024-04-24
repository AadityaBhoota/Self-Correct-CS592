import math

def triangle_area(r) :
    if r < 0:
        return -1

    area = (r ** 2) / 2
    return area

# Test cases




def check(candidate):
    assert triangle_area(-1) == None
    assert triangle_area(0) == 0
    assert triangle_area(2) == 4

check(triangle_area)