def check_min_heap_helper(arr, i):
    n = len(arr)
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[i] > arr[left]:
        return False

    if right < n and arr[i] > arr[right]:
        return False

    return True

def check(candidate):
    assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
    assert check_min_heap([2, 3, 4, 5, 10, 15]) == True
    assert check_min_heap([2, 10, 4, 5, 3, 15]) == False

check(check_min_heap_helper)