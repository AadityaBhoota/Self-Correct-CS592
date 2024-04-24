def second_smallest(numbers):
    """
    Write a function to find the second smallest number in a list.

    Examples:
    second_smallest([1, 2, -8, -2, 0, -2]) == -2
    second_smallest([1, 1, -0.5, 0, 2, -2, -2]) == -0.5
    second_smallest([2,2]) == None
    """
    if len(numbers) < 2:
        return None

    smallest = min(numbers)
    second_smallest = float('inf')

    for num in numbers:
        if num != smallest and num < second_smallest:
            second_smallest = num

    if second_smallest == float('inf'):
        return None
    else:
        return second_smallest

def check(candidate):
    assert second_smallest([1, 2, -8, -2, 0, -2])==-2
    assert second_smallest([1, 1, -0.5, 0, 2, -2, -2])==-0.5
    assert second_smallest([2,2])==None
    assert second_smallest([2,2,2])==None

check(second_smallest)