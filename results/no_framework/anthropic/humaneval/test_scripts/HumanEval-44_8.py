def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    Return the string representation after the conversion.
    Base numbers are less than 10.
    
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:
        return '0'
    
    digits = "0123456789"
    result = ''
    
    while x > 0:
        result = digits[x % base] + result
        x //= base
    
    return result



METADATA = {}


def check(candidate):
    assert candidate(8, 3) == "22"
    assert candidate(9, 3) == "100"
    assert candidate(234, 2) == "11101010"
    assert candidate(16, 2) == "10000"
    assert candidate(8, 2) == "1000"
    assert candidate(7, 2) == "111"
    for x in range(2, 8):
        assert candidate(x, x + 1) == str(x)


check(change_base)