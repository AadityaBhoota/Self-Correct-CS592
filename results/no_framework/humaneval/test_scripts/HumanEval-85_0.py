def add(lst):
    result = 0
    for idx, num in enumerate(lst):
        if idx % 2 != 0 and num % 2 == 0:
            result += num
    return result

# Test the function with the provided example


def check(candidate):

    # Check some simple cases
    assert candidate([4, 88]) == 88
    assert candidate([4, 5, 6, 7, 2, 122]) == 122
    assert candidate([4, 0, 6, 7]) == 0
    assert candidate([4, 4, 6, 8]) == 12

    # Check some edge cases that are easy to work out by hand.
    

check(add)