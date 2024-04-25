def set_left_most_unset_bit(n): 
    '''
    Write a python function to set the left most unset bit.

    Examples:
    set_left_most_unset_bit(10) == 14
    set_left_most_unset_bit(12) == 14
    set_left_most_unset_bit(15) == 15
    '''
def find_leftmost_unset_bit_position(n):
    position = 1
    
    while n & 1:
        n >>= 1
        position += 1

    return position

def check(candidate):
    assert set_left_most_unset_bit(10) == 14
    assert set_left_most_unset_bit(12) == 14
    assert set_left_most_unset_bit(15) == 15

check(set_left_most_unset_bit)