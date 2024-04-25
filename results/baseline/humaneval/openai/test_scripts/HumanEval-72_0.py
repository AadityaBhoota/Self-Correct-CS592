def will_it_fly(q, w):
    # Check if the object is balanced (palindromic list)
    if q == q[::-1]:
        # Check if the sum of elements is less than or equal to the maximum weight
        if sum(q) <= w:
            return True
    return False

# Test the function with given examples





def check(candidate):

    # Check some simple cases
    assert candidate([3, 2, 3], 9) is True
    assert candidate([1, 2], 5) is False
    assert candidate([3], 5) is True
    assert candidate([3, 2, 3], 1) is False


    # Check some edge cases that are easy to work out by hand.
    assert candidate([1, 2, 3], 6) is False
    assert candidate([5], 5) is True


check(will_it_fly)