import math 

def sumofFactors(n): 
    sum_of_factors = 0
    
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i % 2 == 0:
                sum_of_factors += i
                
            if n//i != i and (n//i) % 2 == 0:
                sum_of_factors += n // i
                
    return sum_of_factors

def check(candidate):
    assert sumofFactors(18) == 26
    assert sumofFactors(30) == 48
    assert sumofFactors(6) == 8

check(sumofFactors)