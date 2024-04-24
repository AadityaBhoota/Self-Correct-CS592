def all_Bits_Set_In_The_Given_Range(n, l, r):
    # Create a mask with '1' bits in the range [l, r]
    mask = (2**(r-l+1) - 1) << (l-1)
    
    # Check if the bits in the given range are all unset by bitwise AND with the mask
    return n & mask == 0

# Test cases




def check(candidate):
    assert all_Bits_Set_In_The_Given_Range(4,1,2) == True
    assert all_Bits_Set_In_The_Given_Range(17,2,4) == True
    assert all_Bits_Set_In_The_Given_Range(39,4,6) == False

check(all_Bits_Set_In_The_Given_Range)