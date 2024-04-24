def largest_neg(list1):
    neg_numbers = [num for num in list1 if num < 0]
    if not neg_numbers:
        return "No negative numbers found"
    return max(neg_numbers)

# Test the function with the examples from the problem statement




def check(candidate):
    assert largest_neg([1,2,3,-4,-6]) == -6
    assert largest_neg([1,2,3,-8,-9]) == -9
    assert largest_neg([1,2,3,4,-1]) == -1

check(largest_neg)