def is_perfect_square(n):
    # Check if the square root of the number is an integer
    if n < 0:
        return False
    
    sqrt_n = int(n ** 0.5)
    return sqrt_n * sqrt_n == n

# Test cases




def check(candidate):
    assert not is_perfect_square(10)
    assert is_perfect_square(36)
    assert not is_perfect_square(14)
    assert is_perfect_square(14*14)
    assert not is_perfect_square(125)
    assert is_perfect_square(125*125)

check(is_perfect_square)