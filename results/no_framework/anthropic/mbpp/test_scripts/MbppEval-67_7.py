def bell_number(n):
    """
    Write a function to find the number of ways to partition a set of Bell numbers.

    Examples:
    bell_number(2) == 2
    bell_number(10) == 115975
    bell_number(56) == 6775685320645824322581483068371419745979053216268760300
    """
    if n == 0:
        return 1
    
    bell = [0] * (n + 1)
    bell[0] = 1
    
    for i in range(1, n + 1):
        for j in range(i):
            bell[i] += bell[j] * factorial(i - j, i)
    
    return bell[n]

def factorial(n, k):
    """
    Helper function to compute the falling factorial.
    """
    result = 1
    for i in range(n, n - k, -1):
        result *= i
    return result

def check(candidate):
    assert bell_number(2)==2
    assert bell_number(10)==115975
    assert bell_number(56)==6775685320645824322581483068371419745979053216268760300

check(bell_number)