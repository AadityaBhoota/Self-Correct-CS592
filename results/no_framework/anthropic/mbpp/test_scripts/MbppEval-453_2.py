import math

def sumofFactors(n):
    '''
    Write a python function to find the sum of even factors of a number.

    Examples:
    sumofFactors(18) == 26
    sumofFactors(30) == 48
    sumofFactors(6) == 8
    '''
    total_sum = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i % 2 == 0:
                total_sum += i
            if (n // i) % 2 == 0 and (n // i) != i:
                total_sum += (n // i)
    return total_sum

def check(candidate):
    assert sumofFactors(18) == 26
    assert sumofFactors(30) == 48
    assert sumofFactors(6) == 8

check(sumofFactors)