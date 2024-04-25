def power(a, b):
    if b == 0:
        return 1
    
    result = 1
    for _ in range(b):
        result *= a
    
    return result

def check(candidate):
    assert power(3,4) == 81
    assert power(2,3) == 8
    assert power(5,5) == 3125

check(power)