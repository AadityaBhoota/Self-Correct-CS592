def find_min_diff(arr, n): 
    if len(arr) == 0:
        return "Array cannot be empty"
    if not isinstance(n, int) or n <= 0:
        return "n should be a positive integer"
    
    arr.sort()
    min_diff = float('inf')
    
    for i in range(n - 1):
        diff = arr[i + 1] - arr[i]
        min_diff = min(min_diff, diff)
    
    return min_diff

def check(candidate):
    assert find_min_diff((1,5,3,19,18,25),6) == 1
    assert find_min_diff((4,3,2,6),4) == 1
    assert find_min_diff((30,5,20,9),4) == 4

check(find_min_diff)