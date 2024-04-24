def max_sum(arr):
    n = len(arr)
    
    # Create two arrays to store the increasing and decreasing sequences
    inc = [1] * n
    dec = [1] * n
    
    # Compute the longest increasing subsequence
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            inc[i] = inc[i-1] + 1
    
    # Compute the longest decreasing subsequence
    for i in range(n-2, -1, -1):
        if arr[i] > arr[i+1]:
            dec[i] = dec[i+1] + 1
    
    # Find the maximum sum of a bitonic subsequence
    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, inc[i] + dec[i] - 1)
    
    return max_sum

def check(candidate):
    assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
    assert max_sum([80, 60, 30, 40, 20, 10]) == 210
    assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30]) == 138

check(max_sum)