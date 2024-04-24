def all_Bits_Set_In_The_Given_Range(n, l, r):
    """
    Check whether all the bits are set in the given range or not.

    Args:
        n (int): The number to check.
        l (int): The left index of the range.
        r (int): The right index of the range.

    Returns:
        bool: True if all the bits are set in the given range, False otherwise.
    """
    mask = (1 << (r - l + 1)) - 1
    mask <<= (l - 1)
    return (n & mask) == mask

def check(candidate):
    assert all_Bits_Set_In_The_Given_Range(4,1,2) == True
    assert all_Bits_Set_In_The_Given_Range(17,2,4) == True
    assert all_Bits_Set_In_The_Given_Range(39,4,6) == False

check(all_Bits_Set_In_The_Given_Range)