def odd_Equivalent(s, n):
    """
    Find the number of numbers with an odd value when rotating a binary string the given number of times.

    Args:
    s (str): The binary string to be rotated.
    n (int): The number of times to rotate the binary string.

    Returns:
    int: The number of numbers with an odd value after rotation.
    """
    count = 0
    for _ in range(n):
        # Rotate the binary string to the left by one position
        s = s[1:] + s[0]
        # Convert the rotated binary string to an integer
        num = int(s, 2)
        # Check if the integer has an odd value
        if num % 2 == 1:
            count += 1
    return count

def check(candidate):
    assert odd_Equivalent("011001",6) == 3
    assert odd_Equivalent("11011",5) == 4
    assert odd_Equivalent("1010",4) == 2

check(odd_Equivalent)