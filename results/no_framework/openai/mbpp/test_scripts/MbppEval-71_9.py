def comb_sort(nums):
    def get_next_gap(gap):
        # Shrink factor is 1.3
        gap = (gap * 10) / 13
        if gap < 1:
            return 1
        return int(gap)

    n = len(nums)
    gap = n
    swapped = True

    while gap != 1 or swapped:
        gap = get_next_gap(gap)
        swapped = False

        for i in range(0, n - gap):
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                swapped = True

    return nums

# Test cases




def check(candidate):
    assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
    assert comb_sort([41, 32, 15, 19, 22]) == [15, 19, 22, 32, 41]
    assert comb_sort([99, 15, 13, 47]) == [13, 15, 47, 99]

check(comb_sort)