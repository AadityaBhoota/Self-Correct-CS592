def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    total_sum = 0

    for i in range(n):
        for j in range(i, n):
            product = 1
            for k in range(i, j + 1):
                product *= arr[k]
            total_sum += product

    return total_sum

def check(candidate):
    assert sum_Of_Subarray_Prod([1,2,3]) == 20
    assert sum_Of_Subarray_Prod([1,2]) == 5
    assert sum_Of_Subarray_Prod([1,2,3,4]) == 84

check(sum_Of_Subarray_Prod)