def tuple_to_int(nums):
    """
    Write a function to convert a given tuple of positive integers into a single integer.

    Examples:
    tuple_to_int((1,2,3)) == 123
    tuple_to_int((4,5,6)) == 456
    tuple_to_int((5,6,7)) == 567
    """
    return int(''.join(map(str, nums)))

def check(candidate):
    assert tuple_to_int((1,2,3))==123
    assert tuple_to_int((4,5,6))==456
    assert tuple_to_int((5,6,7))==567

check(tuple_to_int)