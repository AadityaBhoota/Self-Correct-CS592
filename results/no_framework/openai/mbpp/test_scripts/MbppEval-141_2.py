def pancake_sort(nums):
    def flip(arr, k):
        arr[:k+1] = arr[:k+1][::-1]

    n = len(nums)
    for size in range(n, 1, -1):
        max_idx = nums.index(max(nums[:size]))
        flip(nums, max_idx)
        flip(nums, size - 1)

    return nums

# Test the function




def check(candidate):
    assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
    assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
    assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]

check(pancake_sort)