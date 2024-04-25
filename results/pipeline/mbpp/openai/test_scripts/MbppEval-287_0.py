def square_Sum(n):  
    sum_squares = 0
    for i in range(1, n+1):
        num = 2*i
        sum_squares += num**2
    return sum_squares

def check(candidate):
    assert square_Sum(2) == 20
    assert square_Sum(3) == 56
    assert square_Sum(4) == 120

check(square_Sum)