def sum_even_and_even_index(arr, n):
    sum_even = 0
    for i in range(n):
        if i % 2 == 0 and arr[i] % 2 == 0:
            sum_even += arr[i]
    return sum_even

# Test the function with the given examples




def check(candidate):
    assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
    assert sum_even_and_even_index([3, 20, 17, 9, 2, 10, 18, 13, 6, 18]) == 26
    assert sum_even_and_even_index([5, 6, 12, 1]) == 12

check(sum_even_and_even_index)