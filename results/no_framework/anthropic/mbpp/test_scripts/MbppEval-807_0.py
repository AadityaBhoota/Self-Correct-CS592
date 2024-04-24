def first_odd(nums):
    """
    Find the first odd number in a given list of numbers.

    Args:
        nums (list): A list of numbers.

    Returns:
        int: The first odd number in the list, or None if no odd numbers are found.
    """
    for num in nums:
        if num % 2 != 0:
            return num
    return None

def check(candidate):
    assert first_odd([1,3,5]) == 1
    assert first_odd([2,4,1,3]) == 1
    assert first_odd ([8,9,1]) == 9

check(first_odd)