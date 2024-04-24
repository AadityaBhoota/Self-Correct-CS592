def differ_At_One_Bit_Pos(a, b):
    # Count the number of differing bits using XOR
    xor_result = a ^ b
    
    # Check if there is only one set bit in the result
    return xor_result & xor_result - 1 == 0

# Test cases




def check(candidate):
    assert differ_At_One_Bit_Pos(13,9) == True
    assert differ_At_One_Bit_Pos(15,8) == False
    assert differ_At_One_Bit_Pos(2,4) == False
    assert differ_At_One_Bit_Pos(2, 3) == True
    assert differ_At_One_Bit_Pos(5, 1) == True
    assert differ_At_One_Bit_Pos(1, 5) == True

check(is_Power_Of_Two )