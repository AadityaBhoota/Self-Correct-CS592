def get_max_sum(n):
    """
    Find the maximum sum possible by using the given equation f(n) = max((f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).
    """
    if n <= 1:
        return n
    
    # Recursive calls to find the sum of f(n/2), f(n/3), f(n/4), and f(n/5)
    return max(get_max_sum(n // 2) + get_max_sum(n // 3) + get_max_sum(n // 4) + get_max_sum(n // 5), n)

# Test cases




def check(candidate):
    assert get_max_sum(60) == 106
    assert get_max_sum(10) == 12
    assert get_max_sum(2) == 2

check(get_max_sum )