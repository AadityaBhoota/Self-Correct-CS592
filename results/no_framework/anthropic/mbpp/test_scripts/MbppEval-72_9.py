import math

def dif_Square(n):
    """
    Checks whether the given number can be represented as the difference of two squares.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if the number can be represented as the difference of two squares, False otherwise.
    """
    # Check if the number is a perfect square
    sqrt = math.sqrt(n)
    if sqrt.is_integer():
        return True

    # Check if the number can be expressed as the difference of two squares
    for i in range(1, int(sqrt) + 1):
        j = n - i ** 2
        if j >= 0 and math.sqrt(j).is_integer():
            return True

    return False

def check(candidate):
    assert dif_Square(5) == True
    assert dif_Square(10) == False
    assert dif_Square(15) == True

check(dif_Square)