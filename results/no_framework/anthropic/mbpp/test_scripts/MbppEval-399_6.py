def bitwise_xor(test_tup1, test_tup2):
    """
    Perform the bitwise XOR operation across the given tuples.
    
    Args:
        test_tup1 (tuple): The first tuple of integers.
        test_tup2 (tuple): The second tuple of integers.
        
    Returns:
        tuple: The result of the bitwise XOR operation.
    """
    return tuple(a ^ b for a, b in zip(test_tup1, test_tup2))

def check(candidate):
    assert bitwise_xor((10, 4, 6, 9), (5, 2, 3, 3)) == (15, 6, 5, 10)
    assert bitwise_xor((11, 5, 7, 10), (6, 3, 4, 4)) == (13, 6, 3, 14)
    assert bitwise_xor((12, 6, 8, 11), (7, 4, 5, 6)) == (11, 2, 13, 13)

check(bitwise_xor)