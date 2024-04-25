from operator import eq

def count_same_pair(nums1, nums2):
    count = 0
    if len(nums1) != len(nums2):
        return "Error: The lists must have the same length."
    
    count = 0
    
    for i in range(len(nums1)):
        if eq(nums1[i], nums2[i]):
            count += 1
    
    return count

def check(candidate):
    assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])==4
    assert count_same_pair([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8],[2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])==11
    assert count_same_pair([2, 4, -6, -9, 11, -12, 14, -5, 17],[2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])==1
    assert count_same_pair([0, 1, 1, 2],[0, 1, 2, 2])==3

check(count_same_pair)