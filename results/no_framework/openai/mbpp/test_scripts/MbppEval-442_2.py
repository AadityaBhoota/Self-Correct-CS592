def positive_count(nums):
    total = len(nums)
    positives = sum(1 for num in nums if num > 0)
    
    if total == 0:
        return 0
    else:
        return round(positives / total, 2)

def check(candidate):
    assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.54
    assert positive_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])==0.69
    assert positive_count([2, 4, -6, -9, 11, -12, 14, -5, 17])==0.56

check(positive_count)