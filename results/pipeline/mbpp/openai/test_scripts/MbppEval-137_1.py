from array import array

def zero_count(nums):
    zero_count = 0
    total_count = len(nums)
    
    for num in nums:
        if num == 0:
            zero_count += 1
    
    ratio = zero_count / total_count if total_count > 0 else 0
    return round(ratio, 2)

def check(candidate):
    assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
    assert math.isclose(zero_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8]), 0.00, rel_tol=0.001)
    assert math.isclose(zero_count([2, 4, -6, -9, 11, -12, 14, -5, 17]), 0.00, rel_tol=0.001)

check(zero_count)