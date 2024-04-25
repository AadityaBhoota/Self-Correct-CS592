def even_Power_Sum(n):
    total_sum = 0
    for i in range(1, n+1):
        total_sum += (2 * i) ** 5
    return total_sum

def check(candidate):
    assert even_Power_Sum(2) == 1056
    assert even_Power_Sum(3) == 8832
    assert even_Power_Sum(1) == 32

check(even_Power_Sum)