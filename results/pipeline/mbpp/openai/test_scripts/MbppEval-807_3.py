def first_odd(nums):
    for num in nums:
        if num % 2 != 0:
            return num

def check(candidate):
    assert first_odd([1,3,5]) == 1
    assert first_odd([2,4,1,3]) == 1
    assert first_odd ([8,9,1]) == 9

check(first_odd)