import math
def perimeter_pentagon(a):
    # Calculate the perimeter of a regular pentagon
    perimeter = 5 * a
    return perimeter

def check(candidate):
    assert perimeter_pentagon(5) == 25
    assert perimeter_pentagon(10) == 50
    assert perimeter_pentagon(15) == 75

check(perimeter_pentagon)