def is_undulating(n): 
    n_str = str(n)
    if len(n_str) < 3:
        return False
    
    increasing = n_str[0] < n_str[1] > n_str[0]
    for i in range(1, len(n_str) - 1):
        if (n_str[i-1] < n_str[i] > n_str[i+1]) != increasing:
            return False
        increasing = not increasing

    return True

# Test cases




def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)