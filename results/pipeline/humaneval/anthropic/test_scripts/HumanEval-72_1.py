def will_it_fly(q, w):
    total_weight = 0
    for i in range(len(q)):
        if q[i] != q[len(q) - 1 - i]:
            return False
        total_weight += q[i]
    return total_weight <= w

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