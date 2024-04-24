import math

def triangle_area(a, b, c):
    """
    Given the lengths of the three sides of a triangle, return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise, return -1.

    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    """
    # Check if the three sides form a valid triangle
    if a + b <= c or b + c <= a or a + c <= b:
        return -1

    # Calculate the semi-perimeter
    s = (a + b + c) / 2

    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return round(area, 2)

def check(candidate):

    # Check some simple cases
    assert candidate(3, 4, 5) == 6.00, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(1, 2, 10) == -1
    assert candidate(4, 8, 5) == 8.18
    assert candidate(2, 2, 2) == 1.73
    assert candidate(1, 2, 3) == -1
    assert candidate(10, 5, 7) == 16.25
    assert candidate(2, 6, 3) == -1

    # Check some edge cases that are easy to work out by hand.
    assert candidate(1, 1, 1) == 0.43, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate(2, 2, 10) == -1


check(triangle_area)