def sum_odd(l, r): 
    sum = 0
    for i in range(l, r+1): 
        if i % 2 != 0: 
            sum += i 
    return sum

# Test cases




def check(candidate):
    assert sum_in_range(2,5) == 8
    assert sum_in_range(5,7) == 12
    assert sum_in_range(7,13) == 40

check(sum_odd)