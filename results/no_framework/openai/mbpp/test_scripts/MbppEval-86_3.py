def centered_hexagonal_number(n):
    if n == 1:
        return 1
    return 3*n*(n-1) + 1

# Test cases




def check(candidate):
    assert centered_hexagonal_number(10) == 271
    assert centered_hexagonal_number(2) == 7
    assert centered_hexagonal_number(9) == 217

check(centered_hexagonal_number)