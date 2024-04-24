def last_Digit_Factorial(n):
    """
    Write a python function to find the last digit in factorial of a given number.

    Examples:
    last_Digit_Factorial(4) == 4
    last_Digit_Factorial(21) == 0
    last_Digit_Factorial(30) == 0
    """
    if n == 0:
        return 1
    else:
        return (n * last_Digit_Factorial(n-1)) % 10

# Test cases




def check(candidate):
    assert last_Digit_Factorial(4) == 4
    assert last_Digit_Factorial(21) == 0
    assert last_Digit_Factorial(30) == 0

check(last_Digit_Factorial)