import math

def even_binomial_Coeff_Sum(n):
    result = 0
    for i in range(0, n+1, 2):
        result += math.comb(n, i)
    return result

def check(candidate):
    assert even_binomial_Coeff_Sum(4) == 8
    assert even_binomial_Coeff_Sum(6) == 32
    assert even_binomial_Coeff_Sum(2) == 2

check(even_binomial_Coeff_Sum)