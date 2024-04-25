def square_Sum(n):
    return n * (n + 1) * (2 * n + 1) // 6

def check(candidate):
    assert square_Sum(2) == 10
    assert square_Sum(3) == 35
    assert square_Sum(4) == 84

check(square_Sum)