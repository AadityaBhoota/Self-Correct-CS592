import math

def sumOfEvenFactors(n):
    total = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i % 2 == 0:
                total += i
            if (n // i) != i and (n // i) % 2 == 0:
                total += (n // i)
    return total

def check(candidate):
    assert sumofFactors(18) == 26
    assert sumofFactors(30) == 48
    assert sumofFactors(6) == 8

check(sumofFactors)