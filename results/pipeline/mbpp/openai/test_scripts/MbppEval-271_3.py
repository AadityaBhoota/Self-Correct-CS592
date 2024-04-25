def even_Power_Sum(n): 
    sum_power = 0
    
    for i in range(1, n + 1):
        even_num = 2 * i
        power = even_num ** 5
        sum_power += power
        
    return sum_power

def check(candidate):
    assert even_Power_Sum(2) == 1056
    assert even_Power_Sum(3) == 8832
    assert even_Power_Sum(1) == 32

check(even_Power_Sum)