def is_woodall(x):
    """
    Checks if the given number is a Woodall number.

    A Woodall number is a number of the form 2^n - 1, where n is a positive integer.

    Args:
        x (int): The number to be checked.

    Returns:
        bool: True if the number is a Woodall number, False otherwise.
    """
    n = 1
    while 2 ** n - 1 <= x:
        if 2 ** n - 1 == x:
            return True
        n += 1
    return False

def check(candidate):
    assert is_woodall(383) == True
    assert is_woodall(254) == False
    assert is_woodall(200) == False

check(is_woodall)