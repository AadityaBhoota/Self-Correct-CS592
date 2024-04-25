def geometric_sum(n):
    total = 0
    term = 1

    for i in range(n-1):
        total += term
        term /= 2

    return total

def check(candidate):
    assert geometric_sum(7) == 1.9921875
    assert geometric_sum(4) == 1.9375
    assert geometric_sum(8) == 1.99609375

check(geometric_sum)