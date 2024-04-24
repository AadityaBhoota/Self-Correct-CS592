def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

# Test the function




def check(candidate):
    assert sum_digits(345)==12
    assert sum_digits(12)==3
    assert sum_digits(97)==16

check(sum_digits)