def max_sub_array_sum_repeated(a, n, k):
    max_sum = float('-inf')
    current_sum = 0

    for _ in range(k):
        current_sum = 0
        for x in a:
            current_sum += x
            max_sum = max(max_sum, current_sum)
            if current_sum < 0:
                current_sum = 0

    return max_sum

def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)