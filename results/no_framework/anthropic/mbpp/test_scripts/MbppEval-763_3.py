def find_min_diff(arr, n):
    """
    Finds the minimum difference between any two elements in a given array.

    Parameters:
    arr (iterable): The input array.
    n (int): The length of the input array.

    Returns:
    int: The minimum difference between any two elements in the array.
    """
    if n < 2:
        return 0

    arr.sort()  # Sort the array in ascending order
    min_diff = float('inf')  # Initialize min_diff to positive infinity

    for i in range(1, n):
        diff = abs(arr[i] - arr[i-1])
        min_diff = min(min_diff, diff)

    return min_diff

def check(candidate):
    assert find_min_diff((1,5,3,19,18,25),6) == 1
    assert find_min_diff((4,3,2,6),4) == 1
    assert find_min_diff((30,5,20,9),4) == 4

check(find_min_diff)