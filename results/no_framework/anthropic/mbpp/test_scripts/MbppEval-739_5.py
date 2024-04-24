import math

def find_Index(n):
    """
    Write a python function to find the index of smallest triangular number with n digits.
    Examples:
    find_Index(2) == 4
    find_Index(3) == 14
    find_Index(4) == 45
    """
    index = 0
    triangular_number = 0
    
    while len(str(triangular_number)) < n:
        index += 1
        triangular_number += index
    
    return index

# Example usage




def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45

check(find_Index)