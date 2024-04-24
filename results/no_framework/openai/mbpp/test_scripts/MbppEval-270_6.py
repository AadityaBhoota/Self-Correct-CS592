def sum_even_and_even_index(arr, size):
    if not arr or size <= 0:
        return 0

    sum_even = 0
    for i in range(size):
        if i % 2 == 0 and arr[i] % 2 == 0:
            sum_even += arr[i]

    return sum_even

# Test cases




def check(candidate):
    assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
    assert sum_even_and_even_index([3, 20, 17, 9, 2, 10, 18, 13, 6, 18]) == 26
    assert sum_even_and_even_index([5, 6, 12, 1]) == 12

check(sum_even_and_even_index)