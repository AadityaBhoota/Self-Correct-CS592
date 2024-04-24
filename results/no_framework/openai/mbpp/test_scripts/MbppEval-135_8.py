def hexagonal_num(n):
    if n <= 0:
        return None
    return n * (2 * n - 1)

# Test examples




def check(candidate):
    assert hexagonal_num(10) == 190
    assert hexagonal_num(5) == 45
    assert hexagonal_num(7) == 91

check(hexagonal_num)