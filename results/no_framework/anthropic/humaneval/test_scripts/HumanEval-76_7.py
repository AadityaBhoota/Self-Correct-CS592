import math

def is_simple_power(x, n):
    """
    Returns True if a number x is a simple power of n, and False otherwise.
    
    x is a simple power of n if n**int=x, where int is an integer.
    
    Parameters:
    x (int): The number to check.
    n (int): The base to check against.
    
    Returns:
    bool: True if x is a simple power of n, False otherwise.
    """
    if n == 1:
        return x == 1
    
    if x == 1:
        return True
    
    # Check if the logarithm of x with base n is an integer
    log_x_n = math.log(x, n)
    return log_x_n.is_integer()

def check(candidate):

    # Check some simple cases
    assert candidate(16, 2)== True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(143214, 16)== False, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(4, 2)==True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(9, 3)==True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(16, 4)==True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(24, 2)==False, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(128, 4)==False, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(12, 6)==False, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate(1, 1)==True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate(1, 12)==True, "This prints if this assert fails 2 (also good for debugging!)"


check(is_simple_power)