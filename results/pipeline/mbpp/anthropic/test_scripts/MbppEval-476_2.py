def big_sum(nums):
    smallest = min(nums)
    largest = max(nums)
    return smallest + largest

def check(candidate):
    assert big_sum([1,2,3]) == 4
    assert big_sum([-1,2,3,4]) == 3
    assert big_sum([2,3,6]) == 8

check(big_sum)