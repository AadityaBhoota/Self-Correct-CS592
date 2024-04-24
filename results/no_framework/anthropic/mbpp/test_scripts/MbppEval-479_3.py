def first_Digit(n):
    """
    Write a python function to find the first digit of a given number.

    Examples:
    first_Digit(123) == 1
    first_Digit(456) == 4
    first_Digit(12) == 1
    """
    # Convert the number to a string
    n_str = str(n)
    
    # Return the first character of the string
    return int(n_str[0])

def check(candidate):
    assert first_Digit(123) == 1
    assert first_Digit(456) == 4
    assert first_Digit(12) == 1

check(first_Digit)